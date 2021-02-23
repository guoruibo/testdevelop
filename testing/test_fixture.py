import pytest
import yaml


@pytest.fixture()
def test_add():
    print("测试")
    return (1 + 3)


def test_addl(test_add):
    print(test_add + 5)
