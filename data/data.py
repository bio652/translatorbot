import sqlite3

db = 'data/users.db'    
conn = sqlite3.connect(db)
cursor = conn.cursor()
print("database was connected")

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    userid TEXT PRIMARY KEY,
    userlang TEXT,
    trlang TEXT,
    tolang TEXT
)
''')

def checkUser(userid):
    try:
        cursor.execute("SELECT COUNT(1) FROM users WHERE userid = ?", (userid,))
        result = cursor.fetchone()[0] > 0
        return result
    except Exception as e:
        print(e)
        return False

def addUser(userid, userlang):
    try:
        cursor.execute('''
        INSERT INTO users (userid, userlang, trlang, tolang) VALUES (?, ?, ?, ?)
        ''', (userid, userlang, "en", "es"))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False

def updatemenulang(userid, userlang):
    try:
        cursor.execute('''
        UPDATE users SET userlang = ? WHERE userid = ?
        ''', (userlang, userid))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def getUserlang(userid):
    try:
        cursor.execute("SELECT userlang FROM users WHERE userid = ?", (userid,))
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        print(e)
        return False
    
def getTranslangs(userid):
    try:
        cursor.execute("SELECT trlang, tolang FROM users WHERE userid = ?", (userid,))
        result = cursor.fetchone()
        return [result[0], result[1]]
    except Exception as e:
        print(e)
        return False
    
def trlangupdate(userid, newlang):
    try:
        cursor.execute('''
        UPDATE users SET trlang = ? WHERE userid = ?
        ''', (newlang, userid))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def tolangupdate(userid, newlang):
    print(newlang)
    try:
        cursor.execute('''
        UPDATE users SET tolang = ? WHERE userid = ?
        ''', (newlang, userid))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False