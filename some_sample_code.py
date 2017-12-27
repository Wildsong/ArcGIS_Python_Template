#!/usr/bin/env python
from __future__ import print_function
import arcpy
import time

def set_field_value(input_fc, fieldname, value):
    """This function really is just a sample
    and does not do anything interesting."""
    
    print(input_fc)
    print(fieldname)
    print(value)
    
    for t in range(0,10):
        arcpy.AddMessage("Working.. %d" % t)
        time.sleep(1)
    
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