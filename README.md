# GIF Creation Script

This script uses the `imageio` library to create an animated GIF from a set of images. It reads a list of image files, combines them into a GIF, and saves it to disk. The GIF is configured with specific frame durations and loop settings.

## Features

- Converts a sequence of images into an animated GIF.
- Configures frame duration and loop behavior.
- Simple and easy-to-use image-to-GIF conversion.

## Requirements

- Python 3.x
- `imageio` library (install via `pip install imageio`)

## How to Run

1. Install `imageio` if not already installed:

    ```bash
    pip install imageio
    ```

2. Clone or download the repository.
3. Update the `filenames` list in the script with the paths to your images.
4. Run the script:

    ```bash
    python create_gif.py
    ```

   This will create a GIF named `image.gif` from the listed images.

## Code Explanation

### `filenames`
The script first defines a list of image file paths (`filenames`) to be used for the GIF creation.

### `images = [iio.imread(filename) for filename in filenames]`
It reads the images using the `imageio.imread()` function, storing them in a list.

### `iio.mimsave('image.gif', images, duration=0.5, loop=0)`
This function saves the images as a GIF:
- **`duration=0.5`**: Each frame is displayed for 0.5 seconds.
- **`loop=0`**: The GIF will play once and stop.

## Contributing

Feel free to submit issues or pull requests for improvements.
