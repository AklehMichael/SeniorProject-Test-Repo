import requests
import bs4
import re
#request allows python to sned http requests and get() grabs content from website
r = requests.get("https://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los+Angeles%2C+CA") 
soup = bs4.BeautifulSoup(r.content,'lxml') #r.content is the content of the response in bytes while r.text would be unicode. Pass webURL to get bs4 object. lxml parser
#print(soup.prettify()) #functions that makes the html content easier to read
#print(soup.find_all('a')) # find all tags that begin with 'a'

#for link in soup.find_all('a'):
    #print(link) #prints all tags that begin with a
 #   print(link.get('href')) #prints all links on page
#match = soup.title.text # sets the first title tag to match adding .text prints the text inbetween the title tag <title> stufff </title>
#print(match)
#dataList = [] #define a list (array)
#match2 = soup.find('span', itemprop ='name')
#print(match2)

#for stuff in soup.find_all('span',itemprop ='name'): #loop that finds all <span> tags that have attribute: itemprop ='name' and prints them
 #   dataList.append(stuff.text) #store itmes text into a list[] (array)
    
#for stuff in dataList: #print everything in that list
 #   print(stuff)
 
#use of regular expressions
#Goal find all Postal codes and address regions of this pages coffee shops
postalCode = soup.findAll('span', itemprop = 'postalCode')
region = soup.findAll('span', itemprop ='addressRegion')
for i in postalCode:
    print(i.text)
    
for i in region:
    print(i.text)