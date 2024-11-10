

class User:
    def __init__(self,course=None, role=None,status=None,location=None):
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

    def returnCourse(self):
        return self.course
    
    def returnRole(self):
        return self.role
    
    def returnStatus(self):
        return self.status
    
    def returnLocation(self):
        return self.location
    
    def clear(self):
        self.course = None
        self.role = None
        self.status = None
        self.location = None
    

