import psycopg2
class connectDb:
    def connectDB(self):
        try:
            return psycopg2.connect(database= 'dvdrental', user='postgres', password='9815064')
        except:
            print('Failed to connect to DB')
            
            


           
#connectObj = connectDb()
#connect = connectObj.connectDB()
#cursor = connect.cursor()
#cursor.execute('select * FROM actor;')
#data = cursor.fetchall()
#for entry in data:
#    print(entry)

            