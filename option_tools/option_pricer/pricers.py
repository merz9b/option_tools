# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 14:09
# @Author  : Xin Zhang
# @File    : pricers.py

from .options.engine_types import EngineType
from .options.option_base import (EuropeanOption, AmericanOption, ArithmeticDiscreteAsianOption)

PRICER_COLLECTIONS = {}


def register_pricer(pricer_id):
    def wrapper(pricer_func):
        global PRICER_COLLECTIONS
        PRICER_COLLECTIONS[pricer_id] = pricer_func
        return pricer_func
    return wrapper


@register_pricer(12)
def european_(op):
    return op
