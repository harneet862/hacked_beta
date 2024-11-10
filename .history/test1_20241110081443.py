from databasefunctions import *

if __name__ == '__main__':
    setup_db()
    
    # results = get_users_by_course_role_and_status("Math 101", "study buddy")
    # for user in results:
    #     print(user)
    
    clear_users_table()
    
