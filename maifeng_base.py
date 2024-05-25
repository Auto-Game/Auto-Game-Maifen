#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   基础模版
@Time    :   2024年4月2日15:29:02
@Author  :   cwz
'''
import time

from helper_functions import GameAutoInit


class GameAutoBase(GameAutoInit):
    def __init__(self):
        super().__init__()
        self.jiaoshui_num = 3
    def 挂机(self):
        memu = [(119, 900), (195, 900), (269, 900), (346, 900), (421, 900)]
        run_ct = 1 # 当前执行次数
        while True:
            if run_ct == 3:
                self.notice_push("挂机任务结束")
                break
            # 417, 803  进阶   68, 902  返回  497, 575 首领
            self.点击(memu[2], 5)
            if self.find_pic("shouling_01.png")[0] > 0:
                self.notice_push("挑战首领")
                self.点击((497, 575), 5)
                t = time.time()
                while True:
                    if time.time() - t > 60 * 3:
                        print("超过3分钟，自动退出")
                        self.点击(memu[2], 5)
                        break
                    p = self.find_pic("tip_02.png")
                    if p[0] > 0:
                        self.notice_push("挑战胜利，挑战下一关")
                        self.点击((356, 815), 5)
                        break
                    else:
                        print("休息5秒")
                        time.sleep(5)

            self.点击图片("next_01.png", (0, 0, 540, 960), 5, 0.9)
            self.点击图片("back_01.png", (0, 0, 540, 960), 5)

            # 行李
            self.点击(memu[1], 5)
            self.点击图片("yjqh_01.png", (0, 0, 540, 960), 5)
            p = self.find_pic("cuizi_01.png", (38, 42, 493, 428), 0.9)
            if p[0] > 0:
                self.点击(p, 5.5)
                self.点击((416, 802), 5.5)  # 进阶
                self.点击((271, 744), 5.5)  # 进阶
                self.点击图片("queding_02.png", (0, 0, 540, 960), 5)  # 确定
                self.点击((271, 744), 5.5)
                self.点击图片("back_01.png", (0, 0, 540, 960), 5)

            self.点击(memu[2], 5)

            # 旅人
            self.点击(memu[3], 5)
            while True:
                p = self.find_pic("gxjn_01.png")
                if p[0] > 0:
                    self.点击(p, 5)
                    self.点击((394, 698), 5)
                    self.点击((271, 735), 5)
                    self.点击图片("back_01.png", (0, 0, 540, 960), 5)
                else:
                    break

            self.点击(memu[2], 5)
            self.点击(memu[2], 5)

            # 新手试炼
            self.点击((441, 275), 5)
            self.循环点击图片("lingqu_01.png", (0, 0, 540, 960), 3.5, 0.9)
            self.点击图片("back_01.png", (0, 0, 540, 960), 5)

            # 冒险手册
            self.点击((502, 279), 5)
            self.循环点击图片("lingqu_01.png", (0, 0, 540, 960), 3.5, 0.9)
            self.点击图片("back_01.png", (0, 0, 540, 960), 5)

            # 旅团任务
            self.旅团()

            # 日常活动
            # 每月签到

            # 月卡领取

            # 特殊活动

            # 纸飞机

            #

            print("休息1分钟")
            time.sleep(60)
            run_ct += 1

    def 旅团(self):
        self.点击((502, 433), 5)

        # 执行浇灌任务
        print("执行浇灌任务")
        self.点击图片("new_lvtuan_jiaoshui.png", (0, 0, 540, 960), 5)
        # 判断是否已浇灌
        txt = self.文字识别((202, 851, 338, 869))
        jiaoshui_flag = True
        if txt and "/5" in txt:
            txt = txt.replace("今日浇灌次数：", "")
            txt = txt.replace("/5", "")
            num = int(txt)
            if num >= self.jiaoshui_num:
                jiaoshui_flag = False
        if jiaoshui_flag:
            self.点击图片("new_lvtuan_jiaoshui_queren.png", (0, 0, 540, 960), 5)
            self.点击图片("queding_03.png", (0, 0, 540, 960), 5)
        self.点击图片("back_01.png|new_back_01.png", (0, 0, 540, 960), 5) # 返回旅团首页
        print("执行浇灌任务结束")

        # 执行调查队任务
        print("执行调查队任务")
        self.点击图片("new_lvtuan_diaochadui.png", (0, 0, 540, 960), 5)
        self.点击图片("new_lvtuan_kqdd.png", (0, 0, 540, 960), 5)
        # 添加三位队友
        self.点击((150, 570), 5)
        self.点击图片("new_lv_tjjx.png", (0, 0, 540, 960), 5)
        self.点击图片("new_lv_tjjx.png", (0, 0, 540, 960), 5)
        self.点击图片("new_lv_tjjx.png", (0, 0, 540, 960), 5)
        self.点击图片("back_01.png|new_back_01.png", (0, 0, 540, 960), 5) # 返回调查队匹配页
        self.点击图片("start_01.png", (0, 0, 540, 960), 5) # 开始调查
        self.notice_push("旅团调查开始")
        st = time.time()
        while True:
            print("旅团调查中，等待3秒")
            if time.time() - st > 15 * 60:
                print("旅团调查，超过15分钟，自动退出")
                break
            p = self.find_pic("kaiqi_02.png|kaiqi_01.png|new_kaiqi_01.png|new_fangqi_01.png")
            if p[0] > 0:
                self.点击(p, 3.5)
                self.notice_push("旅团调查结束，开宝箱/放弃")
                break
            time.sleep(3)
        self.notice_push("旅团调查结束，退出")
        self.循环点击图片("back_01.png|new_back_01.png", (0, 0, 540, 960), 5) # 返回冒险首页

if __name__ == '__main__':
    game = GameAutoBase()
    game.挂机()
    # game.截屏保存()

    # print(game.find_pic("shouling_01.png"))
    # game.点击((269, 900), 5.5)
    # game.点击图片("yjqh_01.png", (0, 0, 960, 540), 5)
    # game.点击图片("red_01.png", (159, 864, 233, 923), 5)
    # game.截屏保存()
