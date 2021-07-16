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
from time import sleep
import arcpy

__version__ = "2020-07-16.1"

def set_field_value(input_fc, fieldname, value):
    """ Update the named field in every row of the input feature class with the given value. """
    
    arcpy.AddMessage("Version %s" % __version__)
    print("field, value = ", fieldname, value)
    
    start    = 0
    step     = 1
    maxcount = int(arcpy.GetCount_management(input_fc).getOutput(0))
    
    arcpy.SetProgressor("step", "Doing serious work here.", start, maxcount, step)

    # We don't use OID here, this just an example
    # The updateRow operation is faster if you load only the fields you need,
    # in our case that would be specified by 'fieldname'.
    fields = ["OID@", fieldname]

    with arcpy.da.UpdateCursor(input_fc, fields) as cursor:
        t = 0
        for row in cursor:
            msg = "Working.. step %d of %d" % (t,maxcount)
            print(msg) # This shows up in the IDE Debug Console.

            arcpy.SetProgressorLabel(msg)

            # If there is a type error here, I really expect arcpy
            # to throw an error but it does not appear to!
            row[1] = value
            cursor.updateRow(row)
            sleep(.50) # pretend we're doing something so progressor will work.
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
