import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
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
        if not any(
                image_path.lower().endswith(ext)
                for ext in valid_extensions
        ):
            raise ValueError(
                f"Unsupported file format. "
                f"Supported formats: {valid_extensions}"
            )

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


def display_image_with_axes(image_array, title="Image"):
    """
    Display image with scale on x and y axes

    Args:
        image_array (numpy.ndarray): Image array to display
        title (str): Title for the plot
    """
    try:
        if image_array is None:
            raise ValueError("Cannot display None image array")

        plt.figure(figsize=(10, 8))
        plt.imshow(image_array)
        plt.title(title)
        plt.xlabel('X Axis (pixels)')
        plt.ylabel('Y Axis (pixels)')
        plt.colorbar(label='Intensity')
        plt.grid(True, alpha=0.3)
        plt.show()

    except Exception as e:
        print(f"Error displaying image: {e}")
