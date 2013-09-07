Working with line geometries
============================

Building lines from a GPX track file
------------------------------------

Creating points is relatively simple. Polylines and polygons are a little more 
involved. Polylines and polygons are composed of array objects that *contain* 
point objects. For example [Ref]_:

.. code-block:: python

   # Make a new empty array
   array = arcpy.Array()
 
   # Make some points
   point1 = arcpy.Point(-121.34,47.1)
   point2 = arcpy.Point(-121.29,47.32)
   point3 = arcpy.Point(-121.31,47.02)
 
   # Put the points in the array
   array.add(point1)
   array.add(point2)
   array.add(point3)
 
   # Make a polyline out of the now-complete array
   polyline = arcpy.Polyline(array, spatialRef)
 
   # Put the polyline in the feature class
   newRow.shape = polyline
   
The file we will use is a text file of GPS tracks, a GPX file. It's layout is 
very similar to the NBI bridges file - comma-separated values with a header. 
Therefore, some of our code to read in the file will be very similar.

Create a script called ``build-polylines.py`` in your ``code`` directory and open 
it in IDLE. Enter the following code, which should look very familiar:

.. code-block:: python

   # Main script body
   import arcpy
 
   # Hard-coded variables for GPS track text file and feature class
   gpsTrack = open(r"C:\Users\class5user\ar-gis-python\inputs\gps-track.txt", "r")
   polylineFC = r"C:\Users\class5user\ar-gis-python\inputs\shapefiles\gpx-tracks.shp"
   spatialRef = arcpy.SpatialReference("WGS 1984")
 
   # Figure out position of lat and long in the header
   headerLine = gpsTrack.readline()
   valueList = headerLine.split(",")
 
   latValueIndex = valueList.index("lat")
   lonValueIndex = valueList.index("long")
   newTrackIndex = valueList.index("new_seg")
   
Next, create the ``InsertCursor``:

.. code-block:: python

   # Create our InsertCursor
   with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",)) as cursor:
       vertexArray = arcpy.Array()
       
Finally, the important parts. Loop through the GPX tracks and write them to
the featureclass:

.. code-block:: python

   # Read each line and split it
   for line in gpsTrack.readlines():
      segmentedLine = line.split(",")
      isNew = segmentedLine[newTrackIndex].upper()
 
      # If starting a new line, write the completed
      #  line to the feature class
      if isNew == "TRUE":
 
          # This check is needed to handle the first GPS entry
          if vertexArray.count > 0:
              addPolyline(cursor, vertexArray, spatialRef)
 
      # Get the lat/lon values of the current GPS reading
      latValue = segmentedLine[latValueIndex]
      lonValue = segmentedLine[lonValueIndex]
 
      vertex = arcpy.Point(lonValue, latValue)
      vertexArray.add(vertex)
 
   # Add the final polyline to the shapefile
   addPolyline(cursor, vertexArray, spatialRef)       
   
Wait, something is missing, what is that ``addPolyline()`` call? This is what 
actually inserts the polyline into the featureclass. Add it below your 
``arcpy`` import statement:

.. code-block:: python

   # Function to add a polyline
   def addPolyline(cursor, array, sr):
       polyline = arcpy.Polyline(array, sr)
       cursor.insertRow((polyline,))
       array.removeAll()
       
Save your script and run it in IDLE. Check your results in ArcCatalog. 

.. rst-class:: html-toggle

Solution
--------
    
.. literalinclude:: /embeds/build-polylines.py

Questions
---------

1. How many records are in the featureclass, and why? 
2. How do the number of records in the featureclass compare to the number of 
   records in the GPX file?
   


.. [Ref] This section adapted from the PSU Geog 485 course at 
   https://www.e-education.psu.edu/geog485/node/142