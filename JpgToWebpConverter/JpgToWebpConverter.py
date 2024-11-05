import os
import sys
from PIL import Image

def convert_images(directory, max_width_main=1024, max_width_thumb=200):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                # Convert to RGB (in case image is grayscale or CMYK)
                img = img.convert('RGB')

                # Resize for main webp image while keeping aspect ratio
                main_image = img.copy()
                main_image.thumbnail((max_width_main, max_width_main))
                webp_main_path = os.path.splitext(filepath)[0] + ".webp"
                main_image.save(webp_main_path, 'webp')
                print(f"Saved main image: {webp_main_path}")

                # Resize for thumbnail webp image while keeping aspect ratio
                thumbnail_image = img.copy()
                thumbnail_image.thumbnail((max_width_thumb, max_width_thumb))
                webp_thumb_path = os.path.splitext(filepath)[0] + "_thumb.webp"
                thumbnail_image.save(webp_thumb_path, 'webp')
                print(f"Saved thumbnail image: {webp_thumb_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_images.py <directory> [max_width_main] [max_width_thumb]")
        sys.exit(1)

    directory = sys.argv[1]
    max_width_main = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
    max_width_thumb = int(sys.argv[3]) if len(sys.argv) > 3 else 200

    convert_images(directory, max_width_main, max_width_thumb)

