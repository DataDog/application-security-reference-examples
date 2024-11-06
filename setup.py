import mechanize
import csv

with open('setup_creds.csv', newline='') as f:
    reader = csv.reader(f)
    setup_creds = list(reader)

br = mechanize.Browser()
br.set_handle_robots(False)
for cred in setup_creds:
    br.open("http://vulnerable_website:5000/register")
    username = cred[0]
    password = cred[1]
    try:
        br.select_form(nr=0)
        br.form['username'] = username
        br.form['password'] = password
        req = br.submit()
        print("User Created.")
    except:
        print("User Already Created.")

for cred in setup_creds:
    br.open("http://vulnerable_website:5000/login")
    username = cred[0]
    password = cred[1]
    try:
        br.select_form(nr=0)
        br.form['username'] = username
        br.form['password'] = password
        req = br.submit()
        print(username, " logged in.")
        print(req.code)
    except:
        print("User unable to log in.")
            