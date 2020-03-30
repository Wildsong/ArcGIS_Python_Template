# -*- coding: utf-8 -*-
"""
Python Toolbox Template (a ".pyt" file)

@author: Brian Wilson <brian@wildsong.biz>
"""
from __future__ import print_function
import arcpy

# Import all the tool classes that will be included in this toolbox.
from field_update_tool import Field_Update_tool
from ndvi_tools import NDVI_calculate_tool 

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of this .pyt file)."""
        self.label = "My Python Toolbox"
        self.alias = ""
        self.description = """My toolbox containing python tools!"""

        # List of tool classes associated with this toolbox
        self.tools = [
            Field_Update_tool,
            NDVI_calculate_tool
        ]

if __name__ == "__main__":
    # Running this as a standalone script tells what I know about the toolbox.
    toolbox = Toolbox()
    print("toolbox:",toolbox.label)
    print("description:",toolbox.description)
    print("tools:")
    for t in toolbox.tools:
        tool = t()
        print('  ',tool.label)
        print('   description:', tool.description)
        for param in tool.getParameterInfo():
            print('    ',param.name,':',param.displayName)

    exit(0)
    
# That's all!
