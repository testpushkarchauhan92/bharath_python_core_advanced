# Download using CMD
# python3 -m pip install --upgrade pip
# pip --version
# LDFLAGS=-L/usr/local/opt/openssl/lib pip3 install mysql-connector-python

# Format MySQL
# https://www.tutorialspoint.com/online_python_formatter.htm
import mysql.connector;

def delete(id):
    conn = mysql.connector.connect(host='localhost',database='mypythondb',user='root',password='root')

    if conn.is_connected():
        print("Connected to mysql db")

    cursor = conn.cursor()


    try:
#       cursor.execute("delete from emp where id='%d'")
        cursor.execute("insert into emp values(12,'Kunal',1100)")
        conn.commit()
        print("Employee Added")
    except:
        conn.rollback()

    cursor.close()
    conn.close()
