from psycopg2 import sql
import psycopg2

conn = psycopg2.connect(dbname='go-crud', user='postgres', host='localhost', password='RjirfLeyz')
cur = conn.cursor()

cur.execute("DELETE FROM public.debts WHERE id = %s", ("7"))

cur.execute("INSERT INTO public.debts (id, name, status) VALUES (%s, %s, %s)",
    (7, "123", 5))
conn.commit()

cur.execute("SELECT id, name, status FROM debts")

#result = cur.fetchall()
#print(result)

if 0 > 1:
    for data in cur:
        print("----------------------")
        print("ID :" + str(data[0]))
        print("NAME :" + data[1])
        print("STATUS :" + str(data[2]))
else:
    rows = cur.fetchall()
    for data in rows:
        print("----------------------")
        print("ID :" + str(data[0]))
        print("NAME :" + data[1])
        print("EMAIL :" + str(data[2]))