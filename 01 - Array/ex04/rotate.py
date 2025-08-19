#!/usr/bin/env python3
import numpy as np
from load_image import load_image, image_to_array, crop_square_center
import matplotlib.pyplot as plt


def manual_transpose(image_arr):
    """
    Manual transpose implementation without using libraries

    Args:
        image_array (numpy.ndarray): Input image array

    Returns:
        numpy.ndarray: Transposed image array
    """
    try:
        if image_arr is None:
            raise ValueError("Cannot transpose None image array")

        if len(image_arr.shape) == 2:
            height, width = image_arr.shape
            transp = np.empty((width, height), dtype=image_arr.dtype)

            for i in range(height):
                for j in range(width):
                    transp[j, i] = image_arr[i, j]

        elif len(image_arr.shape) == 3:
            height, width, channels = image_arr.shape
            transp = np.empty((width, height, channels), dtype=image_arr.dtype)

            for i in range(height):
                for j in range(width):
                    for c in range(channels):
                        transp[j, i, c] = image_arr[i, j, c]
        else:
            raise ValueError(f"Unsupported image shape: {image_arr.shape}")

        return transp

    except Exception as e:
        print(f"Error in manual transpose: {e}")
        return None


def print_image_info(image_arr, title="Image"):
    """
    Print information about the image array

    Args:
        image_array (numpy.ndarray): Image array to analyze
        title (str): Title for the printout
    """
    try:
        if image_arr is None:
            raise ValueError("Cannot get info from None image array")

        print(f"\n=== {title.upper()} INFORMATION ===")
        print(f"The shape of image is: {image_arr.shape}")

        if len(image_arr.shape) == 3:
            print(f"Number of channels: {image_arr.shape[2]}")
        else:
            print("Number of channels: 1")

        print(f"Data type: {image_arr.dtype}")

    except Exception as e:
        print(f"Error printing image info: {e}")


def print_pixel_sample(image_arr, sample_size=3):
    """
    Print a sample of pixel content from the image

    Args:
        image_array (numpy.ndarray): Image array
        sample_size (int): Number of pixels to sample from beginning
    """
    try:
        if image_arr is None:
            raise ValueError("Cannot print pixl content from None image array")

        print("Pixel content sample (first few pixels):")

        if len(image_arr.shape) == 3:
            flat_sample = image_arr[:sample_size, :sample_size, :].reshape(-1, image_arr.shape[2])
            for i, pixel in enumerate(flat_sample[:sample_size*2]):
                print(f"  {pixel}")
        else:
            flat_sample = image_arr[:sample_size, :sample_size].flatten()
            for i, pixel in enumerate(flat_sample[:sample_size*2]):
                print(f"  [{pixel}]")

        print("  ...")

    except Exception as e:
        print(f"Error printing pixel sample: {e}")


def display_image(image_array, title="Image"):
    """
    Display the image using matplotlib

    Args:
        image_array (numpy.ndarray): Image array to display
        title (str): Title for the plot
    """
    try:
        if image_array is None:
            raise ValueError("Cannot display None image array")

        plt.figure(figsize=(8, 6))

        if len(image_array.shape) == 3:
            plt.imshow(image_array)
        else:
            plt.imshow(image_array, cmap='gray')

        plt.title(title)
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.colorbar(label='Intensity')
        plt.show()

    except Exception as e:
        print(f"Error displaying image: {e}")


def main():
    """
    Main function to execute the rotate program
    """
    try:
        image_path = "animal.jpeg"
        print(f"Loading image: {image_path}")

        pil_image = load_image(image_path)
        if pil_image is None:
            return

        image_array = image_to_array(pil_image)
        if image_array is None:
            return

        print("\nCropping square from center...")
        cropped_image = crop_square_center(image_array, size=400)
        if cropped_image is None:
            return

        print_image_info(cropped_image, "Cropped Square")
        print_pixel_sample(cropped_image)

        print("\nDisplaying cropped square image...")
        display_image(cropped_image, "Cropped Square Image")

        print("\nPerforming manual transpose...")
        transposed_image = manual_transpose(cropped_image)
        if transposed_image is None:
            return

        print_image_info(transposed_image, "Transposed")
        print_pixel_sample(transposed_image)

        print("\nDisplaying transposed image...")
        display_image(transposed_image, "Transposed Image")

        print("\nProgram completed successfully!")

    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"Unexpected error in main program: {e}")


if __name__ == "__main__":
    main()
