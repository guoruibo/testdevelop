def add(a, b):
    return (a + b)


def min(a, b):
    return (a - b)


def mul(a, b):
    return (a * b)


def div(a, b):
    if b == 0:
        return ("被除数不能为0")
    else:
        return (a / b)


def test_ADD():
    assert add(3, 4) == 7


def test_MIN():
    assert min(3, 4) == -1


def test_MUL():
    assert mul(3, 4) == 12


def test_DIV():
    assert div(8, 0) == 2
