from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/solarpage')

def index():
    return render_template("solar.html")

if "__name__" == "__main__":
    app.run(host="your_host", port=8080, debug=True)