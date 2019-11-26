import mysql.connector as mariadb

mariadb_connection = mariadb.connect(host='qpartys.de', user='testuser', password='12345', database='test')
cursor = mariadb_connection.cursor()

catid="0"

cursor.execute("SELECT start,end FROM kittyspinny WHERE catId=%s", (catid,))

for start, end in cursor:
    print("start: {}, end: {}").format(start, end)
    
detectValue = 0
cursor.execute("INSERT INTO kittyspinny (catId) VALUES (%s)", (detectValue,))
mariadb_connection.commit()
    
cursor.close()
