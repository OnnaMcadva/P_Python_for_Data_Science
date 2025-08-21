import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(img: np.ndarray) -> np.ndarray:
    """
    Extract a zoomed portion of the image (center 400x400, one channel).
    """
    try:
        h, w, c = img.shape
        if c != 3:
            raise ValueError("Image must have 3 channels (RGB).")

        start_x = w // 2 - 200
        start_y = h // 2 - 200

        # zoomed = img[start_y:start_y+400, start_x:start_x+400, 0:1]
        zoomed = img[start_y:start_y+400, start_x:start_x+400, 0]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        return zoomed

    except Exception as e:
        raise ValueError(f"Error zooming image: {e}")


if __name__ == "__main__":
    try:
        img = ft_load("samorost.jpg")
        print(img)

        zoomed = zoom_image(img)

        plt.imshow(zoomed, cmap="gray")
        plt.title("Zoomed Image (Red channel)")
        plt.xlabel("X-axis (pixels)")
        plt.ylabel("Y-axis (pixels)")
        plt.show()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
