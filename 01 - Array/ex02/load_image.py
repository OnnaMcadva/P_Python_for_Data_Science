from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.array:
    """
    Load an image, print its format and return pixels in RGB format.

    Args:
        path (str): Path to the image file

    Returns:
        np.array: Image array in RGB format

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format is not supported or
        image cannot be processed
        Exception: For other unexpected errors
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
