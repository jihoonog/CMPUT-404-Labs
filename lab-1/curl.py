import requests

# This will send a GET request to the raw URL that points to this file on my personal GitHub. 
# The default behaviour for a request is that the body is downloaded immediately.
req = requests.get("https://raw.githubusercontent.com/jihoonog/CMPUT-404-Labs/main/lab-1/curl.py")

# This will print out the source code as plain text
print(req.text)