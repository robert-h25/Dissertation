# Sudoku Puzzle Generator
# Student ID: sc21rh
# Student Name: Robert Helps

# Generate an empty grid
def Generate_puzzle():
    #generate an empty (0) 9x9 grid
    grid = []
    # fill the grid with values 
    Solve_puzzle(grid)

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

                #recursively attempt to fill the rest of the grid
                if(Solve_puzzle(grid)):
                    return True
                # no possibility to fill the rest of the grid
                else:
                    # reset cell to 0
                    grid[row][column]=0

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

    #return false if not in the row
    return False

# Check if the number is in the column
# Takes parameters: grid, column and number
def Check_column(grid, column, number):
    #Check grid[][column] to see if number is in it

    #return false if not in the column
    return False

# Check if number is in the 3x3 square
# Takes parameters: grid, row, column and number
def Check_square(grid, row, column, number):
    # Get current square

    # check if number is in that square

    #return false if not in the square
    return False

