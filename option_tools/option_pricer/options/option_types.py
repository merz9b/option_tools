# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 11:18
# @Author  : Xin Zhang
# @File    : option_types.py

"""
params level

1 : european or american

2 : vannilla or exotic

3 : asian or barrier

4 : discrete or continuous

5 : geometric or arithmetic



10 : engine : theoretic , mc or fd
"""

from QuantLib import Option as OpType


class OptionMetaType(type):
    def __new__(mcs, name, bases, attrs):
        if len(bases) > 0:
            attrs['oid'] += bases[0].oid
        return super().__new__(mcs, name, bases, attrs)


# OptionType:
CALL = OpType.Call
PUT = OpType.Put


class CodeGen:
    # 1
    EUROPEAN = 1
    AMERICAN = 2

    # 2
    VANNILLA = 10
    EXOTIC = 20

    # 3
    ASIAN = 100
    BARRIER = 200

    # 4
    DISCRETE = 1000
    CONTINUOUS = 2000

    # 5
    GEOMETRIC = 10000
    ARITHMETIC = 20000


if __name__ == '__main__':
    print(CodeGen.AMERICAN)
