from flask import Flask, render_template, url_for, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/result',  methods=['POST', 'GET'])

def result():
    if request.method == 'POST':
        q1 = request.form['q1']
        q1 = request.form['q1']
        q1 = request.form['q1']
        q1 = request.form['q1']
        q1 = request.form['q1']
        q1 = request.form['q1']
        print(q1)
        return render_template('Result.html')


if __name__ == "__main__":
    app.run(debug=True)

