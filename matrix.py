#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from copy import deepcopy

class Matrix():

    def __init__(self, *args):
        if len(args) == 4:
            self.coordinates_vector = []
            self.coordinates_vector = [(0,0),(0,1),(1,0),(1,1)]
            self.rows = []
            self.rows.append([args[0], args[1]])
            self.rows.append([args[2], args[3]])
        else:
            sys.exit('Error: ¡For each matrix nº of arguments should be 4!')
           
    def __add__(self, op1):
        if type(op1) == type(self):  # Matrix + Matrix
            result = deepcopy(self)
            for tuple in self.coordinates_vector:
                result.rows[tuple[0]][tuple[1]] += op1.rows[tuple[0]][tuple[1]]
            
            return result  
        elif type(op1) == int or type(op1) ==  float:  # Matrix + Scalar 
            result = deepcopy(self)
            
    def mult(self, m1, m2):
        return m1 * m2
              
    def __str__(self):
        matrix_str = '|'
        i = 0
        for tuple in self.coordinates_vector:
            if tuple[0] == 0:
                matrix_str += str(self.rows[tuple[0]][tuple[1]])
            elif i == 0:
                matrix_str += '|\n|'+ str(self.rows[tuple[0]][tuple[1]])
                i = 1
            elif i == 1:
                matrix_str += str(self.rows[tuple[0]][tuple[1]]) + '|\n'
                
        return matrix_str



        
