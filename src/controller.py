# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 09:47:38 2022

@author: vitto
"""
import map
import renderer
from solver import solve 

class controller:
    # initialize map
    def __init__(self,col=5,row=5,objs=4,pool_size=10,init_pool=[]):
        self.Map=None
        if(not (pool_size*objs<col*row and len(init_pool)<col*row)):
            self.Map=map.Map(col,row,objs,pool_size,init_pool)
    #  start solving
    def start(self):
        if(self.Map==None):
            print("Map generation error: pool_size*objs must larger than map size")
            return
        print("initial:")
        renderer.render(self.Map)
        while(self.Map.reduce()):
            print("reduce:")
            #renderer.render(self.Map)
        while(solve(self.Map)):
            print("solve:")
            #renderer.render(self.Map)
            while(self.Map.reduce()):
                print("reduce:")
                #renderer.render(self.Map)
        print("Score:")
        renderer.displayScore(self.Map)
        renderer.render(self.Map)

if __name__ == "__main__":
   c=controller(10,10,4,300)
   c.start()
   if(c.Map!=None):print("Remaining objec count:",c.Map.remain())