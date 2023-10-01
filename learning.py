import requests

url = "https://developer.mozilla.org/en-US/"

r = requests.get(url)
print(r.text)
