# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:22:38 2022

@author: ben72
"""


from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

#part1
# print(mc.player.getTilePos())
# print(mc.player.getPos())

#part2
# mc.player.setTilePos(123.99, 23.5555, 123.456)

#prat3
# time.sleep(10)
# x, y, z = mc.player.getTilePos()
# mc.setBlock(x, y, z, 213)
# mc.setBlock(x, y+1, z, 213)
# mc.setBlock(x, y+2, z, 213)
# mc.setBlock(x, y+3, z, 213)
# mc.setBlock(x, y+4, z, 213)
# mc.setBlock(x, y+5, z, 213)
# mc.setBlock(x, y+6, z, 213)
# mc.setBlock(x, y+7, z, 213)
# mc.setBlock(x, y+8, z, 213)
# mc.setBlock(x, y+9, z, 213)
# mc.setBlock(x, y+10, z, 213)
# mc.setBlock(x, y+11, z, 213)
# mc.setBlock(x, y+12, z, 213)

#part4
# x, y, z = mc.player.getTilePos()
# mc.setBlocks(x, y, z, x+10, y+20, z+10, 213)

#part5
# while True:
#     x, y, z = mc.player.getTilePos()
#     mc.setBlocks(x-1, y, z+1, x+1, y, z-1, 213)
#     mc.setBlock(x, y, z, 11)

#part6 
x, y, z = mc.player.getTilePos()
mc.setBlocks(x, y, z, x+10, y+15, z+12, 133)
mc.setBlocks(x+1, y+1, z+1, x+9, y+14, z+11, 0)
