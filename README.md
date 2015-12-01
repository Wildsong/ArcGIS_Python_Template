# ArcGIS_Python_Template
Example of how to set up a Python Toolbox for ESRI ArcGIS

This project serves as a starting point when creating ArcGIS Python Tools.

In the ESRI world, "Python Tool" and "Python Toolbox" have specific
meanings.  They were added starting sometime around ArcGIS 10.0. 

Before that you could write scripts in Python for use in
ArcGIS. Interfacing a script to ArcGIS meant using ArcCatalog to
define what parameters the script takes and storing the definition in a proprietary binary file.
This approach is clumsy because keeping the ArcGIS binary file and the script in sync was awkward and prone to
breakage.

With Python Toolboxes, everything is stored in plain text Python source files, so it's clean and easy to put into version control.

Conceptually, "Python tools" live inside "Python toolboxes" and that's how they appear in ArcCatalog.
There can be many tools in one toolbox.

In practice, I break everything out into separate files so that's what I have done in this template.

This template does nothing on its own, it just shows you how to set up a Python toolbox.

To use the it, take a copy of the repository. Then add your own code.

If you want of course you can clone the template, make improvements, and send pull requests.

# TODO

Write unit test for sample_tool.py

# Files

sample.pyt - This is a toolbox.

sample_tool.py - This is a class defining a tool.

some_sample_code.py - This is the code that would actually do some work.

The template ESRI provides has all the code in one PYT file. This is okay for little tiny tools, in fact you can easily share 
a toolbox written this way because it's all in one file. But it's hard to debug and hard to maintain.

My intention is that you set up the toolbox and tool files and then seldom touch them.
Minor changes in those sections can confuse ArcCatalog, causing your entire toolbox to fail to load.

Keeping the toolbox code and the tool code in separate files means you can very easily move tools from one toolbox to another.
You just have to change one line in the PYT file to add or remove a tool. It also makes debugging easier.

Keeping the code actually doing the work in a separate file means it can be tested stand-alone in a debugger.
You can hard code paths and settings in the unit test section. 
It's much faster than trying to do everything through ESRI ArcCatalog typing parameters in over and over.

As far as I can tell, you have to quit and restart ArcCatalog to get it to notice changes, this really
slows down debugging too. If you know a work around ("refresh" does not do it), please tell me.

# Unit Tests

I try to put a unit test in each python file. This means you can develop the code in that file independently,
running it in a debugger and confirming it does what you expect before putting together all the pieces. 

You can run sample.pyt as a standalone script. It will pull in the tools and then list out what it knows about them.

I don't have a unit test in sample_tool.py yet.


