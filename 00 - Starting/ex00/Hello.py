# Lists in Python are mutable (changeable) and ordered
#       (element order is preserved)
# Tuples in Python are immutable (unchangeable) and
#       ordered (element order is preserved)
# Sets in Python are unordered (order is not guaranteed)
#       and contain only unique elements
# Dictionaries in Python are mutable (modifiable) and
#       associative (access by key)

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

try:
    if len(ft_list) > 1:
        ft_list[1] = "World!"
    else:
        print("List index 1 not found.")
except Exception as e:
    print(f"Error modifying list: {e}")

try:
    ft_tuple = (ft_tuple[0], "France!")
except Exception as e:
    print(f"Error modifying tuple: {e}")

try:
    if "tutu!" in ft_set:
        ft_set.remove("tutu!")
    else:
        print("Value 'tutu!' not found in set.")
except Exception as e:
    print(f"Error removing from set: {e}")

try:
    ft_set.add("Paris!")
except Exception as e:
    print(f"Error adding to set: {e}")

try:
    ft_dict["Hello"] = "42Paris!"
except Exception as e:
    print(f"Error modifying dict: {e}")

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
