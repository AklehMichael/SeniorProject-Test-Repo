import requests
import bs4
import re
def mathSpider():
    #This URL contains a list of all of schoolcraft's Math classes
    url = requests.get("https://www.schoolcraft.edu/academics/courses/math-courses") 
    #convert URL into soup object
    soup = bs4.BeautifulSoup(url.content,'lxml')
    # Find all relevant links that pertain to title MATH-10X using regular expression
    links = soup.find_all('a',title=re.compile('MATH-10.*'))
    #This loop will crawl through all of the URLS in the list and call mathclassData function to extract desired data
    for l in links:
        href ="https://www.schoolcraft.edu/" + l.get('href')
        print (href)
        #pass all URLs in list to mathClassData function for data extraction
        mathClassData(href)
        


def mathClassData(mathUrl):
    url = requests.get(mathUrl)
    soup = bs4.BeautifulSoup(url.content,'lxml')
    print('hello')
    

#Test
mathSpider()   