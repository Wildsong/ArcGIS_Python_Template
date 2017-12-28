#!/usr/bin/env python

import arcpy
from arcpy import mapping as MAP
import some_sample_code

class Sample_Tool(object):
    """This class has the methods you need to define
       to use your code as an ArcGIS Python Tool."""
        
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = self.__class__.__name__ # Use the class name here
        self.description = """Put some descriptive text here."""
        self.canRunInBackground = False
        #self.category = "Sample" # Use your own category here, or an existing one.
        #self.stylesheet = "" # I don't know how to use this yet.
        
    def getParameterInfo(self):
        """Define parameter definitions
        """       
        params = []

        # params[0] 
        input_fc = arcpy.Parameter(name="input_fc",
                                 displayName="Input Feature Class",
                                 datatype="DEFeatureClass",
                                 parameterType="Required", # Required|Optional|Derived
                                 direction="Input", # Input|Output
                                )
        # You can set filters here for example
        #input_fc.filter.list = ["Polygon"]
        # You can set a default if you want -- this makes debugging a little easier.
        input_fc.value = "D:/GISData/photos.shp"
         
        params.append(input_fc)
        
        # params[1] 
        field = arcpy.Parameter(name="field",
                                displayName="Name of a field",
                                datatype="Field",
                                parameterType="Required", # Required|Optional|Derived
                                direction="Input", # Input|Output
                                )
        # Define this so that the list of field names will be filled in in ArcCatalog
        field.parameterDependencies = [input_fc.name]
        # You can set a filter here too for example
        #field.filter = ["Long"]
        # You can set a default here if you want
        field.value = "Name"
        
        params.append(field)
 
        # params[2] 
        number = arcpy.Parameter(name="number",
                                 displayName="Some long number",
                                 datatype="GPLong",
                                 parameterType="Required", # Required|Optional|Derived
                                 direction="Input", # Input|Output
                                )
        # You could set a list of acceptable values here for example
        number.filter.type = "ValueList"
        number.filter.list = [1,2,3,4]
        # You can set a default value here.
        number.value = 1
        
        params.append(number)
       
        # params[3] 
        depnumber = arcpy.Parameter(name="another_number",
                                    displayName="A number that depends on number",
                                    datatype="GPLong",
                                    parameterType="Required", # Required|Optional|Derived
                                    direction="Input", # Input|Output
                                    )
        # You could set a list of acceptable values here for example
        depnumber.filter.type = "ValueList"
        depnumber.filter.list = [100,200,300,400]
        # You can set a default value here.
        depnumber.value = 200
        
        params.append(depnumber)

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
        params.append(output_fc)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        # When you change the field called "number" then this function will
        # be called and the next field will change to its value * 100.        
        parameters[3].value = int(parameters[2].value)*100

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of your tool."""
        
        # Let's dump out what we know here.
        messages.addMessage("This is a test of your sample tool.")
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
        number    = parameters[2].value
        
        # Okay finally go ahead and do the work.
        some_sample_code.set_field_value(input_fc, fieldname, number)
        return

# That's all!
