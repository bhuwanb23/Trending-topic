# Twitter Trends Scraper with Selenium, ProxyMesh, and MongoDB
An automated tool for scraping the top 5 trending topics on Twitter using Selenium, ProxyMesh for IP rotation, and storing the data in MongoDB. This project includes a Flask web app that triggers the scraper and displays the results in a user-friendly interface.

## 📜 Project Overview
This project automates the process of logging into Twitter, fetching the top 5 trending topics from the "What's Happening" section, and storing this data in a MongoDB database. The scraper uses ProxyMesh to rotate IPs for each request. The trends are displayed through a Flask web application with a simple interface.

## 🚀 Features
- Twitter Trend Scraping: Automatically logs into Twitter, navigates to the homepage, and scrapes the top 5 trending topics.
- IP Rotation with ProxyMesh: Uses ProxyMesh to ensure each request comes from a different IP address.
- MongoDB Integration: Stores scraped data (trend names, timestamp, and IP address) in MongoDB.
- Flask Web Application: A button on a simple web page to trigger the scraper and display the results in real-time.
- Beautiful Results Page: Displays trends, timestamp, and the MongoDB JSON extract of the latest scraped record.

## 🛠 Technologies Used
- Python: For scripting the automation and backend logic.
- Selenium: For automating the browser interactions and scraping the data.
- ProxyMesh: For IP rotation to avoid detection and rate limiting.
- MongoDB: For storing scraped data.
- Flask: To create a web interface to interact with the scraper.
- HTML/CSS: For building the user interface.

## ⚡ How to Use
1. Clone the Repository
``` bash
git clone https://github.com/your-username/twitter-trends-scraper.git
cd twitter-trends-scraper
```

2. Install Dependencies
Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```
3. Set Up MongoDB
Ensure that MongoDB is running locally or you can use MongoDB Atlas if you prefer a cloud setup.

4. Set Up ProxyMesh
Create a ProxyMesh account and obtain your API credentials. Update the PROXY variable in twitter_scraper.py with your ProxyMesh credentials.
```
PROXY = "http://username:password@proxy.proxyMesh.com:31280"
```

5. Update Twitter Credentials
In twitter_scraper.py, update the username and password fields with your own Twitter account credentials.
```
driver.find_element(By.NAME, "text").send_keys("your_twitter_username")
driver.find_element(By.NAME, "password").send_keys("your_twitter_password")
```

6. Run the Flask Web App
Start the Flask application by running:

```bash
python app.py
Visit http://127.0.0.1:5000/ in your browser.
```

7. Trigger the Scraper
Click the "Click here to run the script" button on the webpage to trigger the scraper. Once the script finishes, the top 5 trends will be displayed, along with the MongoDB JSON extract of the latest data.

## 🔍 Project File Structure
```
twitter-trends-scraper/
│
├── app.py                    # Flask app for triggering and displaying the results
├── twitter_scraper.py        # Selenium script for scraping Twitter trends
│
├── templates/                # HTML templates for Flask
│   ├── index.html            # Homepage with button to run the script
│   └── results.html          # Results page to display the trends and MongoDB data
│
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

🧑‍💻 Contributing
Feel free to fork this repository and contribute. If you find any bugs or have ideas for improvements, create an issue or submit a pull request.

📧 Contact
For any queries or issues, feel free to reach out to me at bhuwanseervi4567@gmail.com.

Happy Scraping!
