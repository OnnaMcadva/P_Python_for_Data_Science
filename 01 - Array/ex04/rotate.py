#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def crop_center_square(
    img: np.ndarray, size: int = 400, channel: int | None = None
) -> np.ndarray:
    """
    Crop a square region from the center of the image.

    Args:
        img (np.ndarray): Input image array (H, W, C).
        size (int): Size of the square to crop. Must be <= min(H, W).
        channel (int | None): If specified, selects a single channel
                                (0=R, 1=G, 2=B).
                              If None, keeps all channels.

    Returns:
        np.ndarray: Cropped square image (H, W, C) or (H, W) if channel is set.

    Raises:
        ValueError: If input is invalid or size is too large.
    """
    try:
        if img is None:
            raise ValueError("Input image is None.")

        if not isinstance(img, np.ndarray):
            raise ValueError("Input must be a numpy array.")

        if img.ndim != 3 or img.shape[2] != 3:
            raise ValueError("Image must have shape (H, W, 3).")

        h, w, _ = img.shape
        if size > min(h, w):
            raise ValueError(
                f"Crop size {size} exceeds image dimensions {h}x{w}."
            )

        start_y = (h - size) // 2
        start_x = (w - size) // 2
        cropped = img[start_y:start_y+size, start_x:start_x+size, :]

        if channel is not None:
            if channel not in (0, 1, 2):
                raise ValueError("Channel must be 0, 1, or 2.")
            cropped = cropped[:, :, channel]

        return cropped

    except Exception as e:
        raise ValueError(f"Error cropping image: {e}")


def manual_transpose(image_arr: np.ndarray) -> np.ndarray:
    """
    Manually transpose a grayscale image without numpy.transpose.

    Supports input shapes:
      - (H, W)      -> returns (W, H)
      - (H, W, 1)   -> returns (W, H)

    Raises:
        ValueError: if input is invalid.
    """
    try:
        if image_arr is None:
            raise ValueError("Cannot transpose None image array")

        if not isinstance(image_arr, np.ndarray):
            raise ValueError("Input must be a numpy array")

        if image_arr.ndim == 2:
            src = image_arr
        elif image_arr.ndim == 3 and image_arr.shape[2] == 1:
            src = image_arr[:, :, 0]
        else:
            raise ValueError("Input must be 2D (H, W) or (H, W, 1) grayscale")

        h, w = src.shape
        out = np.zeros((w, h), dtype=src.dtype)

        for i in range(h):
            for j in range(w):
                out[j, i] = src[i, j]

        return out

    except Exception as e:
        raise ValueError(f"Error in manual transpose: {e}")


def main() -> None:
    """
    Main function for the rotate exercise.
    Loads the image, crops center 400x400 (single channel), prints arrays,
    transposes manually, and displays the result.
    """
    try:
        img = ft_load("samorost.jpg")

        cropped = crop_center_square(img, size=400, channel=0)
        print(f"The zoomed shape of image is: {cropped.shape}")
        print(cropped)

        transposed = manual_transpose(cropped)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        plt.imshow(transposed, cmap="gray")
        plt.title("Zoomed and Transposed Image 😺")
        plt.xlabel("X-axis (pixels)")
        plt.ylabel("Y-axis (pixels)")
        plt.show()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
