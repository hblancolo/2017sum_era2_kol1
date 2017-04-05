#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Code by Héctor Blanco Lozano

from matrix import Matrix

matrix_1 = Matrix([[1, 1], [1, 1]])
matrix_2 = Matrix([[4, 1], [3, 1]])
print(matrix_2)

matrix_3 = matrix_1 + matrix_2
print(matrix_3)

matrix_4 = matrix_1 + 5
print(matrix_4)

matrix_5 = matrix_1 - matrix_2
print(matrix_3)

matrix_6 = matrix_1 - 5
print(matrix_4)

matrix_6 = matrix_1.prod(matrix_2)
print(matrix_6)

for v in matrix_2:
    print(v)
