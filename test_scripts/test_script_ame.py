# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 10:29
# @Author  : Xin Zhang
# @File    : test_script_ame.py

import QuantLib as Ql
from QuantLib import Date, VanillaOption, SimpleQuote, QuoteHandle
from option_tools.utils.tools import GreeksComputer

start_date = Date(8, 5, 2015)
end_date = Date(15, 1, 2016)

strike_price = 130

Ql.Settings.instance().evaluationDate = start_date

# set calendar and day counter
calendar = Ql.China()
day_counter = Ql.ActualActual()

payoff = Ql.PlainVanillaPayoff(Ql.Option.Call, strike_price)

ame_option = VanillaOption(payoff, Ql.AmericanExercise(start_date, end_date))

underlying_price = SimpleQuote(127.62)
interest_rate = SimpleQuote(0.001)
volatility = SimpleQuote(0.2)
dividend = SimpleQuote(0.0163)

risk_free_curve = Ql.FlatForward(
    0,
    Ql.TARGET(),
    QuoteHandle(interest_rate),
    day_counter)
volatility_curve = Ql.BlackConstantVol(
    0, Ql.TARGET(), QuoteHandle(volatility), day_counter)
dividend_curve = Ql.FlatForward(
    0,
    Ql.TARGET(),
    QuoteHandle(dividend),
    day_counter)

process = Ql.BlackScholesMertonProcess(
    QuoteHandle(underlying_price),
    Ql.YieldTermStructureHandle(dividend_curve),
    Ql.YieldTermStructureHandle(risk_free_curve),
    Ql.BlackVolTermStructureHandle(volatility_curve)
)

ame_option.setPricingEngine(Ql.FDAmericanEngine(process))
print('FDAmericanEngine price:', ame_option.NPV())

# finite difference method
ame_option.setPricingEngine(Ql.FDDividendAmericanEngine(process))
print('FDDividendAmericanEngine price:', ame_option.NPV())

# BAW
ame_option.setPricingEngine(Ql.BaroneAdesiWhaleyEngine(process))
print('BaroneAdesiWhaleyEngine price', ame_option.NPV())

#
steps = 200
ame_option.setPricingEngine(Ql.BinomialVanillaEngine(process, 'crr', steps))
print('BinomialVanillaEngine price', ame_option.NPV())

# actual price : 7
# implied volatility:
impl_vol = ame_option.impliedVolatility(7, process)
print(impl_vol)

# theoretical method
gc = GreeksComputer(ame_option)
gc.get_greeks()

# implement numerical method
gc = GreeksComputer(ame_option)

gc.get_greeks(underlying_price,
           interest_rate,
           volatility,
           start_date)

# implied volatility
