

class User:
    def __init__(self,username = None,course=None, role=None,status=None,location=None):
        self.username = username
        self.course = course
        self.role = role 
        self.status = status
        self.location = location

    def courseUpdate(self,course):
        self.course = course

    def roleUpdate(self,role):
        self.role = role

    def statusUpdate(self,status):
        self.status = status

    def locationUpdate(self,location):
        self.location = location

    def usernameUpdate(self,username):
        self.username = username

    def returnCourse(self):
        return self.course
    
    def returnRole(self):
        return self.role
    
    def returnStatus(self):
        return self.status
    
    def returnLocation(self):
        return self.location
    
    def returnUsername(self):
        return self.username
    
    
    def clear(self):
        self.username = None
        self.course = None
        self.role = None
        self.status = None
        self.location = None
    

