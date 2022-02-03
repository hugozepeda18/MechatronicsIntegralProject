import mysql.connector
import re

conn = mysql.connector.connect(
     host = "localhost",
     port = "3306",
     user = "root",
     password = "YaelHugo2122",
     database = 'PIM'
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
found = False

for db in cursor:
    pattern = "[(,')]"
    db_string = re.sub(pattern, "", str(db))
    if db_string == 'PIM':
        found = True
        print("database PIM exists!")
if not found:
    cursor.execute("CREATE DATABASE PIM")

    sql = "DROP TABLE IF EXISTS Moviliario"
    cursor.execute(sql)

    sql = "DROP TABLE IF EXISTS Movimientos"
    cursor.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS Moviliario(ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255) NOT NULL, Costo INT, Modelo VARCHAR(255), Lugar VARCHAR(255), Descripcion VARCHAR(255))"
cursor.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS Movimientos(ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, MovID  INT NOT NULL, Fecha  DATETIME, FOREIGN KEY (MovID) REFERENCES Moviliario(ID))"
cursor.execute(sql)

# PIM_list = ['TV', 2000, 'Samsung', 'Cuarto TV', '44in']
#
# for art in PIM_list:
#     sql = "INSERT INTO PIM_list(Nombre, Costo, Modelo, Lugar, Descripcion) VALUES(%s, %s, %s, %s, %s)"
#     values = ("Nombre", "Costo", "Modelo", "Lugar", "Descripcion")
#     cursor.execute(sql, values)
#
#     conn.commit()
#     print("Inserted " + str(cursor.rowcount) + " row into PIM_list")
#
# sql = "SELECT * FROM *"
# print(cursor.execute(sql))

values = ("Python", "1", "es", "un", "test")
sql = "INSERT INTO Moviliario(Nombre, Costo, Modelo, Lugar, Descripcion) VALUES(%s, %s, %s, %s, %s)"
cursor.execute(sql, values)
conn.commit()

sql = "SELECT * FROM Moviliario WHERE Costo = 2000 AND Nombre = 'TV'"
cursor.execute(sql)
# get all records
records = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)

print("\nPrinting each row")
for row in records:
    print("Id = ", row[0])
    print("Nombre = ", row[1])
    print("Costo  = ", row[2])
    print("Modelo = ", row[3])
    print("Lugar  = ", row[4])
    print("Descripción  = ", row[5], "\n")

#print(records)