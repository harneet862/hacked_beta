import sqlite3

def setup_db(path="./test.db"):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS users;')
    cursor.execute('''
        CREATE TABLE users (
            deviceID INT PRIMARY KEY,
            username CHAR(30),
            role CHAR(20),
            status CHAR(20),
            course CHAR(40)
        );
    ''')
    return
# Connect to the database
def connect_db(path="./test.db"):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    return connection, cursor

# Function to add a new user row
def add_user(username, course, role, status, location):
    connection, cursor = connect_db()
    try:
        cursor.execute('''
            INSERT INTO users (deviceID, username, role, status, course) 
            VALUES (?, ?, ?, ?, ?);
        ''', (username, course,role, status, location ))
        connection.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError as e:
        print("Error adding user:", e)
    finally:
        connection.close()

# Function to retrieve users based on course and status
def get_users_by_course_role_and_status(course, role, status):
    connection, cursor = connect_db()
    cursor.execute('''
        SELECT * FROM users WHERE course = ? AND status = ?;
    ''', (course, role,status))
    results = cursor.fetchall()
    connection.close()
    return results
