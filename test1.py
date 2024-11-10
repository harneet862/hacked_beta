from databasefunctions import *

if __name__ == '__main__':
    setup_db()
    add_user("user12", "study buddy", "available", "Chemistry 101","location")

    add_user( "user12", "study buddy", "available", "Chemistry 101",'Cameron 2nd Floor')
    results = get_users_by_course_role_and_status("Math 101", "study buddy","available")
    for user in results:
        print(user)
    
    # all_users = get_all_rows()
    # for user in all_users:
    #     print(user)
    
