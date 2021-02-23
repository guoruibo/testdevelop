import pytest


@pytest.fixture()
def login():
    print("测试")
    # return (1+3)
    # yield
    # print("退出登录")


def test_search(login):
    print("搜索")


@pytest.fixture()
# def select(login):
def select():
    print("选择")
    yield
    print("退出登录")


@pytest.mark.usefixtures("select")
def test_shop():
    print("购物")
