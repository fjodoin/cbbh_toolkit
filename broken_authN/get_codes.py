import re
import requests

url = "https://country-code.cl/"
response = requests.get(url)

if response.status_code == 200:
    html = response.text.split("\n")
    for line in html:
        pattern = r'&nbsp;([^&]+)&nbsp;'
        match = re.search(pattern, line)
        if match:
            # Extract the text between the "&nbsp;" tags
            extracted_text = match.group(1)
            print(extracted_text)
else:
    print(f"Failed to retrieve HTML content. Status code: {response.status_code}")
