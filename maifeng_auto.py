#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   基础模版
@Time    :   2024年4月2日15:29:02
@Author  :   cwz
'''
import time

from maifeng_base import GameAutoBase
from maifeng_shilian import GameAutoShiLian


if __name__ == '__main__':
    gameBase = GameAutoBase()
    gameSL = GameAutoShiLian()

    while True:
        gameBase.挂机()
        gameSL.试炼()
        print("休息2分钟")
        time.sleep(2 * 60)
