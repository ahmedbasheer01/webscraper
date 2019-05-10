from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import pymongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"

client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars
db.mars_data.drop()
collection = db.mars_data

#mars_data = db.mars_data.find()

@app.route("/")
def index():
    mars_data_values = list(db.collection.find())
    #mars_data_values = mars_data_values[0]
    return render_template("index.html", mars_data_values=mars_data_values)


@app.route("/scrape")
def scraper():
    mars_dict = scrape_mars.scrape()
    #db.mars_data.update({}, mars_dict, upsert=True)
    db.collection.delete_many({})
    db.collection.insert_one(mars_dict)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
