# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:07:08 2022

@author: ben72
"""
import random
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

#part1
# for i in range(20):
#     r = random.randrange(1, 5)
#     if r == 1:
#         mc.setBlocks(x, y, z, x+4, y, z, 2)
#         x += 4
#     if r == 2:
#         mc.setBlocks(x, y, z, x-4, y, z, 7)
#         x -= 4
#     if r == 3:
#         mc.setBlocks(x, y, z, x, y, z+4, 13)
#         z += 4
#     if r == 4:
#         mc.setBlocks(x, y, z, x, y, z-4, 68)
#         z -= 4
# part29000000000000000000000000000000000000000
while True:
    mc.executeCommand('time add 50')
    time.sleep(0.05)