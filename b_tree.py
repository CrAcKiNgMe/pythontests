# -*- coding: utf-8 -*-
#desc
#http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/
"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination). You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.

For example, in the following figure, what is the minimum cost path to (2, 2)?

1) Optimal Substructure
The path to reach (m, n) must be through one of the 3 cells: (m-1, n-1) or (m-1, n) or (m, n-1). So minimum cost to reach (m, n) can be written as “minimum of the 3 cells plus cost[m][n]”.

minCost(m, n) = min (minCost(m-1, n-1), minCost(m-1, n), minCost(m, n-1)) + cost[m][n]
"""

list = [ [1, 2, 3], [4, 8, 2], [1, 5, 3]]

"""
[1, 2, 3]
[4, 8, 2]
[1, 5, 3]
"""


def min(a, b, c):
    m = a
    if(a > b):
        m = b
    if(m > c):
        m = c
    return m




def minpath(matrix, m, n):

    if(m == 1 and n == 1):
        return matrix[0][0]
    if(m < 1 or n < 1):
        return 999999999999999999999999
    else:
        n =  min(minpath(matrix, m-1, n-1),minpath(matrix, m, n-1),minpath(matrix, m-1, n)) + matrix[m-1][n-1]

        return n


print minpath(list, 3 , 3)