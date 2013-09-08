Error handling
==============

If you set it up from the beginning, it will make things much easier when 
testing your code.

Simple error handling
---------------------

The basics of error handling are this:

.. code-block:: python

   try:
       do something...
   except:
       handle error...
   finally:
       clean up...

In the ArcMap Python prompt, type this:

.. code-block:: python

   arcpy.Buffer_analysis("Observer")
   
And you'll get something messy like:

.. code-block:: python

   Runtime error  Traceback (most recent call last):   File "<string>", 
   line 1, in <module>   File "c:\program files (x86)\arcgis\desktop10.1\arcpy\
   arcpy\analysis.py", line 687, in Buffer     raise e ExecuteError: ERROR 
   000732: Input Features: Dataset Observer does not exist or is not supported 
   ERROR 000735: Distance [value or field]: Value is required 
   
Now try this:

.. code-block:: python

   try:
       arcpy.Buffer_analysis("Observer")
   except Exception as e:
       print e.message
   
And you get:

.. code-block:: python

   ERROR 000732: Input Features: Dataset Observer does not exist or is not supported
   ERROR 000735: Distance [value or field]: Value is required

   
Cleaning up with ``try/except/finally``
---------------------------------------  

Sometimes you want to clean up when something goes south, the ``finally`` 
clause lets you do that:

.. code-block:: python

   try:
       if arcpy.CheckExtension("3D") == "Available":
           arcpy.CheckOutExtension("3D")
           arcpy.Slope_3d("Magic.gdb/NWA10mNED", "Magic.gdb/SlopeNWA")
   except Exception as e:
       print e.message
       print arcpy.GetMessages(2)
   finally:
       # Check in the 3D Analyst extension
       arcpy.CheckInExtension("3D") 
       
And you get:

.. code-block:: python
   
   ERROR 000865: Input raster: Magic.gdb/NWA10mNED does not exist.
   
.. note:: 

   Using ``finally`` also works well for closing database connections.
   
Getting stack info with ``traceback``
-------------------------------------

The ``traceback`` module provides a standard interface to extract, format and 
print stack traces of Python programs. It exactly mimics the behavior of the 
Python interpreter when it prints a stack trace. Basically, it gives you the 
most info you can get related to your error(s):

Paste this into a IDLE script and run it:

.. code-block:: python

   import sys
   import traceback

   try:
       # Your code goes here
       float("a string")
   except:
       # Get the traceback object
       tb = sys.exc_info()[2]
       tbinfo = traceback.format_tb(tb)[0]
       # Concatenate information together concerning the error into a message string
       #   tbinfo: where error occurred
       #   sys.exc_info: 3-tuple of type, value, traceback
       pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
       msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
       # Return python error messages for use in script tool or Python Window
       arcpy.AddError(pymsg)
       if arcpy.GetMessages(2):
           arcpy.AddError(msgs)
           print msgs
       # Print Python error messages for use in Python / Python Window
       print pymsg + "\n"
       
This tells you **exactly** where your error is occurring:

.. code-block:: python

   >>> 
   PYTHON ERRORS:
   Traceback info:
     File "C:/Users/class5user/ar-gis-python/crap.py", line 7, in <module>
       float("a string")

   Error Info:
   could not convert string to float: a string

   >>>