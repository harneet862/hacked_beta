from databasefunctions import *

if __name__ == '__main__':
    setup_db()
    add_user(12, "user12", "study buddy", "available", "Chemistry 101")
    results = get_users_by_course_and_status("Math 101", "available")
    for user in results:
        print(user)
    
    