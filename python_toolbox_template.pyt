"""
Python Toolbox Template (a ".pyt" file)

@author: Brian Wilson <brian@wildsong.biz>
"""
from __future__ import print_function
import arcpy

# Import all the tool classes that will be included in this toolbox.
from python_tool_template import Sample_Tool
#from python_tool_template import Sample_Tool_2

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of this .pyt file)."""
        self.label = "Sample Toolbox"
        self.alias = "SampleToolbox"  # no special characters including spaces!
        self.description = """Sample toolbox containing sample tools."""

        # List of tool classes associated with this toolbox
        self.tools = [
            Sample_Tool,
            #Sample_Tool_2
        ]

def list_tools():
    toolbox = Toolbox()
    print("toolbox:", toolbox.label)
    print("description:", toolbox.description)
    print("tools:")
    for t in toolbox.tools:
        tool = t()
        print('  ', tool.label)
        print('   description:', tool.description)
        for param in tool.getParameterInfo():
            print('    ',param.name,':',param.displayName)
        print()


if __name__ == "__main__":
    # Running this as a standalone script lists information about the toolbox and each tool.
    list_tools()
    #exit(0) # This causes the toolbox not to load in ArcGIS Pro

# That's all!
