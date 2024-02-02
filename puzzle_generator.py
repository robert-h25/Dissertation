# Sudoku Puzzle Generator
# Student ID: sc21rh
# Student Name: Robert Helps

import numpy
import random

# Print the current grid
def print_grid(grid):
    print(grid)


# Generate an empty grid
def Generate_puzzle():
    #generate an empty (0) 9x9 grid
    grid = [[0] * 9 for _ in range(9)]
    for i in range(0,9):
        for j in range(0,9):
            grid[i][j] = 0

    
    # fill the grid with values 
    Solve_puzzle(grid)
    #print_grid(grid)
    # Remove squares to create a valid puzzle

    return 1

# Solve the puzzle recursively
# Takes parameter grid (current grid)
def Solve_puzzle(grid):
    #find an empty cell in the grid
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                # Try to fill the cell with a number

                # Create list of numbers and randomly choice an index until one works
                for number in range (1,10):

                    #number = random.randint(1,9)
                    #print(number)
                    
                    # Check row, column and grid to make sure number can be there
                    if(Check_row(grid, row, number) == False or Check_column(grid, column, number) == False 
                    or Check_square(grid, row, column, number) == False):
                        
                        grid[row][column] = number
                        print_grid(grid)
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
def Create_holes():
    # check if we can take the cells recursively to create an unique solution

    return 1

# Check if the number is in the row
# Takes parameters: grid, row and number
def Check_row(grid, row, number):
    #Check grid[row] to see if number is in it
    for i in range(9):
        print("twst")
        if grid[row][i] == number:
            print("here")
            return True

    #return false if not in the row
    return False

# Check if the number is in the column
# Takes parameters: grid, column and number
def Check_column(grid, column, number):
    #Check grid[][column] to see if number is in it
    for i in range(9):
        if grid[i][column] == number:
            return True
        
    #return false if not in the column
    return False

# Check if number is in the 3x3 square
# Takes parameters: grid, row, column and number
def Check_square(grid, row, column, number):
    # Get current square
    current_row = row%3 
    current_column = column%3 
    for i in range(3):
        for j in range(3):
            
            if grid[current_row+i][current_column+j] == number:
                return True
            
    # check if number is in that square

    #return false if not in the square
    return False

if __name__ == "__main__":
    Generate_puzzle()