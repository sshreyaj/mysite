from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def homepage():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(port=5000, debug=True)