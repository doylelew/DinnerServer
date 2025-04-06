from flask import Flask

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def index():
    return "It is running"


if __name__ == "__main__":
    app.run(debug=True)
