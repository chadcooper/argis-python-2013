# Reads a NBI bridge data text file and writes the lat and long values
#  to a list of coordinates
input_file = open(r"C:\Users\class5user\ar-gis-python\outputs\dc.csv", "r")
 
# Figure out position of lat and long in the header
header = input_file.readline()
value_list = header.split(",")
 
lat_index = value_list.index("LAT_016")
lon_index = value_list.index("LONG_017")
 
# Read lines in the file and append to coordinate list
coords = []
 
for line in input_file.readlines():
    segmented_line = line.split(",")
    coords.append([segmented_line[lon_index], segmented_line[lat_index]])

for coord_pair in coords:
    print coord_pair
