import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'
#url = 'http://www.google.com/'
r = requests.get(url)
print(r.text)

print(r.status_code)
print(r.reason)
print(r.headers)
print(r.request)
print(r.request.headers)