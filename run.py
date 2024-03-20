from flask import Flask, render_template, jsonify
from puzzle_generator import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_puzzle', methods=['POST'])
def generate_puzzle():
    puzzle = Generate_puzzle()
    print(puzzle)
    formatted_puzzle = [[int(num) for num in row] for row in puzzle]

    return jsonify(grid=formatted_puzzle)

if __name__ == '__main__':
    app.run(debug=True)
