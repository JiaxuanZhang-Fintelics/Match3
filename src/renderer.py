# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:04:18 2022

@author: vitto
"""

# Just a simple function to print the map, can be replaced with animation later
def render(Map):
    for i in range(Map.row):
        print(Map.map[i*Map.col:(i+1)*Map.col])
   
# Just a simple function to print the score, can be replaced with animation later
def displayScore(Map):
    print(Map.score)
