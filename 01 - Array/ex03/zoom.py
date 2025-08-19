#!/usr/bin/env python3
import numpy as np
from load_image import load_image, image_to_array, display_image_with_axes


def print_image_info(image_array):
    """
    Print information about the image array

    Args:
        image_array (numpy.ndarray): Image array to analyze
    """
    try:
        if image_array is None:
            raise ValueError("Cannot get info from None image array")

        print(f"The shape of image is: {image_array.shape}")
        print(f"Number of channels: "
              f"{image_array.shape[2] if len(image_array.shape) > 2 else 1}")
        print(f"Data type: {image_array.dtype}")
        print(f"Min value: {np.min(image_array)},"
              f"Max value: {np.max(image_array)}")

    except Exception as e:
        print(f"Error printing image info: {e}")


def print_pixel_content(image_array, sample_size=5):
    """
    Print a sample of pixel content from the image

    Args:
        image_array (numpy.ndarray): Image array
        sample_size (int): Number of pixels to sample from beginning and end
    """
    try:
        if image_array is None:
            raise ValueError("Cannot print pixl content from None image array")

        print("Pixel content (first few and last few pixels):")

        if len(image_array.shape) == 3:
            flattened = image_array.reshape(-1, image_array.shape[2])
        else:
            flattened = image_array.flatten()

        print("First pixels:")
        for i in range(min(sample_size, len(flattened))):
            print(f"  {flattened[i]}")

        print("Last pixels:")
        for i in range(max(0, len(flattened) - sample_size), len(flattened)):
            print(f"  {flattened[i]}")

    except Exception as e:
        print(f"Error printing pixel content: {e}")


def zoom_image(image_array, zoom_factor=2.0, center=None):
    """
    Zoom into the image by cropping and resizing

    Args:
        image_array (numpy.ndarray): Input image array
        zoom_factor (float): Zoom factor (>1 zooms in, <1 zooms out)
        center (tuple): Center point for zoom(y, x). If None, uses image center

    Returns:
        numpy.ndarray: Zoomed image array
    """
    try:
        if image_array is None:
            raise ValueError("Cannot zoom None image array")

        if zoom_factor <= 0:
            raise ValueError("Zoom factor must be positive")

        height, width = image_array.shape[0], image_array.shape[1]

        crop_height = int(height / zoom_factor)
        crop_width = int(width / zoom_factor)

        if center is None:
            center_y, center_x = height // 2, width // 2
        else:
            center_y, center_x = center

        start_y = max(0, center_y - crop_height // 2)
        end_y = min(height, start_y + crop_height)
        start_x = max(0, center_x - crop_width // 2)
        end_x = min(width, start_x + crop_width)

        if end_y - start_y < crop_height:
            start_y = max(0, end_y - crop_height)
        if end_x - start_x < crop_width:
            start_x = max(0, end_x - crop_width)

        if len(image_array.shape) == 3:
            cropped = image_array[start_y:end_y, start_x:end_x, :]
        else:
            cropped = image_array[start_y:end_y, start_x:end_x]

        print(f"New shape after slicing: {cropped.shape}")

        return cropped

    except Exception as e:
        print(f"Error zooming image: {e}")
        return None


def main():
    """
    Main function to execute the zoom program (Ex03)
    """
    try:
        image_path = "samorost.jpg"
        print(f"Loading image: {image_path}")

        pil_image = load_image(image_path)
        if pil_image is None:
            return

        image_array = image_to_array(pil_image)
        if image_array is None:
            return

        print(f"The shape of image is: {image_array.shape}")
        print(f"Number of channels: "
              f"{image_array.shape[2] if len(image_array.shape) > 2 else 1}")
        print("Pixel content of the image:")
        print(image_array)

        zoomed_image = zoom_image(image_array, zoom_factor=2.0)
        if zoomed_image is not None:
            print(f"New shape after slicing: {zoomed_image.shape}")
            print(zoomed_image)

            display_image_with_axes(zoomed_image, "Zoomed Image")

    except Exception as e:
        print(f"Unexpected error in main program: {e}")


if __name__ == "__main__":
    main()
