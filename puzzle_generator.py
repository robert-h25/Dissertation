# Sudoku Puzzle Generator
# Student ID: sc21rh
# Student Name: Robert Helps

import math
import numpy
import random

# Print the current grid
def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])
    print("\n")

# Generate an empty grid
def Generate_puzzle():
    #generate an empty (0) 9x9 grid
    grid = [[0] * 9 for _ in range(9)]
    for i in range(0,9):
        for j in range(0,9):
            grid[i][j] = 0

    
    # fill the grid with values 
    Solve_puzzle(grid)
    print_grid(grid)
    # Remove squares to create a valid puzzle
    grid = Create_holes(grid)
    print_grid(grid)
    return grid

# Solve the puzzle recursively
# Takes parameter grid (current grid)
def Solve_puzzle(grid):
    #find an empty cell in the grid
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                # Try to fill the cell with a number

                # Create list of numbers and randomly choice an index until one works
                numbers = random.sample(range(1, 10), 9)
                for number in numbers:
                    
                    # Check row, column and grid to make sure number can be there
                    if(Check_row(grid, row, number) and Check_column(grid, column, number) 
                    and Check_square(grid, row, column, number) ):
                        
                        grid[row][column] = number
                        #print_grid(grid)
                        #recursively attempt to fill the rest of the grid
                        if(Solve_puzzle(grid)):
                            return True
                        # no possibility to fill the rest of the grid
                        
                        # reset cell to 0
                        grid[row][column]=0
                return False
    #no more empty cells, puzzle is filled
    return True

# Remove certain cells to create a vaid puzzle
def Create_holes(grid):
    # check if we can take the cells recursively to create an unique solution
    
    # Create puzzle with between 17 and 40 numbers left
    lower_bound = 17
    upper_bound = 40
    target_holes = random.randint(lower_bound,upper_bound)
    holes = 0
    while 81-holes > target_holes:
        #remove number from random row, column
        row = random.randint(0,8)
        column = random.randint(0,8)
        grid[row][column] = 0
        print(holes)
        holes = holes + 1
        #check we have unique solution
        

    return grid

# Check if the number is in the row
# Takes parameters: grid, row and number
def Check_row(grid, row, number):
    #Check grid[row] to see if number is in it
    for i in range(9):
        if grid[row][i] == number:
            return False

    #return true if not in the row
    return True

# Check if the number is in the column
# Takes parameters: grid, column and number
def Check_column(grid, column, number):
    #Check grid[][column] to see if number is in it
    for i in range(9):
        if grid[i][column] == number:
            return False

    #return true if not in the column
    return True

# Check if number is in the 3x3 square
# Takes parameters: grid, row, column and number
def Check_square(grid, row, column, number):
    # Get current square
    current_row = 3 * math.floor(row / 3)
    current_column = 3 * math.floor(column / 3)
    # Search square for number
    for i in range(current_row, current_row + 3):
        for j in range(current_column, current_column + 3):
            if grid[i][j] == number:
                return False
    #return true if not in the square
    return True


if __name__ == "__main__":
    Generate_puzzle()