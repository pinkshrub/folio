from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	return render_template('dice.html')

app.run(debug=True)