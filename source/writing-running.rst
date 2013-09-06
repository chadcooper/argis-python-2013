Writing code and running scripts
================================

We'll be working at the command line some today, both the Windows command line 
and the ArcGIS Python command line. Let's get some basic commands out of the 
way.

Windows Command Prompt
----------------------

Configuration
+++++++++++++

To launch the Windows Command Prompt, click on Start and in the search box, type 
``cmd``, then hit Enter. You should see somthing like this:

.. image:: /images/cmd.png
   :width: 500px
   
Now type ``python``. Do you get an error?

.. image:: /images/cmd-python-not-found.png
   :width: 500px
   
If you did get this error (and you should have), it's because Windows has no 
idea where your Python 
executable is located. ArcGIS 10.1 installs Python to ``C:\Python27\ArcGIS10.1``, 
but for *some reason* unknown to me, the ArcGIS installer does not set the 
proper paths into your ``PATH`` environmental variable. You will inevitably have 
to do this sooner or later on a PC, so let's do it now. Examine your current 
``PATH`` variable:

.. code-block:: bash

   C:\Users\class5user>echo %PATH%
   
You should get a semi-colon separated list of paths to various programs and folders. 
We need to add a few of our own paths there as well. Copy the following ``set`` 
command and paste it into the command window (to paste, simply place your cursor 
in the command prompt and right click):

.. code-block:: bash

   C:\Users\class5user>set PATH=%PATH%;C:\Python27\ArcGIS10.1;C:\Python27\ArcGIS10.1\Lib\site-packages;C:\Python27\ArcGIS10.1\Scripts
   
Check your ``PATH`` now:

.. code-block:: bash

   C:\Users\class5user>echo %PATH%
   
Now type ``python`` again, and you should see this:

.. code-block:: bash
   
   C:\Users\class5user>python
   Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win 32
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   
You are now at the Python interactive prompt. Press ``ctrl + z`` ``enter`` to 
exit the Python interpreter.

Working at the Python prompt
++++++++++++++++++++++++++++

For short one-off jobs and quick code snippet tests, sometimes it's easier to 
just whip up some code at the command line, like so:

.. code-block:: bash

   >>> import arcpy
   >>> arcpy.env.workspace = r"C:\Users\class5user\gp\KittyHawk.gdb"
   >>> l
   [u'KittyHawk_PCS', u'KittyHawk_SlopedShore', u'KittyHawk', u'KittyHawk_HavDist',
    u'KittyHawk_HavCurvedGCS', u'KittyHawk_HavCurvedPCS']
   >>> f = arcpy.ListFeatureClasses()
   >>> f
   [u'KittyHawk_RasterToPoints', u'KOP_Template', u'WTG_Template', u'FOV_Template',
    u'KOP_FOV', u'KOPs', u'WTGs']
   >>>
   
Or:

.. code-block:: bash

   >>> [i**2 for i in range(11)]
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
   >>>
   
You can also run a Python script from the command line:

.. code-block:: bash

   C:\Users\class5user\gp>cd Scripts
   C:\Users\class5user\gp\Scripts>dir
   C:\Users\class5user\gp\Scripts>python run-me.py
   
Which returns:

.. code-block:: bash

   C:\Users\class5user\gp\Scripts\run-me.py
   
Working at the ArcGIS Python prompt
+++++++++++++++++++++++++++++++++++
   
ArcGIS also has a built-in Python interpreter with the big added bonus of code-
completion! Launch ArcMap and open the Python window:

.. image:: /images/open-arcgis-python.png
   :width: 500px
   
.. warning::

   **WAIT!** Let's talk about the ArcGIS online Python `help`_.
   
Import arcpy like you did earlier:

.. code-block:: bash

   >>> import arcpy

Add the following datasets from the KittyHawk file geodatabase at 
``C:\Users\class5user\gp`` (you might want to add a folder connection now to 
save from hunting for the GDB later).

* KOPs
* WTGs
* KOP_FOV
* KittyHawk_HavCurvedPCS

Get a ``Describe`` object on the KOPs featureclass:

.. code:: python

   >>> desc = arcpy.Describe("KOPs")
   >>> desc
   <geoprocessing describe data object object at 0x19C9CC38>
   >>> print desc.catalogPath
   C:\Users\class5user\gp\KittyHawk.gdb\KOPs
   >>> print desc
   <geoprocessing describe data object object at 0x19C9CC38>
   >>> 
   >>> 
   >>> print desc.path
   C:\Users\class5user\gp\KittyHawk.gdb
   >>> print desc.dataType
   FeatureLayer
   >>>
   >>>
   >>>
   >>> fields = arcpy.ListFields('KOPs')
   >>> for field in fields:
   ...     print field.name
   ...     
   OBJECTID
   Shape
   Id
   VIESORE_KOP_ID
   VIESORE_KOP_Name
   VIESORE_Elev_Meters
   VIESORE_Height_Above_Ground
   VIESORE_Timezone
   VIESORE_Ground_Elevation
   >>>
   
You can also execute larger blocks of code and functions. Copy/paste the entire 
function below into the ArcMap Python window:
   
.. code:: python   
   
   def get_raster_props(in_raster):   
       """Get properties of a raster, return as dict"""
       r = arcpy.Raster(in_raster)
       raster_props = {}
       x_center = r.extent.XMin + (r.extent.XMax - r.extent.XMin)/2
       y_center = r.extent.YMin + (r.extent.YMax - r.extent.YMin)/2
       raster_props["XCenter"] = x_center
       raster_props["YCenter"] = y_center
       raster_props["MaxElevation"] = r.maximum
       raster_props["MinElevation"] = r.minimum
       raster_props["NoData"] = r.noDataValue
       raster_props["TerrainWidth"] = r.width
       raster_props["TerrainHeight"] = r.height
       raster_props["TerrainCellResolution"] = r.meanCellHeight
       raster_props["Extent"] = [r.extent.XMin, r.extent.YMin, r.extent.XMax, r.extent.YMax]
       return raster_props
   
Let's see what that gets us:

.. code:: python 

   >>> d = get_raster_props('KittyHawk_HavCurvedPCS')
   >>> d
   {'MaxElevation': 128.38812255859375, 'XCenter': 0.32068791591780155, 'MinElevation': -0.11725148558616638, 'TerrainWidth': 583L, 'Extent': [-900.4526850421192, -848.1423855915971, 901.0940608739548, 845.2497529367195], 'NoData': None, 'TerrainCellResolution': 3.0901316396502128, 'YCenter': -1.446316327438808, 'TerrainHeight': 548L}
   
   
What type of Python built in object is ``d``?

.. code:: python 

   >>> type(d)
   
Print out the contents of ``d``:
   
.. code:: python 

   >>> for k, v in d.iteritems():
   ...     print k, "-->", v
   ...     
   MaxElevation --> 128.388122559
   XCenter --> 0.320687915918
   MinElevation --> -0.117251485586
   TerrainWidth --> 583
   Extent --> [-900.4526850421192, -848.1423855915971, 901.0940608739548, 845.2497529367195]
   NoData --> None
   TerrainCellResolution --> 3.09013163965
   YCenter --> -1.44631632744
   TerrainHeight --> 548
   >>>

.. note::

   You can also customize the look and feel of the ArcGIS Python window pretty 
   easily.

Writing and editing scripts
+++++++++++++++++++++++++++

To compose and edit our scripts, we are going to use IDLE, a Python IDE that ships 
with the ArcGIS install of Python. To access IDLE, got to Start | All Programs | 
ArcGIS | Python 2.7 | IDLE. You will get the IDLE interactive interpreter, which 
is not unlike the two Python interpreters we have already used:

.. image:: /images/idle.png
   :width: 500px
   
To write a script, go to File | New Window, and you will be presented with a 
Notepad-like editor. 

You can also edit a existing script by right-clicking on it in Windows Explorer 
and selecting "Edit with IDLE".

To run a script in IDLE, go to Run | Run File, or hit F5.

Modules
-------

Let's take a few minutes and discuss modules, where they live, and what some 
look like.


.. _help: http://resources.arcgis.com/en/help/main/10.1/
   