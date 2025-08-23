#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of the image.
    """
    try:
        if array is None:
            raise ValueError("Cannot invert None array")

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
        if array is None:
            raise ValueError("Cannot apply red filter on None array")

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
        if array is None:
            raise ValueError("Cannot apply green filter on None array")

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
        if array is None:
            raise ValueError("Cannot apply blue filter on None array")

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
        if array is None:
            raise ValueError("Cannot convert None array to grey")

        grey_values = (
            array[:, :, 0] / 3
            + array[:, :, 1] / 3
            + array[:, :, 2] / 3).astype(np.uint8)

        grey = np.zeros_like(array)
        grey[:, :, 0] = grey_values
        grey[:, :, 1] = grey_values
        grey[:, :, 2] = grey_values

        _display(grey, "Grey Filter")
        return grey
    except Exception as e:
        raise ValueError(f"Error in ft_grey: {e}")


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

        img = ft_load("Sergi.jpg")

        _display(img, "Original Image")

        ft_invert(img)
        ft_red(img)
        ft_green(img)
        ft_blue(img)
        ft_grey(img)

        print(ft_invert.__doc__)

    except Exception as e:
        print(f"Unexpected error in main: {e}")


if __name__ == "__main__":
    main()
