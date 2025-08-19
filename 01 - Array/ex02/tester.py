from load_image import ft_load


def main():
    """Test function for ft_load"""
    try:
        image_array = ft_load("samorost.jpg")
        print(image_array)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
