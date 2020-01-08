import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'
#url = 'http://www.google.com/'
r = requests.get(url)
print(r.text)