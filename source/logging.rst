Using logging in your scripts
=============================

Logging is the act of taking messages which generated in your script and writing 
them out to a file. Log files typically are just plain text files with a ``.log`` 
file extension. Logging is easy and painless and can help you find errors and 
bottlenecks in your scripts.

Logging with the ``logging`` module
-----------------------------------

The Python standard library comes with the ``logging`` module. There are 5 
standard logging levels:

* DEBUG: detailed, for troubleshooting
* INFO: normal operation, statuses
* WARNING: still working, but unexpected behavior
* ERROR: more serious, some functions not working
* CRITICAL: program cannot continue

A simple example. Put this in a script file in your ``scripts`` directory, run 
it in IDLE, and see if you get a log file in the same directory.

.. code-block:: python

   import logging
   logging.basicConfig(filename="log_example.log",level=logging.DEBUG)
   logging.debug("This message should go to the log file")
   logging.info("So should this")
   logging.warning("And this, too")

Let's go all in with this last example, which logs errors and timestamps out:

.. code-block:: python

   import arcpy
   import sys
   import traceback
   import logging
   import datetime

   log_file = "meaningful_log_%s.log" % datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

   arcpy.env.workspace = r"C:\Student\Code\test.gdb"

   # Setup logger
   logging.basicConfig(level=logging.DEBUG,
                       format='%(asctime)s %(levelname)-8s %(message)s',
                       datefmt='%Y-%m-%d %H:%M:%S',
                       filename=log_file,
                       filemode='w')
   logging.info(': START LOGGING')

   try:
       # Your code goes here
       float("lfkjdlk")

       logging.info(": DONE")

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
           logging.error(": %s" % msgs)
       # Log Python error messages for use in Python / Python Window
       logging.error(": %s" % pymsg + "\n")
