import sqlite3
#conn_user = sqlite3.connect('user.db')
#cu = conn_user.cursor()
#cu.execute("""CREATE TABLE users (
#            login text,
#            password text
#            )""")
#cu.execute("INSERT INTO users VALUES ('user2', 'user2')")
#cu.execute("SELECT * FROM users")
#print(cu.fetchall())
#conn_user.commit()
#conn_user.close()
#conn_trans = sqlite3.connect('transaction.db')
#ct = conn_trans.cursor()
#ct.execute("""CREATE TABLE trans (
#            user text,
#            trans text,
#            value text,
#            time text
#            )""")
#ct.execute("INSERT INTO trans VALUES ('user1', 'Take cash', '80', '14:23')")
#ct.execute("SELECT * FROM trans")
#print(ct.fetchall())
#conn_trans.commit()
#conn_trans.close()
#conn_bal = sqlite3.connect('balance.db')
#cb = conn_bal.cursor()
#cb.execute("""CREATE TABLE balances (
#            login text,
#            balance text
#            )""")
#cb.execute("INSERT INTO balances VALUES ('user2', '5000')")
#cb.execute("SELECT * FROM balances")
#print(cb.fetchall())
#conn_bal.commit()
#conn_bal.close()
conn_case = sqlite3.connect('case.db')
cc = conn_case.cursor()
#cc.execute("""CREATE TABLE cases (
#            b1000 text,
#            b500 text,
#            b200 text,
#            b100 text,
#            b50 text,
#            b20 text,
#            b10 text
#            )""")
#case_sql = 'INSERT INTO cases VALUES ' + str(a, b, c, d, e, f, j)
case = {1000: 31, 500: 51, 200: 201, 100: 301, 50: 601, 20: 600, 10: 600}
case_sql = tuple(str(i) for i in case.values())
#print(case_sql)
case_sql1 = '"'+'INSERT INTO cases VALUES ' + str(case_sql)+'"'
cc.execute(case_sql1)
#print(case_sql1)
if case_sql1 == "INSERT INTO cases VALUES ('50', '200', '300', '600', '600', '600')":
    print(True)
else:
    print(False)
    
#cc.execute("INSERT INTO cases VALUES ('50', '200', '300', '600', '600', '600')")
#cc.execute("SELECT * FROM cases WHERE ROWID IN ( SELECT max( ROWID ) FROM cases )")
#case_list_init = cc.fetchall()
#case_list = list((case_list_init[0]))
#banknote_list = [1000, 500, 200, 100, 50, 20, 10]
#case_init = dict(zip(banknote_list, case_list))
#case = {int(i): int(j) for i, j in case_init.items()}
#print(case)
conn_case.commit()
conn_case.close()
