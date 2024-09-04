from flask import Flask, render_template, request
import opencc

app = Flask(__name__)
converter = opencc.OpenCC('s2t.json')

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_text = ''
    if request.method == 'POST':
        simplified_text = request.form['simplified_text']
        converted_text = converter.convert(simplified_text)
    return render_template('index.html', converted_text=converted_text)

if __name__ == '__main__':
    app.run(debug=True)
