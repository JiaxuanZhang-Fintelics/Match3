# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:38:07 2022

@author: vitto
"""

import map
from renderer import render

def flip(Map,i,j):
    temp=Map[i]
    Map[i]=Map[j]
    Map[j]=temp

def solve(Map):
    # start from top left
    for i in range(map.row*map.col):
        # flip to left
        if((i%map.row)>2
        and Map.map[i-2]==Map.map[i] 
        and Map.map[i-3]==Map.map[i]):
            flip(Map.map, i, i-1)
            print("left",int(i/map.row),i%map.row)
            return True
        # flip to right
        if((i%map.row)<map.col-3 
        and Map.map[i+2]==Map.map[i] 
        and Map.map[i+3]==Map.map[i]):
            flip(Map.map, i, i+1)
            print("right",int(i/map.row),i%map.row)
            return True
        # flip up
        if(i>2*map.col
        and Map.map[i-2*map.col]==Map.map[i] 
        and Map.map[i-3*map.col]==Map.map[i]):
            flip(Map.map, i, i-map.col)
            print("up",int(i/map.row),i%map.row)
            return True
        # flip down
        if(i<(map.row-3)*map.col
        and Map.map[i+2*map.col]==Map.map[i] 
        and Map.map[i+3*map.col]==Map.map[i]):
            flip(Map.map, i, i+map.col)
            print("down",int(i/map.row),i%map.row)
            return True
    return False

def main():
    m=map.Map()
    print("initial:")
    render(m)
    while(m.reduce()):
        print("reduce:")
        render(m)
    while(solve(m) and m.reduce()):
        print("solve:")
        render(m)
    

if __name__ == "__main__":
    main()