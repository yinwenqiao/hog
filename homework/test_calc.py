#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pytest


class TestCal:
    @pytest.mark.run(order=2)
    def test_add(self, init_calc, get_data_add):
        assert get_data_add[2] == round(init_calc.add(get_data_add[0], get_data_add[1]))

    @pytest.mark.run(order=1)
    def test_div(self, init_calc, get_data_div):
        try:
            assert get_data_div[2] == round(init_calc.div(get_data_div[0], get_data_div[1]))
        except ZeroDivisionError:
            print("除数为0")