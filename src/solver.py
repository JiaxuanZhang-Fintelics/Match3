# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:38:07 2022

@author: vitto
"""

import map

# change objects in grid i and j 
def flip(Map,i,j):
    temp=Map.map[i]
    Map.map[i]=Map.map[j]
    Map.map[j]=temp

# check if there are 3 adjacent objects around i
def isSolved(Map, i):
    
    # avoid out of bound
    if i<0 or i>map.col*map.row:
        return False
    
    # case 1: two blocks left
    if((i%map.col>1)
       and Map.map[i-1]==Map.map[i] 
       and Map.map[i-2]==Map.map[i]):
        return True
    
    # case 2: two blocks right
    if((i%map.col)<map.col-2 
       and Map.map[i+1]==Map.map[i] 
       and Map.map[i+2]==Map.map[i]):
        return True
    
    # case 3: 1 left 1 right
    if(0<(i%map.col)<map.col-1 
       and Map.map[i-1]==Map.map[i] 
       and Map.map[i+1]==Map.map[i]):
        return True
    
    # case 4: 2 blocks up
    if(i>=2*map.col
       and Map.map[i-map.col]==Map.map[i] 
       and Map.map[i-2*map.col]==Map.map[i]):
        return True
    
    # case 5: 2 blocks down
    if(i<(map.row-2)*map.col
       and Map.map[i+1*map.col]==Map.map[i] 
       and Map.map[i+2*map.col]==Map.map[i]):
        return True
    
    # case 6: 1 up 1 down
    if(map.col<=i<(map.row-1)*map.col
       and Map.map[i-1*map.col]==Map.map[i] 
       and Map.map[i+1*map.col]==Map.map[i]):
        return True

    return False

# for each grid, flip the objects with adjacent grids and check whether it is solved
def solve(Map):
    
    # start from top left
    for i in range(map.row*map.col):
        
        # flip to left
        if(i%map.col>0):
           flip(Map,i,i-1) 
           if(isSolved(Map, i)):
               print("left",int(i/map.col),i%map.col)
               return True
           # if not solve, reset flip
           flip(Map,i,i-1) 
           
        #flip to right
        if(i%map.col<(map.col-1)):
            flip(Map,i,i+1) 
            if(isSolved(Map, i)):
                print("right",int(i/map.col),i%map.col)
                return True
            # if not solve, reset flip
            flip(Map,i,i+1) 
            
        #flip up
        if(i>map.col):
            flip(Map,i,i-map.col) 
            if(isSolved(Map, i)):
                print("up",int(i/map.col),i%map.col)
                return True
            # if not solve, reset flip
            flip(Map,i,i-map.col) 
            
        #flip down
        if(i<(map.row-1)*map.col):
            flip(Map,i,i+map.col) 
            if(isSolved(Map, i)):
                print("down",int(i/map.col),i%map.col)
                return True
            # if not solve, reset flip
            flip(Map,i,i+map.col) 
            
    return False
