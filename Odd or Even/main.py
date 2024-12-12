from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['post'])
def my_form_post():
    text = request.form['pyInput']
    processed_text = text
    remainder_processed_text = int(processed_text) % 2
    if remainder_processed_text == 0:
        return "It is Even."
    else:
        return "It is Odd."
    
if __name__ == '__main__':
    app.run()