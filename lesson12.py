# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:15:16 2022

@author: Marcus
"""

from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

#part1
# myId = mc.getPlayerEntityId('lmlim')
# print(myId)    
# mc.postToTitle(myId, "go die bro")

#part1
myId = mc.getPlayerEntityId('lmlim')
print(myId)    
mc.entity.setTilePos(myId, 100, 100, 100)