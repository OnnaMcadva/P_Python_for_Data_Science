#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def crop_square_center(image_arr: np.ndarray, size=400) -> np.ndarray:
    """
    Crop a square from the center of the image.

    Args:
        image_arr (np.ndarray): Input image array
        size (int): Size of the square crop

    Returns:
        np.ndarray: Cropped square image
    """
    try:
        if image_arr is None:
            raise ValueError("Cannot crop None image array")

        if not isinstance(image_arr, np.ndarray):
            raise ValueError("Input must be a numpy array")

        if len(image_arr.shape) != 3 or image_arr.shape[2] != 3:
            raise ValueError("Image must have 3 channels (RGB)")

        h, w, _ = image_arr.shape
        if size > min(h, w):
            raise ValueError(
                f"Crop size {size} is larger than image dimensions {h}x{w}"
            )

        start_y = (h - size) // 2
        start_x = (w - size) // 2
        return image_arr[start_y:start_y+size, start_x:start_x+size, :]

    except Exception as e:
        raise ValueError(f"Error cropping image: {e}")


def to_grayscale(image_arr: np.ndarray) -> np.ndarray:
    """
    Convert RGB image array to grayscale (1 channel).
    """
    try:
        if image_arr is None:
            raise ValueError("Cannot convert None image to grayscale")

        if not isinstance(image_arr, np.ndarray):
            raise ValueError("Input must be a numpy array")

        if len(image_arr.shape) != 3 or image_arr.shape[2] != 3:
            raise ValueError("Input must have 3 channels (RGB)")

        gray = np.mean(image_arr, axis=2).astype(np.uint8)
        return gray.reshape(gray.shape[0], gray.shape[1], 1)

    except Exception as e:
        raise ValueError(f"Error converting to grayscale: {e}")


def manual_transpose(image_arr: np.ndarray) -> np.ndarray:
    """
    Manually transpose the image array without numpy.transpose.
    """
    try:
        if image_arr is None:
            raise ValueError("Cannot transpose None image array")

        if not isinstance(image_arr, np.ndarray):
            raise ValueError("Input must be a numpy array")

        if len(image_arr.shape) != 3 or image_arr.shape[2] != 1:
            raise ValueError("Input must be grayscale (H, W, 1)")

        h, w, c = image_arr.shape
        transposed = np.zeros((w, h, c), dtype=image_arr.dtype)
        for i in range(h):
            for j in range(w):
                transposed[j, i] = image_arr[i, j]

        return transposed

    except Exception as e:
        raise ValueError(f"Error in manual transpose: {e}")


def main():
    """
    Main function for the rotate exercise.
    """
    try:
        img = ft_load("samorost.jpg")

        cropped = crop_square_center(img, 400)
        gray = to_grayscale(cropped)

        print(f"The shape of image is: {gray.shape}")
        print(gray)

        transposed = manual_transpose(gray)
        transposed = transposed.reshape(
            transposed.shape[0], transposed.shape[1]
            )

        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        plt.imshow(transposed, cmap="gray")
        plt.title("Transposed Image")
        plt.xlabel("X-axis (pixels)")
        plt.ylabel("Y-axis (pixels)")
        plt.show()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
