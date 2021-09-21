import sqlite3
from sqlite3 import Error
import pandas as pd    
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c=conn.cursor()
        c.execute('''
          CREATE TABLE IF NOT EXISTS Movies
          ([name] TEXT, [actor] TEXT,[actress] TEXT,[director] TEXT,[year_of_release] TEXT)
          ''')
        
        conn.commit()
    except Error as e:
        print(e)
    finally:
        
        if conn:
            conn.close()

def inst(db_file,a):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c=conn.cursor()
        sql='''INSERT INTO Movies (name, actor, actress, director, year_of_release) VALUES (?,?,?,?,?)'''
        c.execute(sql,a)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def disp(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c=conn.cursor()
        c.execute('''
          SELECT*from Movies
          ''')

        df = pd.DataFrame(c.fetchall(), columns=['name', 'actor', 'actress', 'director', 'year_of_release'])
        print (df)
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
create_connection(r"C:\sqlite3\pythonMovies.db")
print('1.Insert into data base')
print('2.Display table')
choice=int(input("Enter Your Choice:"))
if(choice==1):
    a=list(map(str,input("Enter Movie Details").strip().split(',')))
    print(a)
    inst(r"C:\sqlite3\pythonMovies.db",a)
else:
    disp(r"C:\sqlite3\pythonMovies.db")

    
    

