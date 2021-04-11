import pytest
from Calculator import Calculator

class Testcal:
    def setup_class(self):
          print("setup_class")
          self.calc = Calculator()
    def teardown_class(self):
        print("teardown_class")
        self.calc = Calculator()

    @pytest.mark.parametrize('a,b,expect',[
        [1,1,2],[0.1,0.1,0.2],[1000,1000,2000],[0,1000,1000]
    ],ids=['int1','float','bignum','zeronum'])
    def test_add(self,a,b,expect):
        # calc = Calculator()
        assert expect == self.calc.add(a,b)

    @pytest.mark.parametrize('a,b,expect',[
        [2,2,1],[0.2,2,0.1],[0,2,0],[100,0,"除数不能为0"]
    ],ids=['int1','float','bignum','zeronum'])
    def test_div(self,a,b,expect):
        # calc = Calculator()
        assert expect == self.calc.div(a,b)

    @pytest.mark.parametrize('a,b,expect',[
        [2,2,4],[0.2,-2,-0.4],[0,2,0],[100,0,0]
    ],ids=['int1','float','bignum','zeronum'])
    def test_mul(self,a,b,expect):
        # calc = Calculator()
        assert expect == self.calc.mul(a,b)

    @pytest.mark.parametrize('a,b,expect',[
        [2,2,0],[1,2,-1],[0,2,-2],[100,0,100]
    ],ids=['int1','float','bignum','zeronum'])
    def test_sub(self,a,b,expect):
        # calc = Calculator()
        assert expect == self.calc.sub(a,b)