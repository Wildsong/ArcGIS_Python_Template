"""
This is the simplest python toolbox I could make, to help test your set up.

@author: Brian Wilson <brian@wildsong.biz>
"""
import arcpy
import time

class Toolbox(object):
    def __init__(self):
        self.label = "Hello Toolbox"
        self.alias = "HelloToolbox"
        self.tools = [Hello_Tool]

class Hello_Tool(object):

    def __init__(self):
        self.label = "Hello Tool"
        self.description = "Sends a friendly greeting as a message."
        self.canRunInBackground = False
        return

    def getParameterInfo(self):
        # I have no parameters!
        return []

    def isLicensed(self):
        return True
    
    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return
    
    def execute(self, parameters, messages):
        messages.addMessage("Hello, ArcGIS!")
        # Pretend we're doing something.
        loop = 5
        while loop:
            loop -= 1
            time.sleep(1)
        messages.addMessage("Process completed successfully!")
        return

# Unit test
if __name__ == "__main__":

    class Messenger(object):
        def addMessage(self, message):
            print(message)

    hello = Hello_Tool()
    hello.execute(None, Messenger())

# That's all!
