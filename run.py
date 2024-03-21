from flask import Flask, render_template, jsonify, session
from puzzle_generator import *
from patterns import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "sc21rh_diss"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_puzzle', methods=['POST'])
def generate_puzzle():
    puzzle = Generate_puzzle()
    print(puzzle)
    session['grid'] = puzzle
    # save to sessions
    formatted_puzzle = [[int(num) for num in row] for row in puzzle]

    return jsonify(grid=formatted_puzzle)

@app.route('/generate_patterns', methods =['POST'])
def generate_patterns():
    grid = session.get('grid')
    sole_technique,unique_candidate,BRC_interaction,block_block_interaction,naked_subset,hidden_subset,X_wing,swordfish,forcing_chain,XY_wing,unique_rectangle = patterns(grid)
    # format

    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)
