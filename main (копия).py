import geopandas as gpd
from shapely.geometry import Polygon, LineString, Point, MultiPolygon, box, MultiLineString
import os
import re
import matplotlib.pyplot as plt
files = os.listdir('F:\PycharmProjects\g-код')
options = []
for f in files:
    if f.endswith(".nc") or f.endswith('.NC'):
        options.append(f)
gcode_file = ''
while not gcode_file:
    for i, option in enumerate(options):
        print("{} - {}".format(i, option))
    selected = input("select file: ")
    try:
        gcode_file = options[int(selected)]
    except:
        print("please input a number.")
with open(gcode_file) as file:
    gcode = file.read()
#gcode = list(gcode.split('*'))
figures = re.findall(r"M15.{,14}M14.*?M15|M14.*?M15", gcode)
figure_list = []
for figure in figures:
    coordinates = re.findall(r"X\d*Y\d*", figure)
    parts = []
    for coordinate in coordinates:
        coords = re.findall(r"\d*[^\D]", coordinate)
        g =[]
        for coord in coords:
            f = int(coord)
            g.append(f)
        parts.append(g)
    figure_list.append(LineString(parts))
multiline = MultiLineString(figure_list)
#total_space = box(multiline.bounds)
bite_length = 6000
#print(multiline.exterior.coords)
intersection_line = gpd.GeoSeries(LineString([(bite_length, multiline.bounds[1]),
                                              (bite_length, multiline.bounds[3])]))
#print(multiline.bounds)
bite_box = box(multiline.bounds[0],
               multiline.bounds[1],
               bite_length,
               multiline.bounds[3])
#print(bite_box)
figures_in_bite = []
figures_outside_bite = []
for figure in figure_list:
    if figure.covered_by(bite_box) == True:
        figures_in_bite.append(figure)
    else:
        figures_outside_bite.append(figure)
#print(figures_outside_bite)
g = gpd.GeoSeries(figures_in_bite)
byte_line = intersection_line.plot('Greens_r')
g.plot(ax=byte_line, color='gray')
plt.show()
#    for coord in figure:
#        coord.split('Y')
#lines = shapely.geometry.MultiLineString(figure_list)
#print(lines)
#plt.plot(figure_list)
#with open('new_' + gcode_file, 'w') as result:
#    for line in gcode:
#        result.write(line + '\n')



