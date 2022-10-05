# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:04:18 2022

@author: vitto
"""
import map
# Just a simple function to print the map, can be replaced with animation later
def render(Map):
    for i in range(map.row):
        print(Map.map[i*map.col:(i+1)*map.col])
   
# Just a simple function to print the score, can be replaced with animation later
def displayScore(Map):
    print(Map.score)
