import sqlite3 as sql


def db_init():
    from os.path import exists
    if exists('test.db'):
        return
    conn = sql.connect("railways.db")
    
    conn.execute('''CREATE TABLE locomotive_types(
        locomotive_type_id integer PRIMARY KEY NOT NULL,
        type_name TEXT NOT NULL
    );''')
    
    conn.commit()
    conn.close()
    
        
def add_carriage_types():
    pass


def add_carriages():
    pass

def db_init():
    add_carriage_types()
    add_carriages()



from os.path import exists
if not exists('railways.db'):
    db_init()
conn = sql.connect('railways.db')
cursor = conn.cursor()
cursor.execute('select * from locomotives')
res = cursor.fetchall()
for r in res:
    print(r)
conn.close()