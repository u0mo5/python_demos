#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('bookfuns.db')

print ("Opened database successfully")

cursor = conn.execute("SELECT *  from fav   LIMIT 10")
for row in cursor:
   print ("ID = ", row[0])
   print ("URL ", row[1])
   print ("TITLE = ", row[2])
   print ("CATEGORY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()