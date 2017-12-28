#!/usr/bin/env python
from __future__ import print_function
import arcpy
import time

__version__ = "2"

def set_field_value(input_fc, fieldname, value):
    """This function really is just a sample
    and does not do anything interesting."""
    
    arcpy.AddMessage("Version %d" % __version__)
    print(fieldname)
    print(value)
    
    start    = 0
    maxcount = 10
    step     = 1
    
    arcpy.SetProgressor("step", "Doing serious work here.", start, maxcount, step)
    for t in range(1,maxcount+1):
        msg = "Working.. step %d of %d" % (t,maxcount)
        arcpy.SetProgressorLabel(msg)
        time.sleep(2)
        arcpy.SetProgressorPosition(t)
    
    return

# ======================================================================

# UNIT TESTING
# You can run this file directly when writing it to aid in debugging

if __name__ == '__main__':
    input_fc = "my_fc.shp"
    fieldname = "my_fieldname"
    value = 42
    
    set_field_value(input_fc, fieldname, value)
    
# That's all