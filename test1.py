from databasefunctions import *

if __name__ == '__main__':
    setup_db()
<<<<<<< HEAD
    add_user("user12", "study buddy", "available", "Chemistry 101","location")
    results = get_users_by_course_and_status("Math 101", "available","location")
=======
    add_user( "user12", "study buddy", "available", "Chemistry 101",'Cameron 2nd Floor')
    results = get_users_by_course_role_and_status("Math 101", "study buddy","available")
>>>>>>> b77ed06ae30a2b5bdae4fe62c800446db6c7e56f
    for user in results:
        print(user)
    
    all_users = get_all_rows()
    for user in all_users:
        print(user)
    
