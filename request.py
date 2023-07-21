import requests 


url = "https://iknow.modme.uz/admin"

r = requests.get(url=url)

print( r.text)