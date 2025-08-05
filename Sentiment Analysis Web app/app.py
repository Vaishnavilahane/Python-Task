from flask import Flask, render_template, request
from textblob import TextBlob
import webbrowser
import threading

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = ''
    polarity = ''
    subjectivity = ''

    if request.method == 'POST':
        user_text = request.form['text']
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            sentiment = 'Positive 😊'
        elif polarity < 0:
            sentiment = 'Negative 😞'
        else:
            sentiment = 'Neutral 😐'

        return render_template('index.html', text=user_text,
                               sentiment=sentiment, polarity=polarity,
                               subjectivity=subjectivity)

    return render_template('index.html')



def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True, use_reloader=False)
