from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient
from datetime import datetime
import time
import random

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client['twitter_trends']
collection = db['trends']

# ProxyMesh Credentials
PROXY = "http://username:password@proxy.proxyMesh.com:31280"  # Update with your ProxyMesh credentials

# Selenium Setup
options = webdriver.ChromeOptions()
options.add_argument(f'--proxy-server={PROXY}')
service = Service('/path/to/chromedriver')  # Update with your chromedriver path
driver = webdriver.Chrome(service=service, options=options)

def scrape_twitter_trends():
    try:
        # Log in to Twitter
        driver.get("https://twitter.com/login")
        time.sleep(5)  # Allow page to load
        
        # Enter username and password
        driver.find_element(By.NAME, "text").send_keys("your_twitter_username")  # Update with your Twitter username
        driver.find_element(By.NAME, "text").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys("your_twitter_password")  # Update with your Twitter password
        driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(5)

        # Navigate to the homepage
        driver.get("https://twitter.com/home")
        time.sleep(5)

        # Scrape the "What's Happening" section
        trends = driver.find_elements(By.XPATH, '//div[@aria-label="Timeline: Trending now"]//span')[:5]
        trend_names = [trend.text for trend in trends]

        # Get current IP
        current_ip = driver.execute_script("return window.navigator.userAgent;")

        # Insert data into MongoDB
        unique_id = random.randint(1000, 9999)
        data = {
            "_id": unique_id,
            "trend1": trend_names[0],
            "trend2": trend_names[1],
            "trend3": trend_names[2],
            "trend4": trend_names[3],
            "trend5": trend_names[4],
            "end_time": datetime.now(),
            "ip_address": current_ip,
        }
        collection.insert_one(data)
        return data

    finally:
        driver.quit()
