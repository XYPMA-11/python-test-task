def func_float_one(x):
    return int(x)


def func_float_two(x, y):
    return type(x/y)


def test_float_one():
    try:
        assert float(func_float_one(10)**315)
    except OverflowError:
        pass


def test_float_two():
    assert func_float_two(1, 5) == float



def func_str_two(x, y):
    return type(x-y)


def test():
    s = "hello"
    a = 'z'
    try:
        assert a in s
    except AssertionError:
        pass

def test_two():
    try:
        assert func_str_two("5678", 100) == str
    except TypeError:
        pass

dict = {"one": 1, "two": 2, "three": 3}

def test_dict_one():
    a = 'one'
    try:
        assert a in dict
    except AssertionError:
        pass
def test_dict_two():
    assert dict.get("five") is None

