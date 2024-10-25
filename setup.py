import mechanize
import csv
import time

with open('setup_creds.csv', newline='') as f:
    reader = csv.reader(f)
    setup_creds = list(reader)

br = mechanize.Browser()
for cred in setup_creds:
    br.open("http://127.0.0.1:5000/register")
    username = cred[0]
    password = cred[1]
    try:
        br.select_form(nr=0)
        br.form['username'] = username
        br.form['password'] = password
        req = br.submit()
        print("User Created.")
        # time.sleep(60)
    except:
        print("User Already Created.")

for count in range(0,1):
    print("count = ", count)
    for cred in setup_creds:
        br.open("http://127.0.0.1:5000/login")
        username = cred[0]
        password = cred[1]
        try:
            br.select_form(nr=0)
            br.form['username'] = username
            br.form['password'] = password
            req = br.submit()
            print(username, " logged in.")
            print(req.code)
            # time.sleep(60)
        except:
            print("User unable to log in.")
            