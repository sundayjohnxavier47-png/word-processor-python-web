from flask import Flask, render_template, request
from puncta import collapse_spaces, fix_punctuation_space
from caps import capitalize
from quotes import fix_quotes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    input_text = ""
    output_text = ""

    if request.method == "POST":
        input_text = request.form["text"]

        result = collapse_spaces(input_text)
        result = fix_quotes(result)
        result = fix_punctuation_space(result)
        result = capitalize(result)

        output_text = result

    return render_template("index.html", input=input_text, output=output_text)

if __name__ == "__main__":
    app.run(debug=True, port=8080)