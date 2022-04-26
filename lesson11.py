# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:17:10 2022

@author: Marcus
"""
import random
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

#part1


# for tnt in range(10):
#     x, y, z = mc.player.getTilePos()
#     x = x + tnt
#     for i in range(10):
#         r = random.randrange(0, 16)
#         z = z + 1
#         mc.setBlock(x, y, z, 35, r)

# part2
r =  random.randrange(0,16)
while True:
     hits = mc.events.pollBlockHits()
     if len(hits) > 0:
         hit = hits[0]
         block = mc.getBlockWithData(hit.pos)
         data = block.data
         mc.postToChat(str(data))