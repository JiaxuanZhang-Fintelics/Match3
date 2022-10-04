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
        print(self.map)