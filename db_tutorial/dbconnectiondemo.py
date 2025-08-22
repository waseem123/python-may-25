import mysql.connector as connector
from mysql.connector import cursor


def dbconnect():
    connection = None
    try:
        connection = connector.connect(host='localhost', database='db_cars', user='root', password='admin')
        print(connection)
    except Exception as e:
        print(e)
    return connection


def save_data():
    print('saving data')
    c = dbconnect()
    sql = "INSERT INTO tbl_car(car_brand,car_model,car_price)VALUES('Porsche','911 GT3',30000000)"
    print(sql)
    cursor = c.cursor()
    cursor.execute(sql)
    c.commit()
    cursor.close()
    c.close()

def update_data():
    print('updating data')
    c = dbconnect()
    sql = "UPDATE tbl_car SET car_brand = 'Lamborghini',car_model='Veneno',car_price=4500000 WHERE car_id=7;"
    cursor=c.cursor()
    cursor.execute(sql)
    c.commit()
    cursor.close()
    c.close()

def delete_data():
    car_id = int(input("ENTER CAR ID to DELETE - "))
    print('deleting data')
    c = dbconnect()
    sql = f"DELETE FROM tbl_car WHERE car_id={car_id};"
    cursor=c.cursor()
    cursor.execute(sql)
    c.commit()
    cursor.close()
    c.close()

print("1. INSERT")
print("2. UPDATE")
print("3. DELETE")
print("4. SELECT ALL")
print("5. SELECT ONE")
choice = int(input("ENTER YOUR CHOICE - "))
match choice:
    case 1:
        save_data()
        print("DATA SAVED SUCCESSFULLY")
    case 2:
        update_data()
        print("DATA UPDATED")
    case 3:
        delete_data()

