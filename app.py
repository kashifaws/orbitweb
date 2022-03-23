from flask import Flask, render_template
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver

app = Flask(__name__)

website_url = 'https://orbitxch.com/customer/inplay/highlights/1'
@app.route("/<username>/<passw>/<ip>/<port>")
def hello_world(username,passw,ip,port):

    driver_options = webdriver.ChromeOptions()
    driver_options.headless = True
    driver_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    driver_options.add_argument("--headless")
    driver_options.add_argument("--disable-dev-shm-usage") 
    driver_options.add_argument("--no-sandbox")

    optionss = {
	    'proxy': {
        'http': 'http://'+username+':'+passw+'@'+ip+':'+port+'',
        'https': 'http://'+username+':'+passw+'@'+ip+':'+port+'',
		'no_proxy': 'localhost,127.0.0.1'
	}
}

    driver_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36')
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=driver_options)
    driver.get(website_url)
    sleep(30)
    people = []
    for request in driver.requests:
        first_request = driver.last_request;  
        people.append(first_request.headers) 
    
    return render_template("index.html", value=people)

if __name__ == "__main__":
    app.run(debug=True)
