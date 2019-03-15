import numpy as np
import bisect
from termcolor import cprint

tax = np.array([
    [1500, 0.03, 0],
    [4500, 0.1, 105],
    [9000, 0.2, 555],
    [35000, 0.25, 1005],
    [55000, 0.3, 2755],
    [80000, 0.35, 5505],
    [10000000000000000, 0.45, 13505]
])

free_tax = 3500

insurance_rate = 0.155
com_insurance_rate = 0.26718


def find_tax_level(income):
  level = bisect.bisect_left(tax[:,0], income)
  return tax[level,1:]


def calculate_insurance(income):
    insurance = income * 0.155
    print("五险一金：{}".format(insurance))
    return insurance


def calculate_tax(income, bonus=False):
    if bonus:
        tax_rate, deduction = find_tax_level(income / 12)
    else:
        income = income - free_tax
        tax_rate, deduction = find_tax_level(income)
    payed_tax = income * tax_rate - deduction
    print("应税收入：{}，税率：{:.2f},交税：{}".format(income, tax_rate, payed_tax))
    return payed_tax


def income_after_tax(income):
    print("月工资计算：")
    print("工资：{}".format(income))
    insurance = calculate_insurance(income)
    i = income - calculate_tax(income - insurance) - insurance
    print("到手工资：{}".format(i))
    y = i * 12
    print("一年工资：{}".format(i * 12))
    return y


def bonuses(income):
    print("年终奖计算：")
    print("年终奖：{}".format(income))
    i = calculate_tax(income, bonus=True)
    print("年终奖交税：{}".format(i))
    y = income - i
    print("到手年终奖：{}".format(y))
    return y


red_print = lambda x: cprint(x, 'red')
yellow_print = lambda x: cprint(x, 'yellow')


month_income = 16000
annual_bonus = 48000

red_print("基本情况：月工资：{}， 年终奖：{}（即每月{}）".format(month_income, annual_bonus, annual_bonus / 12))

annual_income_after_tax = income_after_tax(month_income)
print()
annual_bonus_after_tax = bonuses(annual_bonus)

print()
red_print("年终奖当工资发时，工资计算：")

aa = income_after_tax(month_income + annual_bonus / 12)

print()

red_print("原到手年薪+到手年终奖：{} + {} = {}".format(annual_income_after_tax, annual_bonus_after_tax, annual_income_after_tax + annual_bonus_after_tax))
red_print("无年终奖时到手年薪：{}".format(aa))
red_print("年终奖可避税：{}".format(annual_bonus_after_tax + annual_income_after_tax - aa))

print()

yellow_print("公司一年多交五险一金：年终奖 * 单位五险一金费率：{} * {:.3f}% = {}".format(annual_bonus, com_insurance_rate * 100, annual_bonus * com_insurance_rate))