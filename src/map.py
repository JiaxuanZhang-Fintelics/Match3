# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:57:02 2022

@author: vitto
"""

import random 


class Map:
    
    # Constructor, generate random int in every grid and reduce
    def __init__(self,col=5,row=5,objs=4,pool=3):
        
        # Initialization
        self.col=col # number of columns
        self.row=row # number of rows
        self.objs=objs # number of kinds of objects in grid 
        self.pool_size=pool # size of pool=pool_size*col*row*objs*3
        self.score=0
        
        self.pool=[]
        # generate objects in pool
        for i in range(pool*row*col*3):
            for j in range(objs):
                self.pool.append(j+1)
        # randomize the pool
        random.shuffle(self.pool)
        
        self.map=[]
        # Generate random int in grids from pool
        for i in range(col*row):
            self.map.append(self.pool.pop(0))
        # Reduce
        self.reduce_all()
        # Reset score
        self.score=0
            
    # fill index with object in the pool
    def fill(self,index):
        if(len(self.pool)==0):
            self.map[index]=0
        else:
            self.map[index]=self.pool.pop(0)
        
    # use the value above to cover value in index recursively 
    def remove(self,index):
        if(index<self.col):
            self.fill(index)
            return
        self.map[index]=self.map[index-self.col]
        self.remove(index-self.col)
        
    
    def reduce(self):
        # from top left to right
        for i in range(self.row*self.col):
            # check left
            if ((i%self.col)<self.col-2
                and self.map[i]!=0
                and self.map[i+1]==self.map[i] 
                and self.map[i+2]==self.map[i]):
                self.remove(i)
                self.remove(i+1)
                self.remove(i+2)
                self.score+=1
                return True
            # check down
            if(i<(self.row-2)*self.col 
               and self.map[i]!=0
               and self.map[i+self.col]==self.map[i] 
               and self.map[i+2*self.col]==self.map[i]):
                self.remove(i)
                self.remove(i+self.col)
                self.remove(i+2*self.col)
                self.score+=1
                return True
        return False
    
    # keep reducing untill no match objects exist
    def reduce_all(self):
        while(self.reduce()):
            pass

            
            