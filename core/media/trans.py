from pathlib import Path
from PIL import Image
import PIL

def convert_to_webp(source):
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    base_width = 600
    width_percent = (base_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(width_percent)))
    image = image.resize((base_width, hsize), PIL.Image.ANTIALIAS)
    image.save(destination, format="webp", optimize=True, quality=70)  # Convert image to webp

    return destination

def main():
    paths = Path("elegidasproductos").glob("**/*.jpg")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)

main()