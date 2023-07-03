#choice1
import pyshorteners                  

url= input("enter the link:")

def shorten_url(url):
    s=pyshorteners.shortener()
    print(s.bitly.short(url))
                          
     
#choice2
import pyshorteners

link = input("Enter the link to shorten: ")
name = input("Give your link name: ")

api_key = ''# paste yoour biitlly api key
shortener = pyshorteners.Shortener(api_key=api_key)

short_link = shortener.bitly.short(link)

print('Shortened link:', short_link)
