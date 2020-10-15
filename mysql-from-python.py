import os, pymysql

username=os.getenv('c9_user')
connection = pymysql.connect(host='localhost',user='root',password='', db='Chinook')

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
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                         Friends(name char(20), age int, DOB datetime);""")
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