from flask import Flask, render_template, request
from midi_tools import letter_dict, accidental_dict, format_pitch, name_to_partials_dicts

letters = letter_dict.keys()
accs = accidental_dict.keys()

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        letter = request.form['pitch']
        acc = request.form['acc']
        register = int(request.form['register'])
        n = int(request.form['n'])
        dist = float(request.form['dist'])
        freq = int(request.form['freq'])
        target_pitch = format_pitch(letter, register, acc)
        results = name_to_partials_dicts(target_pitch, n, dist, freq)
        print(results)
        return render_template("form.html", letters=letters, accs=accs,
        results=results, target_pitch=target_pitch, dist=dist, freq=freq)

    return render_template("form.html", letters=letters, accs=accs)

if __name__ == "__main__":
    app.run()
