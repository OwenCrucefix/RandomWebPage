import webbrowser
from random import randint
from time import sleep
from statuscode import get_status_code
extension = [".org",".com",".net"]
dictionary = open("dictionary.txt","r")
dic = []
for i in dictionary:
    string = i.strip("\n")
    dic.append(string)

ExtensionNum = randint(0,2)
ExtensionUsed = extension[ExtensionNum]

run = True
failedcount = 0
while run:
    webnum = randint(0,len(dic)-1)
    webword = dic[webnum]
    usedurl = "www."+webword+ExtensionUsed
    if get_status_code(usedurl) == None:
        failedcount += 1
        pass
    else:
        #print get_status_code(usedurl) #Prints the webpage's Status Code
        #print failedcount    #Prints the amount of times it looped before finding a webpage
        print "Now opening " + usedurl
        sleep(1)
        webbrowser.open(usedurl,new=0,autoraise=True)
        run = False
        
