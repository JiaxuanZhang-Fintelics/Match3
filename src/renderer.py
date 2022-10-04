# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:04:18 2022

@author: vitto
"""
import map
def render(Map):
    for i in range(map.row):
        print(Map.map[i*map.col:(i+1)*map.col])
        
def displayScore(Map):
    print(Map.score)
    
def main():
    m=map.Map()
    print("initial:")
    render(m)
    while(m.reduce()):
        print("reduce:")
        render(m)
    

if __name__ == "__main__":
    main()