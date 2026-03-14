import urllib.request
import json

url = 'https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    for feature in data['features']:
        if 'Sri Lanka' in str(feature['properties']):
            geom = feature['geometry']
            break

lanka_coords = []
if geom['type'] == 'Polygon':
    lanka_coords = geom['coordinates'][0]
elif geom['type'] == 'MultiPolygon':
    # find largest polygon
    lanka_coords = max(geom['coordinates'], key=lambda x: len(x[0]))[0]

# Find bounding box
min_x, max_x = min([c[0] for c in lanka_coords]), max([c[0] for c in lanka_coords])
min_y, max_y = min([c[1] for c in lanka_coords]), max([c[1] for c in lanka_coords])

width = max_x - min_x
height = max_y - min_y

scale_x = 420 / width
scale_y = 720 / height
scale = min(scale_x, scale_y)

offset_x = (500 - (width * scale)) / 2
offset_y = (800 - (height * scale)) / 2

def to_svg(lng, lat):
    x = (lng - min_x) * scale + offset_x
    y = 800 - ((lat - min_y) * scale + offset_y)
    return x, y

path_d = 'M '
for i, c in enumerate(lanka_coords):
    x, y = to_svg(c[0], c[1])
    if i == 0:
        path_d += f'{x:.1f},{y:.1f} L '
    else:
        path_d += f'{x:.1f},{y:.1f} '
path_d += 'Z'

with open('map_output.txt', 'w') as f:
    f.write('=== SVG PATH ===\n')
    f.write(path_d + '\n')

    pins = {
        'sigiriya': (80.7603, 7.9570),
        'kandy': (80.6337, 7.2906),
        'ella': (81.0485, 6.8718),
        'yala': (81.4247, 6.3773),
        'galle': (80.2210, 6.0535),
        'mirissa': (80.4533, 5.9483),
        'trincomalee': (81.2152, 8.5874),
    }

    f.write('\n=== PINS ===\n')
    for key, (lng, lat) in pins.items():
        x, y = to_svg(lng, lat)
        f.write(f"    id: '{key}', x: {x:.1f}, y: {y:.1f}\n")
