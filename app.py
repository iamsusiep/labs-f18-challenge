from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
# app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def main():
	return render_template('index.html')

@app.route('/sp3581')
def sp3581():
	return render_template('sp3581.html')
	
@app.route('/pokemon/<query>')
def pokemon(query):
	try:
		url ='http://pokeapi.co/api/v2/pokemon/' + query
		response = requests.request("GET", url, data="")
		data = response.json()
		# return str(data.keys())
		query_d = int(query)
		return "The pokemon with id "+str(query)+ " is " + str(data['name']) 
	except ValueError as vr:
		return str(query)+ " has id " + str(data['name'])
	pass

if __name__ == '__main__':
    app.run()

