import sqlite3
import mysql.connector
import pymongo
import boto3
import os

def connect_sqlite():
    return sqlite3.connect("products.db")

def connect_mysql():
    return mysql.connector.connect(
        host="mydbinstancesql.c0zolapcanem.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminadministrator",
        database="database-1"
    )

def connect_mongodb():
    client = pymongo.MongoClient("mongodb://your-ec2-endpoint:27017/")
    return client["your-database"]

def connect_s3():
    return boto3.client('s3', 
                        aws_access_key_id='your-access-key', 
                        aws_secret_access_key='your-secret-key', 
                        region_name='your-region')

def connect_local():
    if not os.path.exists("local_products"):
        os.makedirs("local_products")
    return "local_products"

def create_sqlite_table():
    conn = connect_sqlite()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

create_sqlite_table()
