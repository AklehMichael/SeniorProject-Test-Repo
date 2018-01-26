import requests
import bs4
import re
from connectDb import connectDb # saying import connectDb causes error
#base URL to begin webcrawling
url = requests.get("https://www.schoolcraft.edu/academics/courses/math-courses") 
#convert URL into soup object
soup = bs4.BeautifulSoup(url.content,'lxml')
#tableData = soup.find('a',{"title":"MATH-102-Technical Mathematics"}) #finds <a> tag containing "title attribute: title = MATH-102-Technical Mathematics

# Find all relevant links that pertain to title MATH-10X
links = soup.find_all('a',title=re.compile('MATH-10.*'))
#links now contain proper "paths" we wish to crawl through


for l in links:
    href ="https://www.schoolcraft.edu/" + l.get('href')
    print (href)

    
    



   

        

        
    
    
    
    

#schoolcraftMathNames = []
#tableData2 = soup.find_all(title = re.compile('MATH-10.*')) #use regular expressions to find all title attributes title ='MATH-10X
#for td in tableData2:
    #print(td.text)
    #schoolcraftMathNames.append(td.text) #store Schoolcraft's 10X classes in a list
    
#for i in schoolcraftMathNames:
    #print(i)
    

