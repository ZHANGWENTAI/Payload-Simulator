import time
import mysql.connector
from PIL import Image

# image process
width = 200
height = 100
im = Image.open("offer.jpeg").convert("L").resize((width, height)).transpose(method=Image.ROTATE_270)
im.show()
pix = im.load()

# connect database
mydb = mysql.connector.connect(
    host='localhost',
    port='4000',
    user='root',
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS PingCAP_offer")
cursor.execute("use PingCAP_offer")

def create_tables(table_num, cursor):
    for i in range(table_num):
        create_table_sql = "CREATE TABLE IF NOT EXISTS offer_" + str(i) + " (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT )"
        cursor.execute(create_table_sql)
        insert_data = "INSERT INTO offer_" + str(i) + " VALUES (null)"
        for _ in range(257):
            cursor.execute(insert_data)

#create_tables(width, cursor)

for x in range(width):
    start_time = time.time()
    for y in range(height):
        select_data = "SELECT * FROM offer_" + str(y) + " LIMIT " + str(pix[y, x])
        cursor.execute(select_data)
        result = cursor.fetchall()
        
    end_time = time.time()
    duration = end_time - start_time
    if(duration > 60):
        continue
    print(x, 'done in', duration, 'seconds')
    time.sleep(60 - duration)

               
