#!/usr/bin/env python3
import sqlite3
#some initial data
zone = 'kitchen';
temperature = 13.3;
date = '2020-10-01';
time = '20:50:50';
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
for i in range(10):
    #execute insert statement
    if i == 1 or 4 or 7 or 10:
        zone = 'kitchen';
    elif i == 2 or 5 or 8:
        zone = 'greenhouse';
    else:
        zone = 'garage';
    temperature += 1.1;
    cursor.execute('''insert into temps values (?, ?, ?, ?)''',
    (date, time, zone, temperature));
dbconnect.commit();
#create new table
cursor.execute('CREATE TABLE ages(name TEXT, dateofbirth DATE, age NUMERIC)');
#fill new table with data
cursor.execute('''insert into ages values ('Cris', '2013-10-05', 6)''')
cursor.execute('''insert into ages values ('Bob', '1993-11-23', 26)''')
cursor.execute('''insert into ages values ('Dean', '2006-03-14', 14)''')
cursor.execute('''insert into ages values ('Nico', '2012-04-12', 8)''')
dbconnect.commit();

#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );
#execute simple select statement
cursor.execute('SELECT * FROM ages');
#print data
for row in cursor:
    print(row['name'],row['dateofbirth'],row['age'] );
#close the connection
dbconnect.close();
