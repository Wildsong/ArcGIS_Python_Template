"""
Python code that implements implements an ArcGIS Tool,
to be included in an ArcGIS Python Toolbox.

@author: Brian Wilson <brian@wildsong.biz>
"""
import os
import arcpy
from datetime import datetime

# This is for development, so that you can edit code while running in ArcGIS Pro.
import importlib
import field_update_code
importlib.reload(field_update_code)

from field_update_code import set_field_value


class Field_Update_tool(object):
    """This class has the methods you need to define
       to use your code as an ArcGIS Python Tool."""
        
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Field Update tool"
        self.description = """Update a field in a feature class."""
        self.canRunInBackground = False
        self.category = "Example" # Use your own category here, or an existing one.
        #self.stylesheet = "" # I don't know how to use this yet.
        
    def getParameterInfo(self):
        """Define parameter definitions.
Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm
        """       

        # params[0] = feature class
        input_fc = arcpy.Parameter(name="input_fc",
            displayName="Feature Class (NOTE, contents will be modified!)",
            # Using a composite type here means I can 
            # enter either a feature class or a string into the form.
            datatype=["GPFeatureLayer", "DEFeatureClass", "GPString"],
            parameterType="Required", # Required|Optional|Derived
            direction="Input", # Input|Output
        )
        # You can set filters here for example
        #input_fc.filter.list = ["Polygon"]
        # You can set a default if you want -- this makes debugging a little easier.
        input_fc.value = ""
         
        # params[1] = field name
        field = arcpy.Parameter(name="field",
            displayName="Name of field that will have the date written into it",
            datatype="Field",
            parameterType="Required", # Required|Optional|Derived
            direction="Input", # Input|Output
        )
        # Define this so that the list of field names will be filled in in ArcCatalog
        field.parameterDependencies = [input_fc.name]

        # params[2] = a date/time thing
        datestamp = arcpy.Parameter(name="datestamp",
            displayName="A date time string",
            datatype="GPDate",
            parameterType="Required", # Required|Optional|Derived
            direction="Input", # Input|Output
        )
        # You can set a default value here.
        datestamp.value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # params[3] = a number that has to be in a range
        fixedrange = [100,500]
        number = arcpy.Parameter(name="another_number",
            displayName="A number in the range %s-%s" % (fixedrange[0],fixedrange[1]),
            datatype="GPLong",
            parameterType="Required", # Required|Optional|Derived
            direction="Input", # Input|Output
        )
        # You could set a list of acceptable values here for example
        number.filter.type = "Range"
        number.filter.list = [100,500]
        # You can set a default value here.
        number.value = 200
        
        # params[4] 
        output_fc = arcpy.Parameter(name="output_fc",
            displayName="Output feature class",
            datatype="DEFeatureClass",
            parameterType="Derived", # Required|Optional|Derived
            direction="Output", # Input|Output
        )
        # This is a derived parameter; it depends on the input feature class parameter.
        # You usually use this to define output for using the tool in ESRI models.
        output_fc.parameterDependencies = [input_fc.name]
        # Cloning tells arcpy you want the schema of this output fc to be the same as input_fc
        # See http://desktop.arcgis.com/en/desktop/latest/analyze/creating-tools/updating-schema-in-a-python-toolbox.htm#ESRI_SECTION1_0F3D82FC6ACA421E97AC6D23D95AF19D
        output_fc.schema.clone = True

        return [input_fc, field, datestamp, number, output_fc]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        if parameters[0].altered:
            # If the field is not in the new feature class
            # then switch to the first field
            try:
                l = [f.name for f in arcpy.ListFields(parameters[0].valueAsText)]
                if not parameters[1].valueAsText in l:
                    parameters[1].value = l[0]
            except:
                # Could not read the field list
                parameters[1].value = ""

        if not parameters[3].altered:
            # When you change the field called "number" then this function will
            # be called and the next field will change to its value * 100.        
            parameters[3].value = int(parameters[2].value)*100

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

        if parameters[2].value == 2:
            parameters[2].setWarningMessage("Sample warning, you set the number to 2.")
        return

    def execute(self, parameters, messages):
        """The source code of your tool."""
        
        # Let's dump out what we know here.
        messages.addMessage("This is a test of your tool.")
        for param in parameters:
            messages.addMessage("Parameter: %s = %s" % (param.name, param.valueAsText) )
        
        # Get the parameters from our parameters list,
        # then call a generic python function.
        #
        # This separates the code doing the work from all
        # the crazy code required to talk to ArcGIS.
        
        # See http://resources.arcgis.com/en/help/main/10.2/index.html#//018z00000063000000
        input_fc  = parameters[0].valueAsText
        fieldname = parameters[1].valueAsText
        datestamp = parameters[2].valueAsText
        depnumber = parameters[3].value
        output_fc = parameters[4].valueAsText
        
        set_field_value(input_fc, fieldname, datestamp)
        # Okay finally go ahead and do the work.
        messages.addMessage("Okay, I put \"%s\" in the \"%s\" field in \"%s\"." % 
            (datestamp, fieldname, output_fc))
        return
    
# =============================================================================
if __name__ == "__main__":
    # This is an example of how you could set up a unit test for this tool.
    # You can run this tool from a debugger or from the command line
    # to check it for errors before you try it in ArcGIS.
    
    class Messenger(object):
        def addMessage(self, message):
            print(message)

    # Get an instance of the tool.
    update_datestamp = Field_Update_tool()
    # Read its default parameters.
    params = update_datestamp.getParameterInfo()

    # Set some test values into the instance
    arcpy.env.workspace = '.\\test_pro\\test_pro.gdb'
    params[0].value = os.path.join(arcpy.env.workspace, "testing_data")
    params[1].value = "datestamp"
    params[2].value = "2021/07/08 12:34"
    params[3].value = 100
    params[4].value = "testing_output"
    
    # Run it.
    update_datestamp.execute(params, Messenger())

# That's all
