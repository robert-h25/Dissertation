from puzzle_generator import *
import math

# Functions which find certain patterns in a Sudoku puzzle

# Find a sole candidate
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

# Find unique candidates
def unique_candidate(grid):
    # search grid for an empty cell
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                # search through every number
                for x in range(1,10):
                    # List of numbers that could go in that cell
                    numbers = []
                    # Check number in that row,grid,block
                    if(Check_row(grid, i, x) and
                       Check_column(grid, j, x) and
                       Check_square(grid, i, j, x)):
                        # Check all other rows and column in that block if a number could go there
                        current_row = 3 * math.floor(i / 3)
                        current_column = 3 * math.floor(j / 3)
                        for a in range(current_row,current_row+3):
                            # number in that blocks row
                            if(x in grid[a]):
                                numbers.append(x)
                        for b in range(current_column,current_column+3):
                            for row in range(9):
                                # number in that blocks column
                                if grid[row][b] == x:     
                                    numbers.append(x)
                # if we have a unique candidate
                if len(numbers) == 1:
                    print("Unique candidate found at position ({}, {}): {}".format(i, j, x))

                        

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