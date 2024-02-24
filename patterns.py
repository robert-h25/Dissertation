from puzzle_generator import *

# Functions which find certain patterns in a Sudoku puzzle

def sole_technique(grid):
    # Search each cell in the grid
    for i in range(9):
        for j in range(9):
            # Empty square
            if grid[i][j] == 0:
            # Check which number con go in that cells row,column and block
                # Check all numbers
                numbers = []
                for x in range(1,10):
                    if(Check_row(grid, i, x) and
                       Check_column(grid, j, x) and 
                       Check_square(grid, i, j, x)):
                        # if not in row, col and block
                        numbers.append(x)
                # if sole candidate flag that cell
                if len(numbers)==1:
                    print("sole candidate\n")
                    pass
            
    return False

def unique_candidate(grid):
    return False

def BRC_interaction(grid):
    return False

def block_block_interaction(grid):
    return False

def naked_subset(grid):
    return False

def hidden_subset(grid):
    return False

def X_wing(grid):
    return False

def swordfish(grid):
    return False

def forcing_chain(grid):
    return False

def XY_wing(grid):
    return False

def unique_rectangle(grid):
    return False

# Function to run through all the patterns
def patterns(grid):
    sole_technique(grid)
    unique_candidate(grid)
    BRC_interaction(grid)
    block_block_interaction(grid)
    naked_subset(grid)
    hidden_subset(grid)
    X_wing(grid)
    swordfish(grid)
    forcing_chain(grid)
    XY_wing(grid)
    unique_rectangle(grid)