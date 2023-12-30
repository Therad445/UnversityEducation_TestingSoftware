import requests as r
response=r.post("https://www.strategium.ru/forum"+"/search/",{"search":"Europe"})
print(response.url)
print(response.status_code)