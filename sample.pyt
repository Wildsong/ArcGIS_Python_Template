# Sample Python Toolbox
from __future__ import print_function
import arcpy

# Import all the tool classes that will be included in this toolbox.
from sample_tool import Sample_Tool

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of this .pyt file)."""
        self.label = "Sample Toolbox"
        self.alias = ""
        self.description = """Sample toolbox containing sample tools!"""

        # List of tool classes associated with this toolbox
        self.tools = [Sample_Tool]

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
