from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/shop")
def shop():
    return render_template('/shop.html')

@app.route("/product_details.html")
def details():
    return render_template('/product_details.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)