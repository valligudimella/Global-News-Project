<<<<<<< HEAD
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "pub_34c6488db83f4f309fd36f0c7de989e6"
BASE_URL = "https://newsdata.io/api/1/news"

@app.route('/')
def home():
    category = request.args.get('category', 'top')
    params = {
        'apikey': API_KEY,
        'language': 'en',
        'category': category
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get('results', [])
    except Exception as e:
        print("Error fetching news:", e)
        articles = []

    return render_template('index.html', articles=articles, category=category)

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "pub_34c6488db83f4f309fd36f0c7de989e6"
BASE_URL = "https://newsdata.io/api/1/news"

@app.route('/')
def home():
    category = request.args.get('category', 'top')
    params = {
        'apikey': API_KEY,
        'language': 'en',
        'category': category
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get('results', [])
    except Exception as e:
        print("Error fetching news:", e)
        articles = []

    return render_template('index.html', articles=articles, category=category)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 2d0b801 (Add files via upload)
