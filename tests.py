# Document for the unit tests


#imports
from patterns import *
from puzzle_generator import *
from grader import *

# test puzzle generates correctly
def TEST_generate_puzzle(grid):
    # test that we dont have duplicate numbers
    # test solution is unique
    return True

# test for a correct sole candidate
def TEST_sole_technique(grid):
    # test for a sole technique in the set grid
    return True

# test for a correct unique candidate
def TEST_unique_candidate(grid):
    return True

# test for a BRC_interaction
def TEST_brc_interaction(grid):
    return True

# test for a naked subset
def TEST_naked_subset(grid):
    return True

# Test for a hidden subset
def TEST_hidden_subset(grid):
    return True

# test for a X_Wing 
def TEST_x_wing(grid):
    return True

# test for a swordfish
def TEST_swordfish(grid):
    return True

# test for a forcing chain
def TEST_forcing_chain(grid):
    return True

# test for a XY_Wing
def TEST_xy_wing(grid):
    return True

# test for a unique rectangle
def TEST_unique_rectangle(grid):
    return True

# test the grader returns the correct score
def TEST_grader(score):
    return True

if __name__ == '__main__':
    #generate puzzle
    grid = Generate_puzzle()

    #genrate pattern search
    sole_technique,unique_candidate,BRC_interaction,block_block_interaction,naked_subset,hidden_subset,X_wing,swordfish,forcing_chain,XY_wing,unique_rectangle = patterns(grid)
    # run grader
    grader(sole_technique,unique_candidate,BRC_interaction,block_block_interaction,naked_subset,hidden_subset,X_wing,swordfish,forcing_chain,XY_wing,unique_rectangle)

    # run all test
    count = 0       # variable to count number of correct test

    if TEST_generate_puzzle(grid): count+=1
    if TEST_sole_technique(grid): count+=1
    if TEST_unique_candidate(grid): count+=1
    if TEST_brc_interaction(grid): count+=1
    if TEST_naked_subset(grid): count+=1
    if TEST_hidden_subset(grid): count+=1
    if TEST_x_wing(grid): count+=1
    if TEST_swordfish(grid): count+=1
    if TEST_forcing_chain(grid): count+=1
    if TEST_xy_wing(grid): count+=1
    if TEST_unique_rectangle(grid): count+=1
    if TEST_grader(grid): count+=1

    #check all tests return TRUE
    if count != 12:
        print("One of the test failed. Please see above for more detail.")

    else:
        print("All",count,"tests ran correctly!")