import sqlite3
import random
conn = sqlite3.connect('Fastcars.sqlite')
def create_top50_db0():
    with conn:
        conn.execute("CREATE TABLE Cars(id INTEGER PRIMARY KEY, Name TEXT, TopSpeed INT)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Porsche 911 Carrera 4s',185)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Audi R8',187)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Dodge Viper SRT 10',190)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Mosler MT900',190)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Corvette Z06',190)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Aston Martin V12 Vantage',190)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('43 Aston Martin DB9',190)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Aston Martin DB9',190)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Cadillac CTS-V',191)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Aston Martin DBS',191)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Porsche 911 Turbo',193)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Nissan Gt-R',193)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('TVR Tuscan',195)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Lamborghini Gallardo Superleggera',196)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ferrari F430',196)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Audi R8 V10',196)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Alpina B5 S',197)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ferrari 612 Scaglietti',199)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Bentley Flying Spur Speed',200)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Bentley Continental GT',200)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ascari KZ1',200)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ferrari F40',201)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Lamborghini Gallardo LP 560-4',202)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ferrari 575m',202)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ferrari F50',202)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Porsche 911 GT2',204)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Corvette ZR1',205)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ferrari 599GTB',205)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Maserati MC12',205)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ford GT',205)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Caparo T1',205)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('BMW M5',205)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Mercedes Benz SLR Mclaren',207)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Porsche Carrera GT',209)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Lamborghini Diablo GT',211)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Lamborghini Murcielago LP 640',213)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Pagani Zonda F',215)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ferrari Enzo',217)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Gumpert Apollo',224)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Bristol Fighter T',225)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Jaguar XJ220',227)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Ultima GT-R640',231)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('TVR Cebera Speed 12',240)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Mclaren F1',240)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Koenigsegg CCX',241)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Saleen S7 Twin Turbo',248)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Bugatti Veyron',253)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Koenigsegg CCXR',254)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('9ff GT9',254)")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('SSC Ultimate Aero',257)")
def print_one_row():
    with conn:
        PrintCar = input("Car ID:")
        cur = conn.execute("SELECT id, Name, TopSpeed FROM Cars WHERE id = ?", (PrintCar,))
        row = cur.fetchone()
        print ("ID:",row[0],"Name:",row[1],"Top Speed:",row[2],"mph")
print_one_row()