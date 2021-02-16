import pytest
import yaml

from pythoncode.Calcultor import Calcultor


def get_add_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
    return (datas['add']['datas'], datas['add']['ids'])


def get_div_datas():
    with open("./datas/calc.yml") as g:
        datas = yaml.safe_load(g)
        print(datas)
    return (datas['div']['datas'], datas['div']['ids'])


class TestCalc:
    add_datas = get_add_datas()
    div_datas = get_div_datas()

    # 前置条件
    def setup_class(self):
        self.calc = Calcultor()
        print('前置条件')

    # 后置条件
    def teardown_class(self):
        self.calc = Calcultor()
        print('后置条件')

    @pytest.mark.parametrize("a,b,result", add_datas[0], ids=add_datas[1])
    def test_add(self, a, b, result):
        # calc = self.Calcultor()
        print(f"a={a} , b={b} , result={result}")
        assert result == self.calc.add(a, b)

    # done 完善除法
    @pytest.mark.parametrize("a,b,result", div_datas[0], ids=div_datas[1])
    def test_div(self, a, b, result):
        # calc = self.Calcultor()
        print(f"a={a} , b={b} , result={result}")
        assert result == self.calc.div(a, b)
