from PIL import Image, ImageDraw
import numpy as np

# Map size
size = 4097

# Initialize metal map (black = no metal)
metal = Image.new("L", (size, size), 0)
draw = ImageDraw.Draw(metal)

# Function to draw a metal node
def metal_node(x, y, radius=20):
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=255)

# Player start nodes (2 per start)
# Top-left corner starts
metal_node(500, 500)
metal_node(650, 500)
metal_node(1100, 500)
metal_node(1250, 500)
metal_node(800, 900)
metal_node(950, 900)

# Bottom-right corner starts
metal_node(size-500, size-500)
metal_node(size-650, size-500)
metal_node(size-1100, size-500)
metal_node(size-1250, size-500)
metal_node(size-800, size-900)
metal_node(size-950, size-900)

# Mid-valley nodes along valley (from top-right geo to bottom-left geo)
# Using simple diagonal for illustration
valley_start_x, valley_start_y = size-800, 200       # top-right geo
valley_end_x, valley_end_y = 200, size-800           # bottom-left geo

# 6 nodes evenly spaced along the valley
for i in range(5):
    t = i / 5  # fraction along the line
    x = int(valley_start_x * (1 - t) + valley_end_x * t)
    y = int(valley_start_y * (1 - t) + valley_end_y * t)
    # Place nodes slightly offset left/right of valley center
    metal_node(x+100, y+500)

# Save metal map
metal.save("metal_valley_path.png")
print("Metal map saved as 'metal_valley_path.png'")
