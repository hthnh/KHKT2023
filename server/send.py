import requests

url = 'http://192.168.10.40:5000/login'
myobj = {'username': 'htnh', 'password': '1214'}

x = requests.post(url, json = myobj)

print(x.text)