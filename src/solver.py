# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:38:07 2022

@author: vitto
"""


# change objects in grid i and j 
def flip(Map,i,j):
    if(Map.map[i]==0 or Map.map[j]==0):
        return 
    temp=Map.map[i]
    Map.map[i]=Map.map[j]
    Map.map[j]=temp

# check if there are 3 adjacent objects around i
def isSolved(Map, i):
    
    # avoid out of bound
    if i<0 or i>Map.col*Map.row:
        return False
    if(Map.map[i]==0):
        return False
    # case 1: two blocks left
    if((i%Map.col>1)
       and Map.map[i-1]==Map.map[i] 
       and Map.map[i-2]==Map.map[i]):
        return True
    
    # case 2: two blocks right
    if((i%Map.col)<Map.col-2 
       and Map.map[i+1]==Map.map[i] 
       and Map.map[i+2]==Map.map[i]):
        return True
    
    # case 3: 1 left 1 right
    if(0<(i%Map.col)<Map.col-1 
       and Map.map[i-1]==Map.map[i] 
       and Map.map[i+1]==Map.map[i]):
        return True
    
    # case 4: 2 blocks up
    if(i>=2*Map.col
       and Map.map[i-Map.col]==Map.map[i] 
       and Map.map[i-2*Map.col]==Map.map[i]):
        return True
    
    # case 5: 2 blocks down
    if(i<(Map.row-2)*Map.col
       and Map.map[i+1*Map.col]==Map.map[i] 
       and Map.map[i+2*Map.col]==Map.map[i]):
        return True
    
    # case 6: 1 up 1 down
    if(Map.col<=i<(Map.row-1)*Map.col
       and Map.map[i-1*Map.col]==Map.map[i] 
       and Map.map[i+1*Map.col]==Map.map[i]):
        return True

    return False

# for each grid, flip the objects with adjacent grids and check whether it is solved
def solve(Map):
    
    # start from top left
    for i in range(Map.row*Map.col):
        
        # flip to left
        if(i%Map.col>0):
           flip(Map,i,i-1) 
           if(isSolved(Map, i)):
               print("left",int(i/Map.col),i%Map.col)
               return True
           # if not solve, reset flip
           flip(Map,i,i-1) 
           
        #flip to right
        if(i%Map.col<(Map.col-1)):
            flip(Map,i,i+1) 
            if(isSolved(Map, i)):
                print("right",int(i/Map.col),i%Map.col)
                return True
            # if not solve, reset flip
            flip(Map,i,i+1) 
            
        #flip up
        if(i>Map.col):
            flip(Map,i,i-Map.col) 
            if(isSolved(Map, i)):
                print("up",int(i/Map.col),i%Map.col)
                return True
            # if not solve, reset flip
            flip(Map,i,i-Map.col) 
            
        #flip down
        if(i<(Map.row-1)*Map.col):
            flip(Map,i,i+Map.col) 
            if(isSolved(Map, i)):
                print("down",int(i/Map.col),i%Map.col)
                return True
            # if not solve, reset flip
            flip(Map,i,i+Map.col) 
            
    return False
