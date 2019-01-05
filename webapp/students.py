class Student:

    school_name = "NUS"

    def __init__(self, student_name, student_lastname, student_id = 313):
        self.name = self.get_name_capitalized(student_name)
        self.student_id =  student_id
        self.last_name = self.get_name_capitalized(student_lastname)
        

    def __str__(self):
        return "Student " + self.name  

    def get_name_capitalized(self, name):
        return name.title()

    def get_school_name(self):
        return self.school_name 