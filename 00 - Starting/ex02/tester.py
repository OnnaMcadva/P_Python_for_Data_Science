from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_str1 = "Brian"
ft_str2 = "Toto"

ft_int = 10
ft_float = 3.14

ft_none = None


def ft_lambda(x):
    return x


def ft_func(x):
    return x


class MyClass:
    pass


ft_obj = MyClass()

test_objects = [
    ft_list, ft_tuple, ft_set, ft_dict,
    ft_str1, ft_str2,
    ft_int, ft_float,
    ft_none,
    ft_lambda, ft_func,
    ft_obj
]

print("\n\033[38;5;219m=== BEGIN TEST ===\033[0m\n")
for obj in test_objects:
    print(f"\033[38;5;206mTesting object: \033[0m{repr(obj)}")
    result = all_thing_is_obj(obj)
    print(f"\033[38;5;118mReturned:\033[0m 🦎{result}🦎\n")
print("\033[38;5;222m=== END TEST ===\033[0m\n")
