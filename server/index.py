from server.db import db_connect
def getAll():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM STUDENTS"
    )
    students = cursor.fetchall()
    conn.close()
    return students

def getById(id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM STUDENTS WHERE id=%s", (id, )
    )
    student = cursor.fetchone()
    conn.close()
    return student

def createStudent(name, email, age):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO STUDENTS (name, email, age) VALUES (%s, %s, %s)", (name, email, age)
        )
        conn.commit()
        conn.close()
    except:
        print("Error while creating student: ")

def updateStudent(id, name, email, age):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE STUDENTS SET name=%s, email=%s, age=%s WHERE id=%s", (name, email, age, id)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error while updating student record: ", e)

def deleteStudentById(id):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM STUDENTS WHERE id=%s", (id, )
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error while Deleting student: ", e)