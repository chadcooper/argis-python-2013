# Reads a GPS-produced text file and writes the lat and long values
#  to an already-created polyline shapefile. Handles multiple polylines.
 
# Function to add a polyline
def addPolyline(cursor, array, sr):
    polyline = arcpy.Polyline(array, sr)
    cursor.insertRow((polyline,))
    array.removeAll()
 
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
 
# Create our InsertCursor
with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",)) as cursor:
    vertexArray = arcpy.Array()
 
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
