import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                            # your username
                     passwd="in",  # your password
                     db="testdb")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = db.cursor()

# Use all the SQL you like
cursor.execute("SELECT * FROM customer")

results = cursor.fetchall()

widths = []
columns = []
tavnit = '|'
separator = '+' 

for cd in cursor.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])
    print cd[0]

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

print(separator)
print(tavnit % tuple(columns))
print(separator)
print results
# print all the first cell of all the rows


db.close()