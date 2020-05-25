import time
import mysql.connector
from PIL import Image


# image process
def get_gray_matrix(width, height):
    im = Image.open("offer.jpeg").convert("L").resize((width, height)).transpose(method=Image.ROTATE_270)
    im.show()
    pix = im.load()
    return pix

# 256 rows per table
def create_tables(table_num, mycursor):
    for i in range(table_num):
        create_table_sql = "CREATE TABLE IF NOT EXISTS offer_" + str(i) + " (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT )"
        mycursor.execute(create_table_sql)
        insert_data_sql = "INSERT INTO offer_" + str(i) + " VALUES (null)"
        for _ in range(257):
            mycursor.execute(insert_data_sql)


if __name__ == "__main__":
    width = 200
    height = 100
    pix = get_gray_matrix(width, height)

    # connect database        
    mydb = mysql.connector.connect(
        host='localhost',
        port='4000',
        user='root',
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS PingCAP_offer")
    mycursor.execute("use PingCAP_offer")
    
    create_tables(height, mycursor)

    # draw
    for x in range(width):
        start_time = time.time()
        for y in range(height):
            select_data = "SELECT * FROM offer_" + str(y) + " LIMIT " + str(pix[y, x])
            mycursor.execute(select_data)
            result = mycursor.fetchall()
        
        end_time = time.time()
        duration = end_time - start_time
        if(duration > 60):
            break
        print(x, 'done in', duration, 'seconds')
        time.sleep(60 - duration)

    mydb.close()
               
