# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:28:05 2022

@author: ben72
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# #part1
# # x, y, z = mc.player.getTilePos()
# # for i in range(99):
# #     mc.setBlock(x, y-1, z+i, 19)
# #part2
# x, y, z = mc.player.getTilePos()
# for i in range(99):
#     mc.setBlock(x-i, y-1, z-i, 89)
 #part3
 
x, y, z = mc.player.getTilePos()

for i in range(30):
    mc.setBlocks(x, y-1+i, z+i, x+2, y-1+i, z+i, 89)
    mc.setBlocks(x, y+i, z+i, x+2, y+i, z+i, 53, 2)