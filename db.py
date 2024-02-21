import sqlite3
con = sqlite3.connect("pmstracker.db")

cur = con.cursor()


res = cur.execute("SELECT * from users")
print(res.fetchall())



