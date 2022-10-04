# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:04:18 2022

@author: vitto
"""
import map
def render(Map):
    for i in range(map.row):
        print(Map.map[i*map.col:(i+1)*map.col],'\n')
        
def displayScore(Map):
    print(Map.score)