import mysql.connector as aa
def db(): #creating database connection
    return aa.connect(host='localhost', username='root', password='Subbu@123')
    
