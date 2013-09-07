import arcpy
import os

def parse_lat(in_lat):
    if in_lat:
        lat_deg = in_lat[0:2] 
        lat_min = in_lat[2:4]  
        lat_sec = in_lat[4:6] + "." + in_lat[6:8]  
        lat_dd = str(int(lat_deg)+(float(lat_min)/60)+(float(lat_sec)/3600))
        return float(lat_dd)

def parse_lon(in_lon):
    if in_lon:
        lonDeg = in_lon[0:3]
        lonMin = in_lon[3:5] 
        lonSec = in_lon[5:7] + "." + in_lon[7:9]  
        lonDD = str('-'+str(int(lonDeg)+(float(lonMin)/60)+float(lonSec)/3600))
        return float(lonDD)

try: 
    proj_dir = r"C:\Users\class5user\ar-gis-python"
    input_file = open(os.path.join(proj_dir, "outputs", "dc.csv"), "r")

    # Figure out position of lat and long in the header
    header = input_file.readline()
    value_list = header.split(",")
     
    lat_index = value_list.index("LAT_016")
    lon_index = value_list.index("LONG_017")
    structure_index = value_list.index("STRUCTURE_NUMBER_008")
     
    # Read lines in the file and append to coordinate list
    coords = []
     
    for line in input_file.readlines():
        segmented_line = line.split(",")
        lat = parse_lat(segmented_line[lat_index])
        lon = parse_lon(segmented_line[lon_index])
        coords.append([segmented_line[structure_index],
                       lon,
                       lat])

    fc = os.path.join(proj_dir, "inputs", "shapefiles", "dc-bridges.shp")
    for coord_pair in coords:
        if coord_pair[1]:
            print coord_pair
            cursor = arcpy.da.InsertCursor(fc, ["SHAPE@XY"])
            xy = (coord_pair[1], coord_pair[2])
            cursor.insertRow([xy])
except Exception as e:
   print e.message
finally:
    # Cleanup the cursor if necessary
    #
    if cursor:
        del cursor
