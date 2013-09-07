Working with point geometries
=============================

Building a point featureclass from NBI CSV files
------------------------------------------------

Adding more data from the text file
+++++++++++++++++++++++++++++++++++

Lets add some data to our nested list we are pulling from our Rhode Island 
bridges file.

Copy/paste ``parse-csv.py`` in your ``code`` directory, rename it to 
``csv-to-features.py``. Open it up in IDLE. Add in the highlighted lines below. 
Make sure your tabs are correct (4 spaces). 

.. literalinclude:: /embeds/parse-csv-with-strx-no.py
   :emphasize-lines: 1-4, 12, 19-21, 23-24
              
Run your code, you should now get the bridge ID as well as lat and lon:

.. code-block:: python

   ['000000000010800', '071245227', '41485835']
   ['000000000010800', '071245227', '41485835']
   ['000000000010800', '071245227', '41485835']
   ['000000000010810', '071240664', '41485525']
   ['000000000010810', '071240664', '41485525']
   ...
   
Pushing the text data to a featureclass
+++++++++++++++++++++++++++++++++++++++

Check out the shapefile ``inputs\shapefiles\ri-bridges.shp`` in ArcCatalog. 
Pretty basic with Lat, Lon, and StrxNo fields. Let's push the text data into 
this shapefile. The new code will parse out the DMS data to decimal degrees and 
using a ``arcpy.da.InsertCursor``, add each row of bridge data into the 
shapefile as a point feature [Ref]_:

.. note:: 

   `The Recording and Coding Guide for the Structure Inventory and Appraisal 
   of the Nations Bridges`_ document on the NBI site explains all codes used in 
   these datasets.
   
By reading the docs on these datasets, we know that latitude is recorded as:

``XX degrees XX minutes XX.XX seconds``

...and longitude as:

``XXX degrees XX minutes XX.XX seconds``

Let's put in two functions to get those DMS readings to decimal degrees, using 
some simple math. Insert these below your ``import`` statements:

.. code-block:: python

   def parse_lat(in_lat):
       if in_lat:
           lat_deg = in_lat[0:2] 
           lat_min = in_lat[2:4]  
           lat_sec = in_lat[4:6] + "." + in_lat[6:8]  
           lat_dd = str(int(lat_deg)+(float(lat_min)/60)+(float(lat_sec)/3600))
           return float(lat_dd)

   def parse_lon(in_lon):
       if in_lon:
           lon_deg = in_lon[0:3]
           lon_min = in_lon[3:5] 
           lon_sec = in_lon[5:7] + "." + in_lon[7:9]  
           lon_dd = str('-'+str(int(lon_deg)+(float(lon_min)/60)+float(lon_sec)/3600))
           return float(lon_dd)
           
Now that we have our functions, we have to call them and feed data into them. 
Change the section where we read our lines and put them into the ``coords`` 
object to:

.. code-block:: python

   coords = []
   for line in input_file.readlines():
       segmented_line = line.split(",")
       lat = parse_lat(segmented_line[lat_index])
       lon = parse_lon(segmented_line[lon_index])
       coords.append([segmented_line[structure_index],
                      lon,
                      lat])
                      
Next, change these lines:

.. code-block:: python

   for coord_pair in coords:
      if coord_pair[1]:
          print coord_pair
          
To this:

.. code-block:: python

   fc = os.path.join(proj_dir, "inputs", "shapefiles", "ri-bridges.shp")
   for coord_pair in coords:
       if coord_pair[1]:
           print coord_pair[0]
           row_values = (coord_pair[0].strip(),
                         coord_pair[2],
                         coord_pair[1],
                         (coord_pair[1], coord_pair[2]))
           cursor = arcpy.da.InsertCursor(fc, ("StrxNo",
                                               "Lat",
                                               "Lon",
                                               "SHAPE@XY"))
           cursor.insertRow(row_values)

Finally, let's wrap up our code in a ``try/except/finally`` block. Select 
everything from this line:

.. code-block:: python

   proj_dir = r"C:\Users\class5user\ar-gis-python"

to this line:

.. code-block:: python

   cursor.insertRow(row_values)   

With it all selected, tab it in one tab stop. Add the ``try/except/finally`` so 
it looks like so:

.. code-block:: python

   try: 
       proj_dir = r"C:\Users\class5user\ar-gis-python"
       input_file = open(os.path.join(proj_dir, "outputs", "RI12.txt"), "r")
       ...
       ...
       ...
               cursor = arcpy.da.InsertCursor(fc, ("StrxNo",
                                                   "Lat",
                                                   "Lon",
                                                   "SHAPE@XY"))
               cursor.insertRow(row_values)
   except Exception as e:
      print e.message
   finally:
       # Cleanup the cursor if necessary
       if cursor:
           del cursor
           
Save and run your code in IDLE. Go into ArcCatalog and preview your dataset and look at 
the attribute table. Does it have data in it?

We can also run this script from the Windows command line. Open up a command 
prompt and navigate to the ``code`` directory:

.. code-block:: bash

   C:\Users\class5user>cd code
   
Now execute the script:

.. code-block:: bash

   C:\Users\class5user\code>python csv-to-features.py
   
Bonus
+++++

How would we add a field to record the date/time that each record is inserted 
into the featureclass?

Hints
@@@@@

* It only takes 3 lines of code
* You'll need to import a module
* The majority of the work is in the last ``if`` loop
* Does the output featureclass need anything added to it?

.. [Ref] This section adapted from the PSU Geog 485 course at 
   https://www.e-education.psu.edu/geog485/node/142  

.. rst-class:: html-toggle

Solution
--------
    
.. literalinclude:: /embeds/csv-to-features.py



.. _The Recording and Coding Guide for the Structure Inventory and Appraisal 
   of the Nations Bridges: http://www.fhwa.dot.gov/bridge/mtguide.pdf