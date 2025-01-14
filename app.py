from flask import Flask, render_template, jsonify
from twitter_scraper import scrape_twitter_trends
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client['twitter_trends']
collection = db['trends']

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run-script')
def run_script():
    data = scrape_twitter_trends()
    return jsonify(data)

@app.route('/latest')
def get_latest_record():
    latest_record = collection.find_one(sort=[("_id", -1)])
    return render_template("results.html", record=latest_record)

if __name__ == '__main__':
    app.run(debug=True)
