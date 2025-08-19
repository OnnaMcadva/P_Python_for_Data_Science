import numpy as np
from PIL import Image
import os


def load_image(image_path):
    """
    Load an image from the given path and handle any errors

    Args:
        image_path (str): Path to the image file

    Returns:
        PIL.Image.Image or None: Loaded image or None if error occurs
    """
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file '{image_path}' not found")

        if not os.path.isfile(image_path):
            raise ValueError(f"'{image_path}' is not a file")

        valid_extensions = ['.jpeg', '.jpg', '.png', '.bmp', '.tiff']
        file_ext = os.path.splitext(image_path.lower())[1]
        if file_ext not in valid_extensions:
            raise ValueError(f"Unsupported file format. "
                             f"Supported: {valid_extensions}")

        image = Image.open(image_path)

        if image is None:
            raise ValueError("Failed to load image - image object is None")

        return image

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while loading image: {e}")
        return None


def image_to_array(image):
    """
    Convert PIL Image to numpy array
            # Grayscale image
    Args:
        image (PIL.Image.Image): Input image

    Returns:
        numpy.ndarray: Image as numpy array
    """
    try:
        if image is None:
            raise ValueError("Cannot convert None image to array")

        return np.array(image)

    except Exception as e:
        print(f"Error converting image to array: {e}")
        return None


def crop_square_center(image_arr, size=400):
    """
    Crop a square from the center of the image

    Args:
        image_array (numpy.ndarray): Input image array
        size (int): Size of the square crop

    Returns:
        numpy.ndarray: Cropped square image
    """
    try:
        if image_arr is None:
            raise ValueError("Cannot crop None image array")

        if len(image_arr.shape) not in [2, 3]:
            raise ValueError(f"Invalid image shape: {image_arr.shape}")

        height, width = image_arr.shape[0], image_arr.shape[1]

        if size > min(height, width):
            raise ValueError(f"Crop size {size} larger "
                             f"than image dimensions {height}x{width}")

        start_y = (height - size) // 2
        start_x = (width - size) // 2

        if len(image_arr.shape) == 3:
            cropped = image_arr[start_y:start_y+size, start_x:start_x+size, :]
        else:
            cropped = image_arr[start_y:start_y+size, start_x:start_x+size]

        return cropped

    except Exception as e:
        print(f"Error cropping image: {e}")
        return None
