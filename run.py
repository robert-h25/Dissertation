from flask import Flask, render_template, jsonify, session
from puzzle_generator import *
from patterns import *
from grader import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "sc21rh_diss"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_puzzle', methods=['POST'])
def generate_puzzle():
    grid = Generate_puzzle()
    print(grid)
    session['grid'] = grid
    # save to sessions
    formatted_grid = [[int(num) for num in row] for row in grid]

    return jsonify(grid=formatted_grid)

@app.route('/generate_patterns', methods =['POST'])
def generate_patterns():
    # get grid from sessions
    grid = session.get('grid')
    #perform pattern search and get total score
    pattern = patterns(grid)
    sole_technique,unique_candidate,BRC_interaction,block_block_interaction,naked_subset,hidden_subset,X_wing,swordfish,forcing_chain,XY_wing,unique_rectangle = pattern
    score = grader(sole_technique,unique_candidate,BRC_interaction,block_block_interaction,naked_subset,hidden_subset,X_wing,swordfish,forcing_chain,XY_wing,unique_rectangle)
    #jsonify reponse for JS
    return jsonify(patterns = pattern,score=score)

if __name__ == '__main__':
    app.run(debug=True)
