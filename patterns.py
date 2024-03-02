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
                    # Check number in that row,grid,block
                    if(Check_row(grid, i, x) and
                       Check_column(grid, j, x) and
                       Check_square(grid, i, j, x)):
                        # check if the number is unique in its block
                        if check_block_row_columns(grid, i, j, x):
                            print("Unique candidate found at position ({}, {}): {}".format(i, j, x))

    return False

# Check if the number is unique in its row and block columns
def check_block_row_columns(grid, row, col, x):
    current_row = 3 * math.floor(row / 3)
    current_column = 3 * math.floor(col / 3)
    for i in range(current_row, current_row + 3):
        for j in range(current_column, current_column + 3):
            # not checking current row/column
            if (i != row or j != col) and grid[i][j] == 0:
                # check possible candidates x
                if x in get_possible_numbers(grid, i, j):
                    return False
    return True

# Function to get the possible numbers we could have in the row and columns
def get_possible_numbers(grid, row, col):
    numbers = list(range(1, 10))
    for i in range(9):
        if grid[row][i] in numbers:
            # remove numbers in that row
            numbers.remove(grid[row][i])  
        if grid[i][col] in numbers:
            #remove numbers in that column
            numbers.remove(grid[i][col])  
    # return list of possible numbers
    return numbers

# Function to find a number within a specific row or column
def BRC_interaction(grid):
    # Check each number
    for number in range(1,10):
        # iterate over each block
        for i in range(3):
            for j in range(3):
                # list of amount of a certain number
                row = []
                column = []
                # iterate over cells in the block
                for a in range(3):
                    for b in range(3):
                        # get current row and column
                        current_row = i * 3 + a
                        current_col = j * 3 + b
                        # Check if the cell is empty and if the number can be placed in it
                        if grid[current_row][current_col] == 0 and number in get_possible_numbers(grid, current_row, current_col):
                            row.append(current_row)
                            column.append(current_col)
                # Check if we have 1 instance of that number in the column/row
                if len(row) == 1:
                    print(f"Number {number} is unique in row {row.pop()} within block ({i}, {j})")
                if len(column) == 1:
                    print(f"Number {number} is unique in column {column.pop()} within  block ({i}, {j})")
        
                
    return False


def block_block_interaction(grid):
    # Looping through each block
    for row_block in range(3):
        for col_block in range(3):
            # iterate over all the numbers
            for number in range (1,10):
                # setting count per cell and elimated cells as empty
                possible_numbers = 0
                elimated_cells = []
                #iterate over each cell in the block
                for i in range(3):
                    for j in range(3):
                        # get current row and column
                        row = row_block*3+i
                        column = col_block*3+j
                        # if grid is empty and we are the middle and middle left blocks
                        if grid[row][column] == 0 and ((row//3,column//3)==(1,0) or (row//3,column//3)==(1,1)):
                            # if number exists in that column
                            if number in [grid[a][column] for a in range(3)]:
                                # add possible number and cell to elimate
                                possible_numbers+=1
                                elimated_cells.append((row,column))
                # if we have a number to eliminate from a set of cells
                if possible_numbers >0:
                    print("Elimate",number,"from cells:",elimated_cells)

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