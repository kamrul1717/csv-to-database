import csv
import pymysql
import sys

mydb = pymysql.connect(host='localhost',
    user='root',
    passwd='',
    db='test')
cursor = mydb.cursor()

try:

    with open('users.csv', 'r') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',')
        csv_data = csv.reader(csvfile, delimiter='\t')
        for row in csv_data:
            cursor.execute('INSERT INTO users(name, email) VALUES(%s, %s)',  (row[0],row[1]))
except Exception as e:
    print('Error: {}'.format(str(e)))
    sys.exit(1)
        
mydb.commit()
cursor.close()
print("Done");