#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def _validate_image(array: np.ndarray) -> None:
    """
    Validate that the input is a proper RGB image (H, W, 3).

    Raises:
        ValueError: if array is None, not a numpy array, or wrong shape.
    """
    if array is None:
        raise ValueError("Input image is None")

    if not isinstance(array, np.ndarray):
        raise ValueError("Input must be a numpy array")

    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input must have shape (H, W, 3)")


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    try:
        _validate_image(array)
        inverted = 255 - array
        _display(inverted, "Inverted Image")
        return inverted
    except Exception as e:
        raise ValueError(f"Error in ft_invert: {e}")


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keep only the red channel of the image.
    """
    try:
        _validate_image(array)
        red = np.zeros_like(array)
        red[:, :, 0] = array[:, :, 0] * 1
        _display(red, "Red Filter")
        return red
    except Exception as e:
        raise ValueError(f"Error in ft_red: {e}")


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keep only the green channel of the image.
    """
    try:
        _validate_image(array)
        green = np.zeros_like(array)
        green[:, :, 1] = array[:, :, 1] - 0
        _display(green, "Green Filter")
        return green
    except Exception as e:
        raise ValueError(f"Error in ft_green: {e}")


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keep only the blue channel of the image.
    """
    try:
        _validate_image(array)
        blue = np.zeros_like(array)
        blue[:, :, 2] = array[:, :, 2]
        _display(blue, "Blue Filter")
        return blue
    except Exception as e:
        raise ValueError(f"Error in ft_blue: {e}")


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert the image to grayscale.
    """
    try:
        _validate_image(array)
        grey_values = (
            array[:, :, 0] / 3
            + array[:, :, 1] / 3
            + array[:, :, 2] / 3
        ).astype(np.uint8)

        grey = np.zeros_like(array)
        grey[:, :, 0] = grey_values
        grey[:, :, 1] = grey_values
        grey[:, :, 2] = grey_values

        _display(grey, "Grey Filter")
        return grey
    except Exception as e:
        raise ValueError(f"Error in ft_grey: {e}")


def ft_sepia_light(array: np.ndarray) -> np.ndarray:
    """
    Apply a sepia filter and slightly lighten the image.
    """
    try:
        _validate_image(array)

        R = 0.393*array[:, :, 0] + 0.769*array[:, :, 1] + 0.189*array[:, :, 2]
        G = 0.349*array[:, :, 0] + 0.686*array[:, :, 1] + 0.168*array[:, :, 2]
        B = 0.272*array[:, :, 0] + 0.534*array[:, :, 1] + 0.131*array[:, :, 2]

        sepia = np.zeros_like(array)
        sepia[:, :, 0] = np.clip(R + 20, 0, 255)
        sepia[:, :, 1] = np.clip(G + 20, 0, 255)
        sepia[:, :, 2] = np.clip(B + 20, 0, 255)

        sepia = sepia.astype(np.uint8)

        _display(sepia, "Sepia Light Filter")
        return sepia

    except Exception as e:
        raise ValueError(f"Error in ft_sepia_light: {e}")


def ft_neon(array: np.ndarray) -> np.ndarray:
    """
    Apply a neon pink->magenta->violet gradient over the original image.
    """
    try:
        _validate_image(array)
        h, w, _ = array.shape

        X = np.linspace(0, 1, w)
        Y = np.linspace(0, 1, h)
        xv, yv = np.meshgrid(X, Y)

        gradient = np.zeros_like(array, dtype=np.float32)
        gradient[:, :, 0] = (1-xv)*255 + yv*186
        gradient[:, :, 1] = (1-xv)*105 + yv*85
        gradient[:, :, 2] = (1-xv)*180 + yv*226

        neon = 0.5 * array.astype(np.float32) + 0.5 * gradient
        neon = np.clip(neon, 0, 255).astype(np.uint8)

        _display(neon, "Neon Overlay")
        return neon

    except Exception as e:
        raise ValueError(f"Error in ft_neon: {e}")


def _display(image: np.ndarray, title: str) -> None:
    """
    Display the image using matplotlib.
    """
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()


def main():
    """
    Main function to test all pimp filters.
    """
    try:
        from load_image import ft_load

        img = ft_load("samorost.jpg")
        print(img)

        _display(img, "Original Image")

        ft_invert(img)
        ft_red(img)
        ft_green(img)
        ft_blue(img)
        ft_grey(img)
        ft_sepia_light(img)
        ft_neon(img)

        print(ft_invert.__doc__)

    except Exception as e:
        print(f"Unexpected error in main: {e}")


if __name__ == "__main__":
    main()
