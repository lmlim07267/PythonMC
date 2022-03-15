# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:01:50 2022

@author: ben72
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#part1
# while True:
#     hits = mc.events.pollBlockHits()
#     if len(hits) > 0:
#        hit =  hits[0]  
#        x, y, z = hit.pos.x,hit.pos.y, hit.pos.z
#        Block =  mc.getBlock( x, y, z)
#        mc.postToChat('你會被鐵砧壓死' + str(Block))
       
#part2

# while True:
#     hits = mc.events.pollBlockHits()
#     if len(hits) > 0:
#         hit =  hits[0]  
#         x, y, z = hit.pos.x,hit.pos.y, hit.pos.z

#part3
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit =  hits[0]  
        x, y, z = hit.pos.x,hit.pos.y, hit.pos.z
        mc.createExplosion(x, y, z)
    
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit =  hits[0]  
        x, y, z = hit.pos.x,hit.pos.y, hit.pos.z
        mc.createExplosion(x, y, z)