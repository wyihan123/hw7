from flask import Flask, render_template
from secret import API_KEY
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/name/<name>')
def hello(name=None):
    return render_template('name.html', name=name)


@app.route('/headlines/<name>')
def headlines(name=None):
    api = requests.get(f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={API_KEY}')
    result = api.json()
    stories = []
    for i in result['results'][:5]:
        stories.append(i['title'])

    return render_template('top5.html', stories=stories, name=name)



if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)