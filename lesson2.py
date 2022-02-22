# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:08:00 2022

@author: ben72
"""

from mcpi.minecraft import Minecraft
import time

#part1
# mc = Minecraft.create()
# while True:
#     mc.postToChat("hy")

#part2
# mc = Minecraft.create()
# t = 0
# while True:
#     t = t + 1
#     mc.postToChat("第" + str(t) + "次")

#part3
mc = Minecraft.create()
mc.postToChat("I'm looking you!!!!!!!!!!")
while True:
    x, y, z = mc.player.getTilePos()
    mc.postToChat("我看到你在 x: " + str(x) + "Y:" + str(y) + "Z:" + str(z))