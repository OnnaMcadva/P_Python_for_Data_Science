from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.array:
    """
    Load an image from the given path, print its format, and return
    the pixel data as an RGB NumPy array.

    Notes:
        - Full support is guaranteed for JPG and JPEG formats.
        - Other formats (e.g., PNG, BMP, TIFF) may work,
          but are not officially required by this function.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: Image pixel data in RGB format.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the path is not a file, or the image format
                    is unsupported, or the image cannot be processed.
        Exception: For any other unexpected errors.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        if not os.path.isfile(path):
            raise ValueError(f"Path is not a file: {path}")

        with Image.open(path) as img:
            img_format = img.format
            if img_format not in ['JPEG', 'JPG']:
                print(f"Warning: Format {img_format} is not JPG/JPEG")

            rgb_img = img.convert('RGB')

            img_array = np.array(rgb_img)

            print(f"The shape of image is: {img_array.shape}")

            return img_array

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: {e}")
    except Image.UnidentifiedImageError:
        raise ValueError("Error: Cannot identify image file")
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")
