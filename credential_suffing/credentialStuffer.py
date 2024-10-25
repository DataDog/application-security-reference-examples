import mechanize
import csv


with open('creds.csv', newline='') as f:
    reader = csv.reader(f)
    creds = list(reader)

br = mechanize.Browser()
for cred in creds:
    br.open("http://127.0.0.1:5000/login")
    username = cred[0]
    password = cred[1]
    try:
        br.select_form(nr=0)
        br.form['username'] = username
        br.form['password'] = password
        req = br.submit()
        print(req.code)
        print(username,password)
    except:
        print("Invalid Credentials.")