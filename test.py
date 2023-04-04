import requests

BASE = 'http://127.0.0.1:5000/'


""" data =[{"likes":78, "name": "Joe", "views": 10000}, 
       {"likes":100000, "name": "how to make REST API", "views": 8000}, 
       {"likes":35, "name": "Tim", "views": 2000},]

for i in range(len(data)):  
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input() """
response = requests.patch(BASE + "video/2", {})
print(response.json())
