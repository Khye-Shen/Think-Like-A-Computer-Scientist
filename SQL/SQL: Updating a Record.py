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

def searchbyage():
    minage = int(input("Input age"))
    with conn:
        ye = conn.execute("SELECT Age, Name FROM realones where Age>=?   ", (minage,))
        for row in ye:
            print(row[0], "and his name is", row[1])
def hello():
    while True:
        try:
            newonename = input("Please enter name of the new one")
            newoneage = int(input("Please enter age of the new one"))
            with conn:
                conn.execute("INSERT INTO realones(Name, Age) VALUES(?,?)", (newonename, newoneage))
                printdatabase()
            break
        except ValueError:
            print("value error")
def byebye():
    while True:
        try:
            x = input("Hey wanna delete someone?('yes' or 'no')")
            if x == 'yes':
                printdatabase()
                whogone = int(input("Input the id of who you dont think is a real one"))
                while True:
                    try:
                        areyasure = input("Are ya sure?")
                        if areyasure == 'yes':
                            with conn:
                                conn.execute("DELETE FROM realones WHERE id =?", (whogone,))
                                print("OK he gone")
                                printdatabase()

                        else:
                            print('ok')
                        break
                    except ValueError:
                        print('nah')
            else:
                break
        except ValueError:
            print('value error')

def changearealone():
    with conn:
        while True:
            printdatabase()
            x = int(input("enter id of which real one you wanna change:"))
            ye = conn.execute("SELECT id, Name, Age FROM realones WHERE id = ?",(x,))
            row = ye.fetchone()
            print("ID", row[0])
            print("Name", row[1])
            print("Age", row[2], "years")
            y = input("What do you wanna change? Name or Age?:")
            if y == "Name":
                newname = input("What is the newname?:")
                conn.execute("UPDATE realones SET Name=? WHERE id=?", (newname, x))
                print("New name is", row[1])
                break
            elif y == "Age":
                newage = int(input("What is the new age?:"))
                conn.execute("UPDATE realones SET Age=? WHERE id=?", (newage, x))
                print("New age is", row[2], "years")
                break
            else:
                print('what')
changearealone()