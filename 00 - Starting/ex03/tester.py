from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
Normal = "Brian"

tests = [
    (Nothing, "Nothing"),
    (Garlic, "Cheese"),
    (Zero, "Zero"),
    (Empty, "Empty"),
    (Fake, "Fake"),
    (Normal, None),
]

overall_result = 0

for obj, name in tests:
    result = NULL_not_found(obj)
    if result != 0:
        overall_result = 1

print(overall_result)
