#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class TestDiv:
    def test_div(self, initcalc_class, get_div_datas):
        try:
            assert get_div_datas[2] == initcalc_class.div(get_div_datas[0], get_div_datas[1])
        except ZeroDivisionError:
            print("除数为0")
