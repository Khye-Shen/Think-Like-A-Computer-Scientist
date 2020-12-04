import sqlite3
conn = sqlite3.connect('database.sqlite')
def database():
    with conn:
        conn.execute("CREATE TABLE realones(id INTEGER PRIMARY KEY, Name TEXT, Age INTEGER)")
        conn.execute("INSERT INTO realones(Name, Age) Values('Jack Yeo', 11)")
        conn.execute("INSERT INTO realones(Name, Age) Values('President Obama', 32)")
database()

def printdatabase():
    with conn:
        ye = conn.execute("SELECT id, Name, Age from realones")
        for row in ye:
            print("ID", row[0])
            print("NAME", row[1])
            print("AGE", row[2], "years old")

printdatabase()


def searchbyage():
    minage = int(input("Input age"))
    with conn:
        ye = conn.execute("SELECT Age, Name FROM realones where Age>=?   ", (minage,))
        for row in ye:
            print(row[0], "and his name is", row[1])
searchbyage()