import os, pymysql

### NEED TO DECLARE EACH CONNECT FOR EACH TRY ###
# connection = pymysql.connect(host='localhost',user='root',password='', db='Chinook')

## CURSOR OUTPUT ##
# try:
#     with connection.cursor() as cursor:
#         sql = "select * from Genre limit 5;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)

# finally:
#     connection.close()

## DICTIONARY OUTPUT (JSON) ##
# try:
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         sql = "select * from Genre limit 5;"
#         cursor.execute(sql)
#         for row in cursor:
#             print(row)

# finally:
#     connection.close()


## CREATING TABLE IN SQL ##
# try:
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         cursor.execute("CREATE TABLE IF NOT EXISTS Friends(name char(20), age int, DOB datetime);
#                         #Note that the above will still display a warning (not error) 

# finally:
#     connection.close()

## INSERTING DATA INTO FRIENDS TABLE ##
# try:
#     with connection.cursor() as cursor:
#         rows = [ ("bob", 21, "1990-02-06 23:04:46"),
#                 ("jim", 56, "1955-05-09 13:12:45"),    
#                 ("fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
#         connection.commit()
#         print(cursor.rowcount, "record(s) affected")
# finally:
#     connection.close()

# try:
#     # with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#     with connection.cursor() as cursor:
#         sql = "select * from Artist limit 5;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)
#         # for row in result:
#         #     print(row)
# finally:
#     connection.close()

## INSERTING RECORDS ###
# connection = pymysql.connect(host='localhost',user='root',password='', db='Chinook')
# try:
#     with connection.cursor() as cursor:
#         #inserting
#         row = [("bob", 21, "1990-02-06 23:04:56"),
#                ("jim", 56, "1955-05-09 13:12:45"),
#                ("fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", row)
#         connection.commit()
#         print("Records affected: ", cursor.rowcount)
#         sql = "Select * from Friends;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)

# finally:
#     connection.close()

## UPDATING RECORDS ##
# connection = pymysql.connect(host='localhost',user='root',password='', db='Chinook')
# try:
#     with connection.cursor() as cursor:
#         sql = "UPDATE Friends SET age = 22 WHERE name = 'bob';"
#         cursor.execute(sql)
#         connection.commit()
#         print("Records affected: ", cursor.rowcount)

# finally:
#     connection.close()

### MULTIPLE UPDATES ####
# connection = pymysql.connect(host='localhost',user='root',password='', db='Chinook')
# try:
#     with connection.cursor() as cursor:
#         rows = [(23, 'bob'),
#                 (24, 'jim'),
#                 (25, 'fred')]
#         cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
#         connection.commit()
#         print("Records affect: ", cursor.rowcount)
# finally:
#     connection.close()

## DELETE ##
connection = pymysql.connect(host='localhost',user='root',password='', db='Chinook')
try:
    with connection.cursor() as cursor:
        # sql = "DELETE from Friends where name = 'bob';"
        rows = ["bob", "jim"]
        cursor.executemany("DELETE from Friends where name = %s;", rows)
        connection.commit()
        print("Records affect: ", cursor.rowcount)
finally:
    connection.close()