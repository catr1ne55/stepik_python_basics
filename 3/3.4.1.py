import requests


a = input()
b = input()
urla = requests.get(a)
urlb = "<a href=\"" + b + "\">"
if urla.status_code == 200:
    if urlb in urla.text:
        