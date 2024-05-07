import mysql
import mysql.connector

def myconn():
    return mysql.connector.connect(host="localhost",user="root",password="")

def crtdb():
    conn = myconn()
    cursor = conn.cursor()
    query = "create database student"
    cursor.execute(query)
    conn.commit()
    print("Created")

crtdb()