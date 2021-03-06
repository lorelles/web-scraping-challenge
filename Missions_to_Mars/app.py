from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import mars_scraper

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsDB")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    # mars_data = mars_scraper.scrape_info()
    mars_data = mongo.db.mars_data
    scraped_data = mars_scraper.scrape_info()

    # Update the Mongo database using update and upsert=True
    mars_data.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
 
