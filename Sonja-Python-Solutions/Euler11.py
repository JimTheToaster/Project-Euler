def getgrid(gridfile):
    grid = [[int(i) for i in line.split()] for line in open(gridfile, "r")]
    return grid

def rows_and_cols(grid): 
    largest_product = 0
    for i in range(len(grid)):
        for j in range(len(grid)-4):
            product = 1
            for index in range(0, 4):
                product = product * grid[i][j+index]
                if product > largest_product: 
                    largest_product = product
            product = 1
            for index in range(0, 4):
                product = product * grid[j+index][i]
                if product > largest_product: 
                    largest_product = product
    return largest_product

def diags(grid):
    largest_product = 0
    for i in range(len(grid)-4):
        for j in range(len(grid)-4):
            product = 1
            for index in range(0, 4):
                product = product * grid[i+index][j+index]
                if product > largest_product: 
                    largest_product = product
        for i in range(3,len(grid)):
            for j in range(len(grid)-4):
                product = 1
                for index in range(0, 4):
                    product = product * grid[i-index][j+index]
                    if product > largest_product: 
                        largest_product = product
    return largest_product

def compare(x, y):
    if x>y:
        return x
    return y

file = getgrid("grid.txt")

print compare(rows_and_cols(file), diags(file))
