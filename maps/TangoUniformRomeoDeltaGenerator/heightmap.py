from PIL import Image
import numpy as np

# Full BAR heightmap size
size = 4097

# Initialize heightmap array
heightmap = np.zeros((size, size), dtype=np.uint8)

# Helper functions
def plateau(x0, y0, w, h, height):
    heightmap[y0:y0+h, x0:x0+w] = height

def ramp(x0, y0, w, h, start_h, end_h):
    for i in range(h):
        heightmap[y0+i, x0:x0+w] = np.linspace(start_h, end_h, w, dtype=np.uint8)

# Heights
valley_height = 80
plateau_height = 200
geo_height = 220

# Start clusters (top-left corner)
plateau(200, 200, 600, 600, plateau_height)
plateau(1000, 200, 600, 600, plateau_height)
plateau(600, 800, 600, 600, plateau_height)

# Start clusters (bottom-right corner)
plateau(size-800, size-800, 600, 600, plateau_height)
plateau(size-1400, size-800, 600, 600, plateau_height)
plateau(size-1000, size-1400, 600, 600, plateau_height)

# Raised geothermals
plateau(size-800, 200, 600, 600, geo_height)   # top-right corner
plateau(200, size-800, 600, 600, geo_height)   # bottom-left corner

# Snaking valley (diagonal from geo to geo)
for i in range(size):
    x = i
    y = int(size/2 + 200*np.sin(i/200))  # smooth snaking
    heightmap[y-10:y+10, x] = valley_height

# Optional: add slight smoothing (simple blur)
from scipy.ndimage import gaussian_filter
heightmap = gaussian_filter(heightmap, sigma=3)

# Save PNG
img = Image.fromarray(heightmap)
img.save("heightmap_full.png")
print("Full-resolution heightmap saved as 'heightmap_full.png'")
