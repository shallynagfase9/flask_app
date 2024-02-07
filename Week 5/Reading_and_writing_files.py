data = {
    "name" : "shally",
    "gmail" : "shally@gmail.com",
    "phone_no" : 849549375,
    "subjects" : ["data analytics", 'Big data', "Maths"]
 }

import json

with open ("test1.json",'w') as f:
    json.dump(data,f)
with open("test1.json",'r') as f:
    data1 = json.load(f)

print(data1)

print(data1['subjects'][1])


###################################
data2 = [
    ["name", "gmail", "number"],
    ["shally","shally@gmail.com",7834382],
    ["harpreet", 'harpreet@gmail.com', 7439859]
]

import csv

with open("test3.txt",'w') as f:
    w = csv.writer(f)
    for i in data2:
        w.writerow(i)

with open("test3.txt",'r') as f:
    read = csv.reader(f)
    for i in read:
        print(i)

with open("test4.txt","wb") as f:  # wb = write binary
    f.write(b"\x01\x02\x03")

with open("test4.txt","rb") as f:  # read binary
    print(f.read())


