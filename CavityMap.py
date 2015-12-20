#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)

#print grid

for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        #print str(i)+","+str(j)
        if i >= 1 and i < len(grid)-1 and j >= 1 and j < len(grid[0])-1:
            if grid[i-1][j]<grid[i][j] and grid[i+1][j]<grid[i][j] and grid[i][j+1]<grid[i][j] and grid[i][j-1]<grid[i][j]:
                sys.stdout.write("X")
            else:
                sys.stdout.write(grid[i][j])
        else:
            sys.stdout.write(grid[i][j])
    print('')
