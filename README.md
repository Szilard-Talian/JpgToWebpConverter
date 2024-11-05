# JPG to WebP Converter

This Python script converts all `.jpg` images in a given directory to `.webp` format. The conversion includes two versions of each image: a main image and a thumbnail. The script resizes the images to maintain their aspect ratio, with customizable maximum widths.

## Features
- Converts all `.jpg` images in the specified directory to `.webp` format.
- Generates two versions of each image:
  - **Main Image**: Resized to a maximum width (default: 1024 pixels).
  - **Thumbnail Image**: Resized to a smaller maximum width (default: 200 pixels).
- Maintains the original aspect ratio of images during resizing.

## Requirements
- Python 3.x
- Pillow library

Install the required library with:
```sh
pip install Pillow
```

## Usage
To run the script, use the following command:
```sh
python convert_images.py <directory> [max_width_main] [max_width_thumb]
```

### Parameters
- `<directory>`: The path to the directory containing the `.jpg` images to be converted.
- `[max_width_main]` (optional): The maximum width for the main images (default is 1024 pixels).
- `[max_width_thumb]` (optional): The maximum width for the thumbnail images (default is 200 pixels).

### Example
```sh
python convert_images.py ./images 800 400
```
This command converts all `.jpg` images in the `./images` directory to `.webp` format, with the main images resized to a maximum width of 800 pixels and the thumbnails to a maximum width of 400 pixels.

## Notes
- The converted images will be saved in the same directory as the original `.jpg` files.
- Each converted image will have the `.webp` extension, and the thumbnails will have `_thumb` appended to the filename.

## License
This project is open-source and available under the MIT License.

