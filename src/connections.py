import MySQLdb

def db_connection ():
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="tp2")
    return db