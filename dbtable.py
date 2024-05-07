import mysql
import mysql.connector

def myconn():
    return mysql.connector.connect(host="localhost",user="root",password="",database="student")
def crttable():
    conn = myconn()
    cursor=conn.cursor()
    query="CREATE TABLE std (id INT(2) PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), city VARCHAR(50))"
    cursor.execute(query)
    conn.commit()
    print("Created")
    conn.close()
def inserdata(name,city):
    try:
        conn = myconn()
        cursor=conn.cursor()
        args=(name,city)
        query = "INSERT INTO std (name,city) VALUES(%s,%s)"
        cursor.execute(query,args)
        conn.commit()
        print("Inserted")
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error connecting or inserting data: {err}")

n = input("Enter Name :")
c = input("Enter City :")

inserdata(n,c)
