# ArcGIS_Python_Template
Example of how to set up a Python Toolbox for ESRI ArcGIS Pro.

Tested with ArcGIS Pro 2.8 / Python 3.7.10

*2020-03-29 This project has been updated to work with either ArcGIS Desktop or ArcGIS Pro.*
In former days I tested it with ArcGIS Desktop 10.8 / Python 2.7
It *probably* still works with Desktop. I no longer care.

## Overview

This project serves as a starting point when creating ArcGIS Python Tools.

In the ESRI world, "Python Tool" and "Python Toolbox" have specific
meanings.  They were added starting sometime around ArcGIS 10.1. 

You can write a "script tool" in Python but this approach splits apart
the definition of parameters (done in Pro) from the Python and further,
validator code remains trapped inside the proprietary binary ArcGIS "Toolbox" (.tbx) file where it cannot be maintained.

With Python Toolboxes, everything is stored in the plain text Python
source files, so it's cleaner and very easy to put into version
control.

Conceptually, "Python tools" live inside "Python toolboxes" and that's
how they appear in Catalog. There can be many tools in one toolbox.

In practice, I break everything out into separate files,
so that's what I have done in this template.

This template just shows you how to set up a Python toolbox, it does nothing interesting on its own.

To use it, copy the repository as a functioning starting point, then add your own code. Github recognizes it as a template; just click their "Use this template" button.

Of course if you want, you could clone the template, make improvements, and send pull requests to me!

I use Visual Studio Code to develop and test Python. It's free and has excellent code completion ("Intellisense") and debugging. Therefore I have added the associated project files. 

### PYT files

You can add the .pyt extension to VS Code so that it treats them as python instead of text. 

Under File->Preferences->Settings->Files->Associations
I add *.pyt: python.

## Files

**python_toolbox.pyt** - This is the Python toolbox; it will show up in ArcCatalog as a toolbox.

**field_update_tool.py** - This is a class defining a tool. It acts as "glue" to connect the "business logic" in field_update_code.py to the toolbox.

**field_update_code.py** - This is a sample which updates a datestamp field in a feature class

**test_pro/** - contains an ArcGIS Pro project for unit testing and development.
Includes sample data.

The template Esri provides has all the code in one PYT file. This is okay for little tiny tools, in fact you can easily share a toolbox written this way because it's all in one file. With everything in one file though it's hard to debug and hard to maintain.

My intention is that once you set up the toolbox and tool files, you will seldom touch them. Minor errors in those sections can confuse Catalog, causing your entire toolbox to fail to load.

Keeping the toolbox code and the tool code in separate files also means you can very easily move tools from one toolbox to another. You just have to change one line in PYT files to add or remove a tool. 

Keeping the code doing the geoprocessing work in a separate file means it can be tested stand-alone in a debugger. You can hard code paths and settings in the unit test section and run the business logic by itself. It's much faster than trying to do everything through ArcGIS Pro, typing in the parameters in over and over.

There is a bug in both ArcGIS Pro and ArcCatalog; to get them to notice changes in the toolbox you have to reload them. This really slows down debugging. If you know a work around ("refresh" does not do it), please tell me. By contrast keeping business logic in separate files means you can update and save that file and then immediately re-run the tool in ArcMap or ArcCatalog.

## Unit Tests

There is a unit test in each python file. This means you can develop the code in that file independently, running it in a debugger and confirming it does what you expect before putting together all the pieces. 

So for example, you can start by testing field_update_code.py,
and once you are satisfied it runs, move on to field_update_tool.py,
and then finally run python_toolbox.pyt as a standalone script.

Of course, you could run each from a command line, but you can run it in 
Visual Studio Code and watch its operation in the debugger, executing
one line at a time.

## Visual Studio Code
### ArcGIS Pro set up

I followed some suggestions found [here, in GIS Stackexchange.](https://gis.stackexchange.com/questions/203380/setting-up-python-arcpy-with-arcgis-pro-and-visual-studio/356487#356487)

In ArcGIS Pro, clone the default Python environment. I renamed the clone arcgispro-py3-vscode. Then make the clone the default in ArcGIS Pro.
Use the cloned environment in Visual Studio Code, adding any additional packages
to the clone including autopep8.  

Another way is to start a clean new conda environment like this for example

   conda create -c esri -n arcgispro-vscode python=3.7.10 arcpy arcgis autopep8

### Selecting Python version

Set the version using Ctl-Shift-P Python: Select interpreter.
You should see the conda version created above listed.

## Resources

### Esri

2018 video: [Building Geoprocessing Tools With Python: Getting Started](https://www.youtube.com/watch?v=iTZytnBcagQ)

2019 slides for [Python: Beyond the Basics](https://proceedings.esri.com/library/userconf/devsummit19/papers/DevSummitPS_51.pdf) The current video link I found is [here](https://www.youtube.com/watch?v=y84onLbW-_M).

[Defining parameter data types in a python toolbox](https://desktop.arcgis.com/en/arcmap/latest/analyze/creating-tools/defining-parameter-data-types-in-a-python-toolbox.htm)

[Controlling the progress dialog box](https://desktop.arcgis.com/en/arcmap/latest/analyze/creating-tools/controlling-the-progress-dialog-box.htm)

