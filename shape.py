# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:59:27 2021

@author: ChiruvellaPoojitha
"""
#commented2
#time 12:17

class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculateArea(self):
        raise NotImplementedError('calculate area not implemented')
        
