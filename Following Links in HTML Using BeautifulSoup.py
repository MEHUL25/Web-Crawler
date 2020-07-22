import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url - ')
count = int(input("Enter count - "))
position = int(input("Enter position -"))


for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    s = []          #to store link
    t = []          #to store name
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
    url = s[position-1]
    #print s[position-1]
    p=t[position-1]
print(p)
