import zipfile
import os

# Folder containing map files
folder = "../TangoUniformRomeoDelta"
sdz_filename = "../TangoUniformRomeoDelta.sdz"

with zipfile.ZipFile(sdz_filename, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            # Add file preserving relative path
            z.write(file_path, arcname=file)

print(f"Map packaged as '{sdz_filename}'! Drop this into your BAR maps folder.")