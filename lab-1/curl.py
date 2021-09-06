import requests

req = requests.get("https://raw.githubusercontent.com/jihoonog/CMPUT-404-Labs/main/lab-1/curl.py")

print(req.text)