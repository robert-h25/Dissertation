
#TODO: Add a function that calculates distance between cells for some patterns
#       change scores per pattern based on how many times they occur

#Function which takes all patterns, scores each pattern and returns a total score
def grader(sole_technique,unique_candidate,BRC_interaction,block_block_interaction,naked_subset,hidden_subset,X_wing,swordfish,forcing_chain,XY_wing,unique_rectangle):
    #set initial score as 0
    score = 0
    #scores per pattern
    score_sole_technique = 5
    score_unique_candidate = 10
    score_BRC_interaction = 20
    score_block_block_interaction = 50
    score_naked_subset = 50
    score_hidden_subset = 10
    score_x_wing = 100
    score_swordfish = 150
    score_forcing_chain = 250
    score_XY_wing = 75
    score_unique_rectangle = 100

    # count amount of each pattern and
    # calculate scores per pattern and total score
    score = len(sole_technique)*score_sole_technique + score
    score = len(unique_candidate)*score_unique_candidate + score
    score = len(BRC_interaction)*score_BRC_interaction + score
    score = len(block_block_interaction)*score_block_block_interaction + score
    score = len(naked_subset)*score_naked_subset + score
    score = len(hidden_subset)*score_hidden_subset + score
    score = len(X_wing)*score_x_wing + score
    score = len(swordfish)*score_swordfish + score
    score = len(forcing_chain)*score_forcing_chain + score
    score = len(XY_wing)*score_XY_wing + score
    score = len(unique_rectangle)*score_unique_rectangle + score

    print("Total score of:",score)

    return score
