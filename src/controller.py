# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 09:47:38 2022

@author: vitto
"""
import map
import renderer
from solver import solve 

# generate map and start solving
def start(col,row,objs,pool):
    m=map.Map(col,row,objs,pool)
    print("initial:")
    renderer.render(m)
    while(m.reduce()):
        print("reduce:")
        #renderer.render(m)
    while(solve(m)):
        print("solve:")
        #renderer.render(m)
        while(m.reduce()):
            print("reduce:")
            #renderer.render(m)
    print("Score:")
    renderer.displayScore(m)
    renderer.render(m)

if __name__ == "__main__":
    start(10,10,4,10)