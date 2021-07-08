"""
This script contains the business logic for a sample in the ArcGIS Python Toolbox.

It shows how to iterate a feature class and update a field with a new value.
You could more easily do this using a call to arcpy.CalculateField_management()
but that's not as interesting an example!

@author: Brian Wilson <brian@wildsong.biz>
"""
from __future__ import print_function
from collections import namedtuple
from datetime import datetime
import arcpy

__version__ = "2020-03-29.1"

def set_field_value(input_fc, fieldname, value):
    """ Update the named field in every row of the input feature class with the given value. """
    
    arcpy.AddMessage("Version %s" % __version__)
    print(fieldname, value)
    
    start    = 0
    step     = 1
    maxcount = int(arcpy.GetCount_management(input_fc).getOutput(0))
    
    arcpy.SetProgressor("step", "Doing serious work here.", start, maxcount, step)

    # We don't need OID here, just an example
    fields = ["OID@", fieldname]

    with arcpy.da.UpdateCursor(input_fc, fields) as cursor:
        t = 0
        for row in cursor:
            msg = "Working.. step %d of %d" % (t,maxcount)
            arcpy.SetProgressorLabel(msg)

            row[1] = value
            cursor.updateRow(row)

            arcpy.SetProgressorPosition(t)
            t += 1
    return

def dump_contents(input_fc):
    """ Print the contents of the feature class, this is just a namedtuple sample. """
    fcrow = namedtuple("fcrow", ["oid", "datestamp"])
    with arcpy.da.SearchCursor(input_fc, ["OID@", "datestamp"]) as cursor:
        for row in cursor:
            feature = fcrow._make(row)
            print(feature.oid, feature.datestamp)
    return

# ======================================================================

# UNIT TESTING
# You can run this file directly when writing it to aid in debugging.
# For example, "Set as Startup File" when running under Visual Studio.

if __name__ == '__main__':
    arcpy.env.workspace = ".\\test_pro\\test_pro.gdb"
    input_fc   = "testing_data"
    fieldname  = "datestamp"
    datestring = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    arcpy.AddMessage("starting geoprocessing")
    set_field_value(input_fc, fieldname, datestring)
    
    dump_contents(input_fc)

    print("Tests successful!")

# That's all
