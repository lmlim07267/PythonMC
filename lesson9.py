# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:08:32 2022

@author: ben72
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
#part1
# height = 8
# width = height*2-1
# for i in range(height):
#     x1 = x + i
#     y1 = y + i
#     z1 = z + i
#     x2 = x + width - i - 1
#     z2 = z + width - i - 1
#     mc.setBlocks(x1, y1, z1, x2, y1, z2, 46)

# def boom(x, y, z, h, ID):
#     height = h
#     width = height*2-1
#     for i in range(height):
#         x1 = x + i
#         y1 = y + i
#         z1 = z + i
#         x2 = x + width - i - 1
#         z2 = z + width - i - 1
#         mc.setBlocks(x1, y1, z1, x2, y1, z2, ID)

# for u in range(1, 101, 20):
#     boom(x+u, y, z, 10, 46)

#part2
# line1 = []
# line2 = []
# line3 = []

# for i in range(1, 4):
#     line1.append(i*1)
# for i in range(1, 4):
#     line2.append(i*2)
# for i in range(1, 4):
#     line3.append(i*3)
# mc.setSign(x, y, z, 63, 0, str(line1), str(line2), str(line3))

#part3
number = 1
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x, y, z, 60)
    number *= 2
    mc.postToChat(str(number))