# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:57:02 2022

@author: vitto
"""

import random 

col=5
row=5
objs=4

class Map:
    def __init__(self):
        self.score=0
        self.map=[]
        for i in range(col*row):
            self.map.append(random.randint(1,objs))
            
    # fill index with random number
    def fill(self,index):
        self.map[index]=random.randint(1,objs)
        
    # use the value above to cover value in index  
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
    
    def reduce_all(self):
        while(self.reduce()):
            print("reduce:")
        return True

            
            