import math
import random





def func(n, grid):
    row = int(input("enter number: "))
    col = int(input("enter number: "))
    if n ==1:
        return grid

    if n%2 == 0:
        return ['O'*col for i in range(row)]

    n//=2
    for q in range((n+1)%2 + 1):
        newgrid = [['O']*col for i in range(row)]
        def set(x, y ):
            if 0<=x<row and 0<=y<col:
                newgrid[x][y] = '.'

        xi = [0,0,0,1,-1]
        yi = [0,-1,1,0,0]


        for x in range(row):
            for y in range(col):
                if grid[x][y] == 'O':
                    for i,j in zip(xi,yi):
                        set(x+i,y+j)
                        

        grid = newgrid

        

    return ["".join(x) for x in grid ]


