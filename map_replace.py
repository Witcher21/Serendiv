import re

filepath = 'e:/Projects/Serendiv/src/components/IslandMap.vue'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Read map output
with open('map_output.txt', 'r', encoding='utf-8') as f:
    map_data = f.read()

svg_path = re.search(r'=== SVG PATH ===\n(M .*?Z)', map_data, re.DOTALL).group(1)

# Pins data
pins = {}
for line in map_data.split('=== PINS ===')[-1].strip().split('\n'):
    match = re.search(r"id: '([^']+)', x: ([\d.]+), y: ([\d.]+)", line)
    if match:
        pins[match.group(1)] = (match.group(2), match.group(3))

# Replace SVG path
old_path = r'd="M 233 46 C 242 35 C 242 35[A-Za-z0-9, \n]+?Z"'
new_path = f'd="{svg_path}"'
# using a more generic regex for the path
content = re.sub(r'd="M 233 46 .*?Z"', new_path, content, flags=re.DOTALL)

# Replace pin coordinates
for pin_id, (x, y) in pins.items():
    # Replace x
    content = re.sub(fr"id:\s*'{pin_id}',\s*(?:name.*?\n\s*)?x:\s*[\d.]+,\s*y:\s*[\d.]+", 
                     lambda m: m.group(0).replace(re.search(r'x:\s*[\d.]+', m.group(0)).group(0), f"x: {x}").replace(re.search(r'y:\s*[\d.]+', m.group(0)).group(0), f"y: {y}"), 
                     content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Replaced successfully')
