def NULL_not_found(obj: any) -> int:
    try:
        if obj is None:
            print(f"Nothing: {obj} <class 'NoneType'>")
        elif isinstance(obj, float) and obj != obj:  # NaN
            print(f"Cheese: {obj} <class 'float'>")
        elif isinstance(obj, bool) and obj is False:
            print(f"Fake: {obj} <class 'bool'>")
        elif isinstance(obj, int) and obj == 0:
            print(f"Zero: {obj} <class 'int'>")
        elif isinstance(obj, str) and obj == '':
            print(f"Empty: {obj} <class 'str'>")
        else:
            print("Type not Found")
            return 1
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1
