import requests
import bs4
import re
from connectDb import connectDb # saying import connectDb causes error
r = requests.get("https://www.schoolcraft.edu/academics/courses/math-courses") 
soup = bs4.BeautifulSoup(r.content,'lxml')
tableData = soup.find('a',{"title":"MATH-102-Technical Mathematics"}) #finds <a> tag containing "title attribute: title = MATH-102-Technical Mathematics

#print(tableData.text) #prints Math 102

schoolcraftMathNames = []
tableData2 = soup.find_all(title = re.compile('MATH-10.*')) #use regular expressions to find all title attributes title ='MATH-10X
for td in tableData2:
    #print(td.text)
    schoolcraftMathNames.append(td.text) #store Schoolcraft's 10X classes in a list
    
#for i in schoolcraftMathNames:
    #print(i)
    

connectObj = connectDb()
connect = connectObj.connectDB()
cursor = connect.cursor()
cursor.execute('select * FROM actor;')
data = cursor.fetchall()
for entry in data:
    print(entry)
