# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:55:06 2022

@author: ben72
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


# part1
# while True:
#     x, y, z = mc.player.getTilePos()
#     a = mc.getBlock(x, y-1, z+1)
#     b = mc.getBlock(x, y-1, z-1)
#     c = mc.getBlock(x+1, y-1, z)
#     d = mc.getBlock(x-1, y-1, z)
    
#     if a==9 or b==9 or c==9 or d==9:
#         mc.setBlocks(x-1, y, z+1, x+1, y, z-1, 57)

# part2
while True:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y, z, 38, 7)
