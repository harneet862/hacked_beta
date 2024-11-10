import sqlite3

def setup_db(path="./test.db"):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    #cursor.execute('DROP TABLE IF EXISTS users;')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username CHAR(30) PRIMARY KEY,
            role CHAR(20),
            status CHAR(20),
            course CHAR(40),
            location CHAR(80)
        );
    ''')
    #cursor.execute('''
    #        INSERT INTO users (username, role, status, course,location) 
    #        VALUES (?, ?, ?, ?, ?);
    #    ''', ("yellow","Study Buddy", None, "CMPUT 204", None ))
    connection.commit()
    return
# Connect to the database
def connect_db(path="./test.db"):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    return connection, cursor

# Function to add a new user row
def add_user(username,role, status, course, location):
    connection, cursor = connect_db()
    try:
        cursor.execute('''
            INSERT INTO users (username, role, status, course,location) 
            VALUES (?, ?, ?, ?, ?);
        ''', (username,role, status, course, location ))
        connection.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError as e:
        print("Error adding user:", e)
    finally:
        connection.close()

# Function to retrieve users based on course and status
def get_users_by_course_role_and_status(course, role, status):
    print(course, role, status)
    connection, cursor = connect_db()
    cursor.execute('''
         SELECT * FROM users WHERE course = ? AND role like ? AND status = ?;
    ''', (course, role,'available'))
    #cursor.execute('''
    #   SELECT * FROM users WHERE course = ? AND role = ?;
    #''', (course, role))
    results = cursor.fetchall()
    connection.close()
    return results



def get_all_usernames():
    connection, cursor = connect_db()
    cursor.execute('SELECT username FROM users')
    usernames = [row[0] for row in cursor.fetchall()]  # Extract usernames from the rows
    connection.close()
    return usernames

def clear_users_table():
    connection, cursor = connect_db()
    cursor.execute('DELETE FROM users')
    connection.commit()  # Apply the deletion
    connection.close()
    print("All rows have been cleared from the users table.")

def get_user_by_username(username):
    connection, cursor = connect_db()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()  # Fetch the single row matching the username
    connection.close()
    return user