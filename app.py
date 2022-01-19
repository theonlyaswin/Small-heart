import pyshorteners
from flask import Flask,render_template,url_for,request

app = Flask(__name__)

def shorten_magic(url):
    output_url = pyshorteners.Shortener().tinyurl.short(url)
    return output_url


@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        original_url = request.form["original"]
        print(original_url)
        new_url = shorten_magic(original_url)
        return render_template('index.html',original_url = original_url ,output_url = new_url)

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
