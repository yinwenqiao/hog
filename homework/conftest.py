#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pytest
import yaml

from Calculator import Calculator


@pytest.fixture(scope='class')
def initcalc_class():
    # setup
    print("setup")
    calc = Calculator()
    yield calc
    # teardown
    print("teardown")

def read_data_add():
    with open("./add_data.yaml") as f:
        data_add = yaml.load(f)
        return data_add


def read_data_div():
    with open("./div_data.yaml") as f:
        data_div = yaml.load(f)
        return data_div

@pytest.fixture(params=read_data_add()["datas"], ids=read_data_add()["ids"])
def get_data_add(request):
    return request.param

@pytest.fixture(params=read_data_div()["datas"], ids=read_data_div()["ids"])
def get_data_div(request):
    return request.param






@pytest.fixture(params=[[0.1, 0, False], [2, 2, 2], [10, 1, 10]],
                ids=['zero', 'int', 'int1'])
def get_div_datas(request):
    return request.param

def pytest_collection_modifyitems(session,config,items:list):
    print('这是收集所有测试用例的方法')
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode