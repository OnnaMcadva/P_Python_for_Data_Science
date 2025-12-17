from DiamondTrap import King


def main():
    try:
        joffrey = King("Joffrey")
        print("Initial state:", joffrey.__dict__)

        joffrey.eyes = "blue"
        joffrey.hairs = "light"
        print("Eyes:", joffrey.eyes)
        print("Hairs:", joffrey.hairs)
        print("Updated state:", joffrey.__dict__)

        joffrey.die()
        print("Is alive after die():", joffrey.is_alive)

        try:
            joffrey.eyes = ""
        except ValueError as e:
            print("Caught error as expected:", e)

        try:
            joffrey.hairs = 123
        except ValueError as e:
            print("Caught error as expected:", e)

        another_king = King("Robert", is_alive=False)
        print("Another king:", another_king.__dict__)
        another_king.eyes = "green"
        another_king.hairs = "black"
        print("Modified another king:", another_king.__dict__)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
