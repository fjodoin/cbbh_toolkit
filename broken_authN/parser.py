import re

htb_boxes = []

with open("machines.txt","r") as file:
    data=file.read()
    print("The file contents are:")
    for line in data.split(" "):
        if "alt" in line: 
            match = re.search(r'"(.*?)"', line)
            if match:
                #print(match.group(1))
                htb_boxes.append(match.group(1))

print("htb boxes: ", htb_boxes)

with open("htb_boxes.txt", "w") as file:
    for box in htb_boxes:
        file.write(box + '\n')
                
                
