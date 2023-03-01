
import requests  # εισαγωγή της βιβλιοθήκης
from datetime import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? \n')
            if reply == 'n':
                break

url=input("Give a url:")  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    more(html)

#a)
headers=response.headers
if "Server" in headers.keys():

    for key,value in headers.items(): 
            if key=='Server':
                print("Web server is {} \n".format(value))
else:
    print("Can't find information about the server.\n")            

#b)           
cookies=response.cookies

li=[]
for key,value in enumerate(cookies):
    li.append(key) 

if len(li)!=0:

    print("This website uses {} cookies \n".format(len(li)))
else:
    print("This website does not use cookies")

#c)
for item in cookies:
     print("Cookie name:{}".format(item.name))
     
     if(item.expires==None):
          print("This cookie does not expire.\n")
     else:
        print("Expires at:{}\n".format(datetime.fromtimestamp(item.expires)))
    
     
    
     