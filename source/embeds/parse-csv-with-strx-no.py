import os

proj_dir = r"C:\Users\class5user\ar-gis-python"
input_file = open(os.path.join(proj_dir, "outputs", "RI12.txt"), "r")

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
   coords.append([segmented_line[structure_index],
                  segmented_line[lon_index],
                  segmented_line[lat_index]])
for coord_pair in coords:
   if coord_pair[1]:
       print coord_pair
