# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:38:07 2022

@author: vitto
"""
import map

# change objects in grid i and j 
def swap(Map,i,j):
    if(Map.map[i]==0 or Map.map[j]==0):
        return 
    temp=Map.map[i]
    Map.map[i]=Map.map[j]
    Map.map[j]=temp



# for each grid, swap the objects with adjacent objects and find the best swap
def solve(Map):
    vmax=[]
    hmax=[]
    max_index=0
    max_swap=0
    # start from top left
    for i in range(Map.row*Map.col):
        # swap to left
        if(i%Map.col>0):
           swap(Map,i,i-1) 
           if(Map.map[i]!=0):
               v=[]
               h=[]
               Map.find_around(i,v,h)
               if(map.compare_reduce(len(vmax),len(hmax),len(v),len(h))):
                   vmax=v
                   hmax=h
                   max_index=i
                   max_swap=i-1
           swap(Map,i,i-1) 
           
        #swap to right
        if(i%Map.col<(Map.col-1)):
            swap(Map,i,i+1) 
            if(Map.map[i]!=0):
               v=[]
               h=[]
               Map.find_around(i+1,v,h)
               if(map.compare_reduce(len(vmax),len(hmax),len(v),len(h))):
                   vmax=v
                   hmax=h
                   max_index=i
                   max_swap=i+1
            swap(Map,i,i+1) 
            
        #swap up
        if(i>Map.col):
            swap(Map,i,i-Map.col) 
            if(Map.map[i]!=0):
                v=[]
                h=[]
                Map.find_around(i-Map.col,v,h)
                if(map.compare_reduce(len(vmax),len(hmax),len(v),len(h))):
                    vmax=v
                    hmax=h
                    max_index=i
                    max_swap=i-Map.col
            swap(Map,i,i-Map.col) 
            
        #swap down
        if(i<(Map.row-1)*Map.col):
            swap(Map,i,i+Map.col) 
            if(Map.map[i]!=0):
                v=[]
                h=[]
                Map.find_around(i+Map.col,v,h)
                if(map.compare_reduce(len(vmax),len(hmax),len(v),len(h))):
                    vmax=v
                    hmax=h
                    max_index=i
                    max_swap=i+Map.col
            swap(Map,i,i+Map.col)

    if(len(vmax)>1 or len(hmax)>1):
        swap(Map,max_index,max_swap)
        return True

    return False
