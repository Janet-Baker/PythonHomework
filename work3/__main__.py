# -*- coding: UTF-8 -*- 
import sys


if __name__ == '__main__':
    # 输入数据
    d = (input()).split()
    # 读年月日
    # 问题：本代码没有考虑瞎输入的情况，比如输入了4个数。无条件信任了输入的数据。
    year = int(d[0])
    month = int(d[1])
    day = int(d[2])
    # 1月和2月无需考虑闰年
    if month == 1:
        print(day)
    elif month == 2:
        print((day + 31))
        # 注：输入一个不存在的日期，比如2022年2月32日？本题没有考虑胡乱输入的情况。
    # 3月和之后，需要考虑闰年
    else:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        i = 0
        sums = 0
        days[(month - 1)] = day
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days[1] = 29
        for i in range(0, month, 1):
            sums = sums + days[i]
        print(sums)
