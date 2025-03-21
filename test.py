'''string = "abc"
string.replace("d","")
print(string)
test = urllib.request.urlopen("https://i.postimg.cc/fRB9ZHZ4/test-image-3061864-1280-1648860360.png")
print(test.read())'''
import requests
import json
import pyclip
import urllib.request as ul
from bs4 import BeautifulSoup
x = pyclip.paste().decode("utf-8")
pathtype = None
if "\x00" in x:
    x = x.replace("\x00","")
try:
    soup = BeautifulSoup(x, 'html.parser')
    x_attrs = soup.find('img').attrs
    x = x_attrs["src"]
except:
    x = x
print(x)
y = ul.urlopen(x)
file = open("/home/timo/Downloads/osint-exercise-001-big-picture.jpeg","rb")
params = {
    'key': '5fd22077dd3563d8d44d78b4985e6fd8',
}

files = {
    'image': (y),
}

response = requests.post('https://api.imgbb.com/1/upload', params=params, files=files)
print(response.json())