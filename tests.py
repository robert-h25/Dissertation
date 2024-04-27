# Document for the unit tests


#imports
import time
import unittest

from run import app
from patterns import *
from puzzle_generator import *
from grader import *

# test puzzle generates correctly
def TEST_generate_puzzle():
    # test the puzzle generates
    grid = Generate_puzzle()

    # test solution is unique
    return True

def TEST_duplicate_numbers():
    grid = Generate_puzzle()
    print(grid)
    # check each number in grid to see if it appears in the same row, column and block
    for i in range(0,9):
        for j in range(0,9):
            #check col,row,block
            number = grid[i][j]
            if number == 0:
                pass
            else:
                if not (Check_row(grid, i, number) and Check_column(grid, j, number) 
                        and Check_square(grid, i, j, number) ):
                    pass
                else:
                    print("Failed duplicate number test")
                    return False

    print("Passed duplicate number test")
    return True

# test for a correct sole candidate
def TEST_sole_technique():
    # test for a sole technique in the set grid
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]

    if (1,5,9) in sole_technique(grid):
        print("Passed Sole Candidate test")
        return True
    else:
        print("FAILED Sole Candidate test")
        return False
    

# test for a correct unique candidate
def TEST_unique_candidate():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    if (0,3,8) in unique_candidate(grid):
        print("Passed Unique Candidate test")
        return True
    else:
        print("Failed Unique Candidate test")
        return False
    

# test for a BRC_interaction
def TEST_brc_interaction():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    
    if (1,4,1,0) in BRC_interaction(grid):
        print("Passed BRC_interaction test")
        return True
    else: 
        return False

# Test for a Block/Block interaction
def TEST_block_block_interaction():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    if (6,[(5,1)]) in block_block_interaction(grid):
        print("Passed Block/Block interaction test")
        return True
    else:
        print("Failed Block/Block interaction test")
        return False

# test for a naked subset
def TEST_naked_subset():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    if ([[3, 7], [3, 7]]) in naked_subset(grid):
        print("Passed naked subset test")
        return True
    else:
        print("Failed naked subset test")
        return False

# Test for a hidden subset
def TEST_hidden_subset():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    if (0, (3, 9)) in hidden_subset(grid):
        print("Passed Hidden Subset test")
        return True
    else:
        print("Failed Hidden Subset test")
        return False

# test for a X_Wing 
def TEST_x_wing():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    if [[(3, 6), (3, 8), (8, 6), (8, 8)]] in X_wing(grid):
        print("Passed X-Wing test")
        return True
    else:
        print("Failed X-Wing test")
        return False

# test for a swordfish
def TEST_swordfish():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    if ([(3, 2), (3, 6), (4, 0), (4, 2), (8, 0), (8, 2)], 6) in swordfish(grid):
        print("Passed swordfish test")
        return True
    else:
        print("Failed swordfish test")
        return False

# test for a forcing chain
def TEST_forcing_chain():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    if [(6, 7), (6, 5)] in forcing_chain(grid):
        print("Passed Forcing chain test")
        return True
    else:
        print("Failed Forcing chain test")
        return False

# test for a XY_Wing
def TEST_xy_wing():
    grid1 = [
    [2, 1, 0, 4, 0, 0, 0, 5, 9],
    [0, 0, 0, 0, 3, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 7, 0, 1],
    [5, 2, 1, 8, 0, 0, 0, 0, 0],
    [9, 0, 0, 7, 0, 2, 1, 0, 8],
    [3, 0, 7, 9, 0, 0, 5, 0, 6],
    [6, 0, 0, 2, 1, 7, 0, 0, 0],
    [0, 0, 5, 6, 0, 4, 2, 0, 3],
    [0, 0, 2, 3, 0, 0, 6, 0, 0]
    ]
    
    if (3, 6, 4, 7, 5, 7) in XY_wing(grid1):
        print("Passed XY-wing test")
        return True
    else:
        print("Failed XY-wing test")
        return False

# test for a unique rectangle
def TEST_unique_rectangle():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    if ((0, 0), (7, 0), (0, 2), (7, 2), (3, 4)) in unique_rectangle(grid):
        print("Passed Unique Rectangle test")
        return True
    else:
        print("Failed Unique Rectangle test")
        return False

# test the grader returns the correct score
def TEST_grader():
    grid = [[0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 3, 0, 0, 0, 6, 0],
            [2, 0, 0, 6, 0, 9, 5, 0, 0],
            [1, 4, 0, 0, 8, 0, 0, 0, 0],
            [0, 5, 0, 9, 0, 2, 4, 0, 0],
            [0, 0, 9, 0, 6, 1, 0, 0, 0],
            [7, 0, 2, 1, 9, 0, 8, 0, 5],
            [0, 0, 0, 2, 0, 8, 9, 0, 6],
            [0, 0, 0, 0, 0, 4, 0, 0, 0]]
    sole_technique,unique_candidate,BRC_interaction,block_block_interaction,naked_subset,hidden_subset,X_wing,swordfish,forcing_chain,XY_wing,unique_rectangle = patterns(grid)
    score = grader(sole_technique,unique_candidate,BRC_interaction,block_block_interaction,naked_subset,hidden_subset,X_wing,swordfish,forcing_chain,XY_wing,unique_rectangle)
    if score == 4950:
        print("Passed grader test")
        return True
    else:
        print("Failed grader test")
        return False
    

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_generate_puzzle_post(self):
        response = self.app.post('/generate_puzzle')
        self.assertEqual(response.status_code, 200)

    def test_generate_patterns_post(self):
        with app.test_request_context('/generate_patterns', method='POST'):
            with self.app as client:
                with client.session_transaction() as sess:
                    # Mock the session object here if needed
                    sess['grid'] = [[2, 5, 7, 3, 0, 0, 0, 0, 8], [0, 3, 0, 5, 0, 0, 0, 6, 7], [8, 0, 0, 2, 0, 7, 0, 0, 0], [0, 0, 0, 6, 0, 0, 7, 0, 0], [0, 0, 0, 0, 0, 9, 8, 2, 6], [7, 0, 0, 8, 0, 0, 0, 0, 0], [0, 0, 0, 0, 8, 0, 3, 0, 0], [4, 0, 0, 0, 3, 6, 0, 0, 9], [0, 8, 0, 0, 0, 2, 0, 0, 0]]
        response = self.app.post('/generate_patterns')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    start_time = time.time()
    # run all test
    count = 0       
    
    if TEST_generate_puzzle(): count+=1
    if TEST_duplicate_numbers(): count+=1
    if TEST_sole_technique(): count+=1
    if TEST_unique_candidate(): count+=1
    if TEST_brc_interaction(): count+=1
    if TEST_block_block_interaction(): count+=1
    if TEST_naked_subset(): count+=1
    if TEST_hidden_subset(): count+=1
    if TEST_x_wing(): count+=1
    if TEST_swordfish(): count+=1
    if TEST_forcing_chain(): count+=1
    if TEST_xy_wing(): count+=1
    if TEST_unique_rectangle(): count+=1
    if TEST_grader(): count+=1

    

    #check all tests return TRUE
    if count != 14:
        print("One of the test failed. Please see above for more detail.")

    else:
        print("All",count+2,"tests ran correctly!")
    end_time = time.time()
    elapsed_times = (end_time - start_time)
    print(elapsed_times)
    start_time = time.time()
    result = unittest.main()
    end_time = time.time()
    time_taken = end_time - start_time
    print("Time taken:", time_taken, "seconds")


    