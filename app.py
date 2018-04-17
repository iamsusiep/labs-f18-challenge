from flask import Flask, render_template

app = Flask(__name__)
# app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def main():
	return render_template('index.html')

@app.route('/sp3581')
def sp3581():
	return render_template('sp3581.html')

if __name__ == '__main__':
    app.run()


