import time
import threading
import mysql.connector
from PIL import Image


# image process
def get_gray_matirx(width, height):
    im = Image.open("offer.jpeg").convert("L").resize((width, height)).transpose(method=Image.FLIP_TOP_BOTTOM)
    im.show()
    pix = im.load()
    
    gray_matrix = []
    for y in range(height):
        line = []
        for x in range(width):
            line.append(pix[x, y])
        gray_matrix.append(line)
    return gray_matrix
        
# create database and tables
def create_tables(table_num):
    mydb = mysql.connector.connect(
	host='localhost',
	port='4000',
	user='root',
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS PingCAP_offer")
    mycursor.execute("use PingCAP_offer")
    
    for i in range(table_num):
        create_table_sql = "CREATE TABLE IF NOT EXISTS offer_" + str(i) + " (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT )"
        mycursor.execute(create_table_sql)
        insert_data_sql = "INSERT INTO offer_" + str(i) + " VALUES (null)"
        for _ in range(257):
            mycursor.execute(insert_data_sql)
    mydb.close()

# task for each thread
def write_per_min(table_id, seq):
    db = mysql.connector.connect(
	host='localhost',
	port='4000',
	user='root',
        database='PingCAP_offer',
    )
    cursor = db.cursor()
    for write_num in seq:
        select_data = "SELECT * FROM offer_" + str(table_id) + " LIMIT " + str(write_num)
        cursor.execute(select_data)
        result = cursor.fetchall()
        time.sleep(60)
    db.close()


if __name__ == "__main__":
    width = 100
    height = 100
    gray_matrix = get_gray_matirx(width, height)

    create_tables(height)
    
    for y in range(height):
        t = threading.Thread(target=write_per_min, name="thread_"+str(y), args=(y, gray_matrix[y]), daemon=True)
        t.start()

    



               
