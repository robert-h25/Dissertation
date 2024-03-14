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
                        if grid[row][column] == 0 and ((math.floor(row / 3),math.floor(column / 3))==(1,0) or (math.floor(row / 3),math.floor(column / 3))==(1,1)):
                            # if number exists in that column
                            if number in [grid[a][column] for a in range(3)]:
                                # add possible number and cell to elimate
                                possible_numbers+=1
                                elimated_cells.append((row,column))
                # if we have a number to eliminate from a set of cells
                if possible_numbers >0:
                    print("Elimate",number,"from cells:",elimated_cells)

    return False



def get_candidates(grid):
    #create an empty 9x9 grid
    candidates = [[[]for _ in range(9)]for _ in range(9)]
    # scan grid for empty cells
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                # get candidates from row, column and block
                numbers = []
                for i in range(1,10):
                    if(Check_row(grid,row,i) and
                    Check_column(grid,column,i) and
                    Check_square(grid, row, column, i)):
                        numbers.append(i)
                candidates[row][column] = numbers
            #print(row,column,candidates[row][column])
                
    return candidates

def naked_subset(grid):
    # set naked subset list
    naked_subset = []
    # get candidate numbers for each cell
    candidates = get_candidates(grid)
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]):    
                count= 0
                subset = []
                # check row
                for a in range(9):
                    # if we have the same candidate subset
                    if candidates[i][j] == candidates[a][j] and i != a:
                        count +=1
                        subset.append(candidates[a][j])

                #check column
                for a in range(9):
                    # if we have the same candidate subset
                    if candidates[i][j] == candidates[i][a] and i != a:
                        count +=1
                        subset.append(candidates[i][a])

                #check block
                current_row = 3 * math.floor(i / 3)
                current_column = 3 * math.floor(j / 3)
                for a in range(current_row, current_row + 3):
                    for b in range(current_column, current_column + 3):
                        # if we have the same candidate subset
                        if candidates[i][j] == candidates[a][b] and i != a and j!=b:
                            count+=1
                            subset.append(candidates[a][b])
                                               
                # naked subset when we have same candidates 
                if (count > 1 and len(candidates[i][j]) == count):
                    naked_subset.append(subset)

    return naked_subset

def generate_pairs(candidate_for_cell):
    pairs = []
    for a in range(len(candidate_for_cell)):
        for b in range(a + 1, len(candidate_for_cell)):
            pairs.append((candidate_for_cell[a], candidate_for_cell[b]))
    return pairs

# Function to find hidden subsets in a row
def hidden_subset_row(grid,candidates):
    hidden_subset = []
    for i in range(9):
        # Keep track of pairs checked in that row
        checked_pairs = []    
        numbers_checked = []
        for j in range(9):
            # empty cell
            if grid[i][j] == 0:
                # get candidates for that cell
                candidate_for_cell = candidates[i][j]
                
                # Generate pairs
                pairs = generate_pairs(candidate_for_cell)

                # Check if a pair of numbers appears twice in row
                for pair in pairs:
                    # skip if checked before
                    if pair in checked_pairs: 
                        continue
                    #check all cells in that row
                    count = 0
                    for a in range(9):
                        if pair[0] in candidates[i][a] and pair[1] in candidates[i][a]:
                            count += 1
                    # if count is 2 we have a pair
                    if count == 2:
                        checked_pairs.append(pair)  
                
        # checking all pairs to see if we have a repeat number
        for pair in checked_pairs:
            if pair[0] not in numbers_checked and pair[1] not in numbers_checked:
                hidden_subset.append((i,pair))
                numbers_checked.append(pair[0])
                numbers_checked.append(pair[1])
    
    return hidden_subset

# Function to find hidden subsets in a column
def hidden_subset_column(grid,candidates):
    hidden_subset = []
    for i in range(9):
        # Keep track of pairs checked in that column
        checked_pairs = []      
        numbers_checked = []
        for j in range(9):
            # empty cell
            if grid[i][j] == 0:
                # get candidates for that cell
                candidate_for_cell = candidates[i][j]
                
                # Generate pairs
                pairs = generate_pairs(candidate_for_cell)

                # Check if a pair of numbers appears twice in coluumn
                for pair in pairs:
                    # skip if checked before
                    if pair in checked_pairs: 
                        continue
                    #check all cells in that coluumn
                    count = 0
                    for a in range(9):
                        if pair[0] in candidates[a][j] and pair[1] in candidates[a][j]:
                            count += 1
                    # if count is 2 we have a pair
                    if count == 2:
                        checked_pairs.append(pair)  
                
        # checking all pairs to see if we have a repeat number
        for pair in checked_pairs:
            if pair[0] not in numbers_checked and pair[1] not in numbers_checked:
                hidden_subset.append((i,pair))
                numbers_checked.append(pair[0])
                numbers_checked.append(pair[1])
    
    return hidden_subset

# Function to find hidden subsets in a block
def hidden_subset_block(grid, candidates):
    hidden_subset = []
    for block_row in range(3):
        for block_col in range(3):
            # Keep track of pairs checked in that block
            checked_pairs = []      
            numbers_checked = []
            for i in range(block_row * 3, (block_row + 1) * 3):
                for j in range(block_col * 3, (block_col + 1) * 3):
                    # empty cell
                    if grid[i][j] == 0:
                        # get candidates for that cell
                        candidate_for_cell = candidates[i][j]
                        
                        # Generate pairs
                        pairs = generate_pairs(candidate_for_cell)

                        # Check if a pair of numbers appears twice in the block
                        for pair in pairs:
                            # skip if checked before
                            if pair in checked_pairs: 
                                continue
                            #check all cells in that block
                            count = 0
                            for a in range(block_row * 3, (block_row + 1) * 3):
                                for b in range(block_col * 3, (block_col + 1) * 3):
                                    if pair[0] in candidates[a][b] and pair[1] in candidates[a][b]:
                                        count += 1
                            # if count is 2 we have a pair
                            if count == 2:
                                checked_pairs.append(pair)  
            
            # checking all pairs to see if we have a repeat number
            for pair in checked_pairs:
                if pair[0] not in numbers_checked and pair[1] not in numbers_checked:
                    hidden_subset.append(((block_row, block_col), pair))
                    numbers_checked.append(pair[0])
                    numbers_checked.append(pair[1])
    
    return hidden_subset

# Function to check hidden subsets in a grid
def hidden_subset(grid):
    # Get candidates for each cell
    candidates = get_candidates(grid)
    # Get hidden subset in the row
    hidden_subset_rows = hidden_subset_row(grid, candidates)
    for i, hidden_subset in hidden_subset_rows:
        print("Hidden subset found on row:", i, "Pair is:", hidden_subset)
    
    # Get hidden subset in column
    hidden_subset_columns = hidden_subset_column(grid, candidates)
    for i, hidden_subset in hidden_subset_columns:
        print("Hidden subset found on Column:", i, "Pair is:", hidden_subset)

    # Get hidden subset in column
    hidden_subset_blocks = hidden_subset_block(grid, candidates)
    for i, hidden_subset in hidden_subset_blocks:
        print("Hidden subset found in block:", i, "Pair is:", hidden_subset)
        
                                
# Function to check if a number appears twice in a row
def twice_in_row(candidates,row,number):
    count = 0
    for column in range(9):
        if number in candidates[row][column]:
            count += 1
            if count > 2:
                return False
    return count == 2

# Function to check if a number appears twice in a column
def twice_in_column(candidates,column,number):
    count = 0
    for row in range(9):
        if number in candidates[row][column]:
            count += 1
            if count > 2:
                return False
    return count == 2

#Function to check a set of coordinates to see if we can make a rectangle
def check_rectangle(coordinates):
    x_wings = []
    # loop through all 4 possible combination of coords
    for i in range(len(coordinates)):
            for j in range(i+1, len(coordinates)):
                for k in range(j+1, len(coordinates)):
                    for l in range(k+1, len(coordinates)):
                        # get first 2 values of the coordinate tuple
                        x_values = []
                        y_values = []
                        # ignore 3rd value
                        subset = [coordinates[i][:2], coordinates[j][:2], coordinates[k][:2], coordinates[l][:2]]
                        # add unique x and y values to subset
                        for coord in subset:
                            if coord[0] not in x_values:
                                x_values.append(coord[0])
                            if coord[1] not in y_values:
                                y_values.append(coord[1])
                        # if 2 unique x and y values we have a rectangle
                        if len(x_values) == 2 and len(y_values) == 2:
                            # append to x_wings array
                            set = []
                            for x in x_values:
                                for y in y_values:
                                    set.append((x, y))
                            x_wings.append(set)
    #return all x_wings found
    return x_wings

def X_wing(grid):
    # get candidates for each cell
    candidates = get_candidates(grid)
    x_wings_candidates = []
    for i in range(9):
        for j in range(9):
            if(grid[i][j]==0):
                for number in range(1,10):
                    # for each number check if it appears twice in that row or column
                    if number in candidates[i][j]:
                        if(twice_in_row(candidates,i,number) or (twice_in_column(candidates,j,number))):
                            # append to x_wing_candidates array
                            x_wings_candidates.append((i,j,number))

    # in x_wings_candidates array check if we have a rectangle with the same number
    x_wings = []     
    # get coordinates for each number       
    for number in range(1,10):
        coordinates = []
        # for each candidate check if it = a number
        for i in range(len(x_wings_candidates)):
            if x_wings_candidates[i][2] == number:
                coordinates.append(x_wings_candidates[i])
        #for the coordinate array check if we have a rectangle
        rectangles = check_rectangle(coordinates)
        # if we have a rectangle
        if len(rectangles)>0:
            for rectangle in rectangles:
                print("X-wing found with coordinates:",rectangle,"for number:",number)
            x_wings.append(rectangles)
        
                    
                   
    return False

# Function to check if a number appears twice in a column of coordinates
def number_twice_in_col(coordinates,number):
    col_counts = {}
    twice_col = []
    
    # Count occurrence of column value
    for coord in coordinates:
        col = coord[1]
        if coord[2] == number:
            col_counts[col] = col_counts.get(col, 0) + 1
    
    # if count==2 add to list
    for coord in coordinates:
        col = coord[1]
        if coord[2] == number and col_counts[col] == 2:
            twice_col.append(coord)
    
    return twice_col

# Function to check if a number appears twice in a row of coordinates
def number_twice_in_row(coordinates,number):
    row_counts = {}
    twice_row = []
    
    # Count occurrences of row value
    for coord in coordinates:
        row = coord[0]
        if coord[2] == number:
            row_counts[row] = row_counts.get(row, 0) + 1
    
    # add to list if count ==2
    for coord in coordinates:
        row = coord[0]
        if coord[2] == number and row_counts[row] == 2:
            twice_row.append(coord)
            
    return twice_row

# x wing on steroids in a 3x3 rectangle
def swordfish(grid):
    candidates = get_candidates(grid)
    corners = []

    # find a cell where one of the candidates only appears twice in that row/column
    for number in range(1, 10):
        # check row
        for i in range(9):
            # check if number appears 2 or 3 times in that row
            count = sum(1 for column in range(9) if number in candidates[i][column])
            if count == 2 or count == 3:
                #print(number, "appears", count, "times in row", i)
                # check if that number appears in another column
                # check if column contains at least 2 shared cells
                for j in range(9):
                    if number in candidates[i][j]:
                        # Store the coordinates of where that number appears
                        corners.append((i, j,number)) 

    # Check if a coodinate for a number connect to 1 row and 1 column
    for number in range(1,10):
        coords = []
        # check if a number appears twice in a row and column
        result = number_twice_in_row(corners,number)
        for coord in result:
            # add to coords list if not in there
            if(coord[0],coord[1])not in coords:
                coords.append((coord[0],coord[1]))
        result = number_twice_in_col(corners,number)
        for coord in result:
            # add to coords list if not in there
            if(coord[0],coord[1])not in coords:
                coords.append((coord[0],coord[1]))

        #check if we have swordfish if amount of col and row value == 3
        if len(coords) == 6:
            print("Swordfish occurs with coordinates:",coords,"for number:",number)                
                
    return False

def forcing_chain(grid):
    return False

def check_candidates(cell1, cell2, cell3):
    common_number_cell1_cell2 = [num for num in cell1 if num in cell2]
    common_number_cell2_cell3 = [num for num in cell2 if num in cell3]
    
    if len(common_number_cell1_cell2) == 1 and len(common_number_cell2_cell3) == 1:
        if common_number_cell1_cell2 != common_number_cell2_cell3:
            return True
    
    return False

def XY_wing(grid):
    candidates = get_candidates(grid)
    # list to hold matching candidates in cells
    matching_candidates = []
    # scan grid for cells with 2 candidates
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                # if candidates=2 scan block, column, row for another cell with 2 candidates
                if len(candidates[i][j])==2:
                    # check row
                    for a in range(9):
                        if len(candidates[a][j])== 2 and i != a:
                            # check if we have 1 common candidate
                            if ((candidates[i][j][0] in candidates[a][j]) ^ (candidates[i][j][1] in candidates[a][j])) and i != a:
                                #print(i,j,"match with",a,j ,"in row")
                                matching_candidates.append((i,j,a,j))
                            

                    # check column 
                    for a in range(9):
                        if len(candidates[i][a])== 2 and j != a:
                            # check if we have 1 common candidate
                            if ((candidates[i][j][0] in candidates[i][a]) ^ (candidates[i][j][1] in candidates[i][a])) and j != a:
                                #print(i,j,"match with",i,a ,"in column")
                                matching_candidates.append((i,j,i,a))

                    #check block
                    current_row = 3 * math.floor(i / 3)
                    current_column = 3 * math.floor(j / 3)
                    # Search square for number
                    for a in range(current_row, current_row + 3):
                        for b in range(current_column, current_column + 3):
                            if len(candidates[a][b])== 2 and i != a and j != b:
                                # check if we have 1 common candidate
                                if ((candidates[i][j][0] in candidates[a][b]) ^ (candidates[i][j][1] in candidates[a][b])) and i != a and j != b:
                                    #print(i,j,"match with",a,b ,"in block")
                                    matching_candidates.append((i,j,a,b))
    xy_wings = []
    # search matching_candidates for a third cell
    for cells in matching_candidates:
        i1,j1=cells[0],cells[1]
        i2,j2=cells[2],cells[3]
        # check for a third cell that intersects one of the cells
        for a in matching_candidates:
            if i2 == a[0] and j2 == a[1]:
                candidates_1 = candidates[i1][j1]
                candidates_2 = candidates[i2][j2]
                candidates_3 = candidates[a[2]][a[3]]
                # find which cell is the middle and which are the wings                
                if(check_candidates(candidates_1,candidates_2,candidates_3)):
                    if((i1!=i2) and (i2!=a[2]) and (i1!=a[2])) :
                        if ((j1!=j2) or (j2!=a[3]) or (j1!=a[3])):
                            #print("XY-wing found between cells: (",i1,j1,") (",i2,j2,") (",a[2],a[3],")")
                            xy_wings.append((i1,j1,i2,j2,a[2],a[3]))

    # Delete duplicates in reverse
    for xy_wing in xy_wings:
        for check_xy_wing in xy_wings:
            if (xy_wing != check_xy_wing):
                if(xy_wing[0]==check_xy_wing[4]and xy_wing[1]==check_xy_wing[5]and xy_wing[2]==check_xy_wing[3]):
                    xy_wings.remove(xy_wing)
    print(xy_wings)
    return False

def unique_rectangle(grid):
    # find an empty cell
    candidates = get_candidates(grid)
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                # get candidates for that cell
                candidate_for_cell = candidates[i][j]
                
                # Generate pairs
                pairs = generate_pairs(candidate_for_cell)

                # check row AND column if this pair occurs again
                for pair in pairs:
                    #check row
                    for a in range(9):
                        if len(candidates[a][j])> 2 and i != a:
                            if pair[0] in candidates[a][j] and pair[1] in candidates[a][j]:
                                # pair occurs again 
                                pass
                    for a in range(9):
                        if len(candidates[i][a])> 2 and j != a:
                            if pair[0] in candidates[i][a] and pair[1] in candidates[i][a]:
                                # pair occurs again
                                pass

    # if yes check these two cells have another cell with the pair
    # check if this cell intersects
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