from flask import Flask, render_template, request
from midi_tools import letter_dict, accidental_dict

letters = letter_dict.keys()
accs = accidental_dict.keys()

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        pitch = request.form['pitch']
        acc = request.form['acc']
        register = request.form['register']
        n = request.form['n']
        dist = request.form['dist']
        freq = request.form['freq']
        print(pitch, acc, register, n, dist, freq)

    return render_template("form.html", letters=letters, accs=accs)

if __name__ == "__main__":
    app.run()
