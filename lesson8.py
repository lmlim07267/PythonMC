# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:16:46 2022

@author: ben72
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def PlantTree(x, y, z):
    mc.setBlocks(x-1, y+3, z-1, x+1, y+5, z+1, 46)
    mc.setBlocks(x, y, z, x, y+4, z, 17)
    
#part1
# x, y, z = mc.player.getTilePos()
# PlantTree(x, y, z)

#part2
# x, y, z = mc.player.getTilePos()
# for i in range(20):
#     PlantTree(x+5*i, y, z)

#part3
x, y, z = mc.player.getTilePos()
for i in range(20):
    for tnt in range(20):
            PlantTree(x+5*i, y, z+5*tnt)