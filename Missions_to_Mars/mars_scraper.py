# Import dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
import pymongo
import time
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017/marsDB'
    client = pymongo.MongoClient(conn)

    # Define the 'classDB' database in Mongo
    db = client.marsDB

    # Initialize browser
#def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    #executable_path = {'exeutable_path': "C:/Users/serenabaker/chromedriver_win32/chromedriver"}
    #executable_path = {'exeutable_path': "C:/Users/serenabaker/.wdm/drivers/chromedriver/mac64/89.0.4389.23/chromedriver"}

    #return Browser('chrome', **executable_path, headless=False)
    browser = Browser('chrome', **executable_path, headless=False)
    #browser = init_browser()

    # URL of page to be scraped
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    # Sleep function
    time.sleep(1)
    
    #response = requests.get(url)
    
    # Scrape page into Soup
    #html = browser.html
    news_html = browser.html
    news_soup = bs(news_html, "html.parser")
    #html = requests.get(url).text

    # Scrape NASA Mars News Site and collect latest News Tiltle and Paragraph Text, assign to variables

# news_title = "NASA's Curiosity Team Names Martian Hill That Serves as Mission ‘Gateway'"
# news_p = "The name honors recently deceased mission scientist Rafael Navarro-González, who helped lead the team that identified ancient organic compounds on Mars"

    news_title = news_soup.find_all('div', class_="content_title")
    news_p = news_soup.find_all('div', class_='article_teaser_body')[0].text

    # return news_title
    # return news_p

    # Store data in dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p


    }

    browser.quit()
    print(mars_data)
    return mars_data
    # return news_p
# console.log(mars_data)

# print(news_title)
# print(news_p)
# print(news_soup)

# Close browser after scraping
browser.quit()

    # return news_title
    # return news_p