# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:57:02 2022

@author: vitto
"""

import random 

col=5 # number of columns
row=5 # number of rows
objs=4 # number of kinds of objects in grid 


class Map:
    
    # Constructor, generate random int in every grid and reduce
    def __init__(self):
        # Initialization
        self.score=0
        self.map=[]
        # Generate random int in grids
        for i in range(col*row):
            self.map.append(random.randint(1,objs))
        # Reduce
        self.reduce_all()
        # Reset score
        self.score=0
            
    # fill index with random number
    def fill(self,index):
        self.map[index]=random.randint(1,objs)
        
    # use the value above to cover value in index recursively 
    def remove(self,index):
        if(index<col):
            self.fill(index)
            return
        self.map[index]=self.map[index-col]
        self.remove(index-col)
        
    
    def reduce(self):
        # from top left to right
        for i in range(row*col):
            # check left
            if ((i%row)<col-2 
                and self.map[i+1]==self.map[i] 
                and self.map[i+2]==self.map[i]):
                self.remove(i)
                self.remove(i+1)
                self.remove(i+2)
                self.score+=1
                return True
            # check down
            if(i<(row-2)*col 
               and self.map[i+col]==self.map[i] 
               and self.map[i+2*col]==self.map[i]):
                self.remove(i)
                self.remove(i+col)
                self.remove(i+2*col)
                self.score+=1
                return True
        return False
    
    # keep reducing untill no match objects exist
    def reduce_all(self):
        while(self.reduce()):
            pass

            
            