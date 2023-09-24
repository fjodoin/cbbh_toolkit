import json

# Copied from BURP curl command
curl_command = """
curl -i -s -k -X $'POST' \
    -H $'Host: 94.237.48.48:51996' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate, br' -H $'Referer: http://94.237.48.48:51996/messages.php' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 38' -H $'Origin: http://94.237.48.48:51996' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'htb_sessid=MDk4ZjZiY2Q0NjIxZDM3M2NhZGU0ZTgzMjYyN2I0ZjY%3D' \
    --data-binary $'user=support&message=123&submit=submit' \
    $'http://94.237.48.48:51996/messages.php'
"""

def parse_headers(header_lines):
    headers_in_json = {}
    for line in header_lines.split("-H"):
        if line == " ":
            continue
        else:
            formatted_headers = line.replace("$", "").replace("'", "")
            formatted_key = formatted_headers.split(":", 1)[0]
            formatted_value = formatted_headers.split(":", 1)[1]
            headers_in_json.update({formatted_key.strip() : formatted_value.strip()})
    return headers_in_json

# Split the curl command into lines and create a dictionary
curl_lines = curl_command.strip().split("  ")

# PARSE REQUEST

headers = parse_headers(curl_lines[2])
print(headers)

# Find other important information, such as session IDs and Data body
## Session ID
session_id = curl_lines[4].replace("-b $", "").replace("'", "")
print(session_id)

## Data Body
data = curl_lines[6].replace("--data-binary $", "").replace("'", "")
print(data)
