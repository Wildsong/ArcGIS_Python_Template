# -*- coding: utf-8 -*-
"""
Python code that implements implements an ArcGIS Tool,
to be included in an ArcGIS Python Toolbox.

@author: Brian Wilson <brian@wildsong.biz>
"""
import os
import arcpy
from ndvi_code import calculate_ndvi

class NDVI_calculate_tool(object):
    """This class has the methods you need to define
       to use your code as an ArcGIS Python Tool.
       
       "calculate_ndvi" takes 3 arguments, 
        name of a red raster,
        name of a nir raster,
        and name of an output raster
    """
        
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = self.__class__.__name__ # Use the class name here
        self.description = """Calculate an NDVI raster from Red and NIR bands."""
        self.canRunInBackground = False
        self.category = "Raster" # Use your own category here, or an existing one.
        #self.stylesheet = "" # I don't know how to use this yet.
        
    def getParameterInfo(self):
        """Define parameter definitions.
Refer to https://desktop.arcgis.com/en/arcmap/latest/analyze/creating-tools/defining-parameters-in-a-python-toolbox.htm
        """       

        # params[0] 
        red_rd = arcpy.Parameter(name="red_rd",
                                displayName="Red raster dataset",
                                # Using a composite type here means I can 
                                # enter either a raster or a string into the form.
                                datatype=["DERasterDataset", "GPString"],
                                parameterType="Required", # Required|Optional|Derived
                                direction="Input", # Input|Output
                                )
        # You can set filters here for example
        #red_rd.filter.list = ["Polygon"]
        # You can set a default if you want -- this makes debugging a little easier.
        red_rd.value = "red.tif"
         
        # params[1] 
        nir_rd = arcpy.Parameter(name="nir_rd",
                                displayName="NIR raster dataset",
                                # Using a composite type here means I can 
                                # enter either a raster or a string into the form.
                                datatype=["DERasterDataset", "GPString"],
                                parameterType="Required", # Required|Optional|Derived
                                direction="Input", # Input|Output
                                )
        # You can set a default if you want -- this makes debugging a little easier.
        nir_rd.value = "nir.tif"

        # params[2] 
        output_rd = arcpy.Parameter(name="output_rd",
                                    displayName="Output raster dataset",
                                    datatype="DERasterDataset",
                                    parameterType="Required", # Required|Optional|Derived
                                    direction="Output", # Input|Output
                                    )
        # This output is not "dreived"
        output_rd.value = "ndvi.tif"

        return [red_rd, nir_rd, output_rd]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        SA = "NoSpatial"
        return arcpy.sa.CheckLicense(SA)
        
    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        # nothing to do here

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

        # You could get fancy here and make sure the rasters
        # are in the right format, that they are in the right projection
        # and they cover the same piece of ground
        # and so on... and issue warnings if they don't

        return

    def execute(self, parameters, messages):
        """The source code of your tool."""
        
        # Let's dump out what we know here.
        for param in parameters:
            messages.addMessage("Parameter: %s = %s" % (param.name, param.valueAsText) )
        
        # Get the parameters from our parameters list,
        # then call a generic python function.
        #
        # This separates the simple code doing the work from all
        # the crazy code here that is required to talk to ArcGIS.
        
        # See http://resources.arcgis.com/en/help/main/10.2/index.html#//018z00000063000000
        red = parameters[0].valueAsText
        nir = parameters[1].valueAsText
        out = parameters[2].valueAsText

        calculate_ndvi(red, nir, out)  
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
    ndvi_calc = NDVI_calculate_tool()

    arcpy.env.workspace = '.\\test_pro'

    # Let's try using all the defaults this time.
    params = ndvi_calc.getParameterInfo()

    try:
        ndvi_calc.execute(params, Messenger())
    except Exception as e:
        print("Something went wrong;", e)

# That's all
