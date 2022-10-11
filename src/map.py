# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:57:02 2022

@author: vitto
"""

import random 


# return true if 2 is better than 1
def compare_reduce(vlen1,hlen1,vlen2,hlen2):
    # both 1 and 2 are L or T shape
    if(vlen1>1 and hlen1>1 and 
        vlen2>1 and hlen2>1 and
        (vlen1+hlen1)<(vlen2+hlen2)):
        return True
    # only 2 is L or T shape
    elif(vlen2>1 and hlen2>1 and
          max(vlen1,hlen1)<(vlen2+hlen2)): 
        return True
    # only vertical or horizontal
    elif max(vlen1,hlen1) < max(vlen2,hlen2):
        return True
    return False

class Map:
    
    # Constructor, generate random int in every grid and reduce
    def __init__(self,col,row,objs,pool_size,init_pool,mode):
        
        # Initialization
        self.col=col # number of columns
        self.row=row # number of rows
        self.objs=objs # number of kinds of objects in grid 
        self.pool_size=pool_size # size of pool=pool_size*col*row*objs*3
        self.score=0
        self.obj_count=0
        self.pool=init_pool
        self.mode=mode
        # only set randomized pool if not specified
        if len(init_pool)==0:
            # generate objects in pool
            if(mode=="3"):
                for i in range(pool_size*3):
                    for j in range(objs):
                        self.pool.append(j+1)
            if(mode=="random"):
                for i in range(pool_size*3*objs):
                    self.pool.append(random.randint(1, objs))
            # randomize the pool
            random.shuffle(self.pool)
        
        self.map=[]
        # Generate random int in grids from pool
        for i in range(col*row):
            self.map.append(self.pool.pop(0))
                
        # Reduce
        self.reduce_and_fill_pool()
        # Fill the pool and reset score
        self.score=0
            
    # fill index with object in the pool
    def fill(self,index):
        if(len(self.pool)==0):
            self.map[index]=0
        else:
            self.map[index]=self.pool.pop(0)
        self.score+=1
        
    # use the value above to cover value in index recursively 
    def remove(self,index):
        if(index<self.col):
            self.fill(index)
            return
        self.map[index]=self.map[index-self.col]
        self.remove(index-self.col)
    
    # find_direction functions are modified recursive dfs that only find 
    # consective objects in one direction
    def find_up(self,i,v):
        if (i<0): return # out of bound
        if(i>self.col*self.row): return # out of bound
        if(self.map[i]==0): return # empty grid
        #find up
        if(i>=self.col and self.map[i]==self.map[i-self.col]):
           v.append(i-self.col)
           self.find_up(i-self.col,v)
        
    def find_down(self,i,v):
        if (i<0): return # out of bound
        if(i>self.col*self.row): return # out of bound
        if(self.map[i]==0): return # empty grid
        #find down
        if(i/self.col<(self.row-1) and self.map[i]==self.map[i+self.col]):
           v.append(i+self.col)
           self.find_down(i+self.col,v)

    def find_left(self,i,h):
        if (i<0): return # out of bound
        if(i>self.col*self.row): return # out of bound
        if(self.map[i]==0): return # empty grid
        #find left
        if(i%self.col>0 and self.map[i]==self.map[i-1]):
           h.append(i-1)
           self.find_left(i-1,h)
         
    def find_right(self,i,h):
        if (i<0): return # out of bound
        if(i>self.col*self.row): return # out of bound
        if(self.map[i]==0): return # empty grid
        #find right
        if(i%self.col<self.col-1 and self.map[i]==self.map[i+1]):
           h.append(i+1)
           self.find_right(i+1,h)
    
    # find consecutive objects in four directions
    def find_around(self,i,v,h):
        self.find_up(i,v)
        self.find_down(i,v)
        self.find_left(i,h)
        self.find_right(i,h)
        
    # reduce consecutive objects around i, including i
    def reduce_around(self,i,v,h):
        reduced=False
        if(len(h)>1):
            for index in h:
                self.remove(index)
            reduced=True
            if(len(v)<2): 
                self.remove(i)
        if(len(v)>1):
            v.append(i)
            v.sort()
            for index in v:
                self.remove(index)
            reduced=True   

        return reduced

    # for each gird, find consecutive objects and compare, then reduce the best
    def reduce(self):
        max_index=0  
        # from top left to right
        vmax=[]
        hmax=[]
        for i in range(self.row*self.col):
            v=[]
            h=[]
            self.find_around(i,v,h)
            if compare_reduce(len(vmax),len(hmax),len(v),len(h)):
                max_index=i
                vmax=v
                hmax=h
        return self.reduce_around(max_index,vmax,hmax)
    
    # keep reducing untill no match objects exist
    def reduce_and_fill_pool(self):
        while(self.reduce()):
            if(self.mode=="3"):
                for j in range(self.score):
                    self.pool.append(self.obj_count%3+1)
                    self.obj_count+=1
                random.shuffle(self.pool)
            if(self.mode=="random"):
                for j in range(self.score):
                    self.pool.append(random.randint(1, self.objs))
            self.score=0
        
    # count not empty gird
    def remain(self):
        count=0
        for i in range(self.col*self.row):
            if self.map[i]!=0:
                count+=1
        return count

            
            