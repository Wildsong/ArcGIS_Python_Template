import arcpy
import arcpy.sa
from arcpy.sa import Raster

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

# ======================================================================
# UNIT TESTING
# You can run this file directly when writing it to aid in debugging.

if __name__ == '__main__':

    # You could set this to the project's FGDB if your rasters are there
    #arcpy.env.workspace = "./test_pro/test_pro.gdb"
    arcpy.env.workspace = "./test_pro"

    red_rd    = "red.tif"
    nir_rd    = "nir.tif" 

    # I suspect you can put a different extension on the output_rd string
    # for example, "ndvi.tif", to generate different format outputs??
    output_rd = "ndvi.tif"
    
    arcpy.AddMessage("starting geoprocessing")
    calculate_ndvi(red_rd, nir_rd, output_rd)

    print("Tests successful!")
    exit(0)
