import mysql.connector as db
import json

with open('keys.json') as json_file:
    keys = json.load(json_file)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0

def write_file(data, path):
    # Convert binary data to proper format and write it on your computer
    with open(path, 'wb') as file:
        file.write(data)

def registerUser(name, password, photo):
    id = 0
    inserted = 0

    try:
        con = db.connect(host=keys["host"], user=keys["user"], password=keys["password"], port=keys["port"], database=keys["database"])
        cursor = con.cursor()
        sql = "INSERT INTO `user`(nombre, password, photo) VALUES (%s,%s,%s)"
        pic = convertToBinaryData(photo)

        if pic:
            cursor.execute(sql, (name, password, pic))
            con.commit()
            inserted = cursor.rowcount
            id = cursor.lastrowid
    except db.Error as e:
        print(f"Failed inserting image: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    return {"id": id, "affected":inserted}

def registerUserBot(name, password):
    id = 0
    inserted = 0

    try:
        con = db.connect(host=keys["host"], user=keys["user"], password=keys["password"], port=keys["port"], database=keys["database"])
        cursor = con.cursor()
        sql = "INSERT INTO `user`(nombre, password) VALUES (%s,%s)"

        cursor.execute(sql, (name, password))
        con.commit()
        inserted = cursor.rowcount
        id = cursor.lastrowid
    except db.Error as e:
        print(f"Failed inserting user: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    return {"id": id, "affected":inserted}

def getUser(name, path):
    id = 0
    rows = 0

    try:
        con = db.connect(host=keys["host"], user=keys["user"], password=keys["password"], port=keys["port"], database=keys["database"])
        cursor = con.cursor()
        sql = "SELECT * FROM `user` WHERE nombre = %s"

        cursor.execute(sql, (name,))
        records = cursor.fetchall()

        for row in records:
            id = row[0]
            write_file(row[3], path)
        rows = len(records)
    except db.Error as e:
        print(f"Failed to read image: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    return {"id": id, "affected": rows}

def getUserCredentials(nombre, password):
    row = None

    try:
        con = db.connect(host=keys["host"], user=keys["user"], password=keys["password"], port=keys["port"], database=keys["database"])
        cursor = con.cursor()
        sql = "SELECT * FROM `user` WHERE nombre = %s AND password = %s"

        cursor.execute(sql, (nombre, password))
        row = cursor.fetchone()
    except db.Error as e:
        print(f"Failed to retrieve user credentials: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    return {"affected": row}