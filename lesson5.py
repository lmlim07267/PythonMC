# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:57:00 2022

@author: ben72
"""
from mcpi.minecraft import Minecraft
import random
while True:
    mc = Minecraft.create()
    x, y, z = mc.player.getTilePos()
    if mc.getBlock(x, y-1, z) == 12:
        ID = random.choice([0, 81])
        mc.setBlock(x, y, z, ID)
    else:
        ID=random.randint(0, 8)
        mc.setBlocks(x, y-1, z, x+4, y-1, z+4, 38, ID)