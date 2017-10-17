import webbrowser
from random import randint
from time import sleep
extension = [".org",".com",".net"]
http = ["http://www.","https://www."]
urllength = randint(1,1)

dictionary = open("dictionary.txt","r")
dictionarylist = []
for i in dictionary:
    dictionarylist.append(i)
dictionary.close()
    
x = 0
urlwords = []
while x < urllength:
    randomword = randint(1,len(dictionarylist))
    urlwords.append(dictionarylist[randomword-1])
    x += 1
    
randhttp = randint(0,1)
usedhttp = http[randhttp]
randextension = randint(0,2)
usedextension = extension[randextension]

usedurl = usedhttp
for i in urlwords:
    usedurl = usedurl + i
usedurl = usedurl + usedextension

print "Now opening " + usedurl
sleep(2)
webbrowser.open(usedurl,new=0,autoraise=True)
