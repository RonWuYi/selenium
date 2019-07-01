import psycopg2


conn = psycopg2.connect(database="testdb", user="postgres", password="postgres", host="172.16.66.244")
cur = conn.cursor()
cur.execute("SELECT * from bugs where checked = FALSE order by (name, cp) desc;")
print(cur.fetchone())

print("##########################################################")
flag = 0
for i in cur.fetchall():
    flag += 1
    print(i)
    print(type(i[1]))
    if flag >= 5:
        break
    else:
        continue
