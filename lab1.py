import requests

print(requests.__version__)

print(requests.get("http://google.com"))

print(requests.get("https://raw.githubusercontent.com/mikeharbidge/cmput404lab1/master/lab1.py").text)

