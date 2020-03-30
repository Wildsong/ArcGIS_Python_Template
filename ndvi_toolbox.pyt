# -*- coding: utf-8 -*-
"""
NDVI Toolbox (a ".pyt" file)

@author: Brian Wilson <brian@wildsong.biz>
"""
import os
import arcpy
import arcpy.sa
from arcpy.sa import Raster

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of this .pyt file)."""
        self.label = "NDVI Toolbox"
        self.alias = ""
        self.description = """My toolbox containing python tools!"""

        # List of tool classes associated with this toolbox
        self.tools = [
            NDVI_calculate_tool
        ]

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
        #self.category = "Raster" # Use your own category here, or an existing one.
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
        SA = "Spatial"
        if not arcpy.CheckExtension(SA):
            raise Exception("Spatial Analyst license not available.")
        return True
        
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


def calculate_ndvi(red_rd, nir_rd, output_rd):
 
    # Get a spatial analyst license
    SA = "Spatial"
    if not arcpy.CheckExtension(SA):
        raise Exception("No license is available for %s" % SA)

    arcpy.CheckOutExtension(SA)

    # Wrapped in an exception handler so license always gets returned.
    try:
        Red   = arcpy.sa.Float(red_rd)
        NIR   = arcpy.sa.Float(nir_rd)

        diff  = arcpy.sa.Arithmetic(NIR, Red, "Minus")
        sum   = arcpy.sa.Arithmetic(NIR, Red, "Add")
        ndvi = arcpy.sa.Arithmetic(diff, sum, "Divide")

        ndvi.save(output_rd)

    except Exception as e:
        # This typically happens if there is a missing raster
        # or inputs are not valid (eg you pass in a vector)
        raise e
    finally:
        arcpy.CheckInExtension(SA)

    return

# That's all!
