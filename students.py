import pickle
from pprint import pprint as pp


students = [] # empty list for adding new students. each student will be a dictionary{"id": ,"name": }


def get_student_titlecase(students):
    """
    Convert a list of students' names to titlecase

    Args:
        students: a list of students' names

    Return:
        a list of title-cased students' names    
    
    """
    return [student["name"].title() for student in students]


def print_student_titlecase(students_list):
    """
    Prints out title-cased students' names

    Args:
        students_lists: a list of students' names

    Returns:
        prints out title-cased students' names    
    """

    for student in get_student_titlecase(students_list):
        print(student)    



def add_student(student_name, student_id = 999):
    """
    Adds a new student to a list <students>
    """
    student = {"name": student_name,"id":student_id}
    students.append(student)


def ask_user():
    """
    Ask if user wants to add a new student. If Y, add a new student, 
    else prints out a list of title-cased students
    
    """
    ask_user = input("Do you want to add new student? Enter Y or N:")
    while ask_user == "Y":
        student_name_input = input("Enter student name:")
        student_id_input = input ("Enter student ID:")    
        add_student(student_name_input, student_id_input)
        ask_user  = input("Do you want to add new student? Enter Y or N:")
    print_student_titlecase(students)


def save_file(students, filename = "students.pickle"):
    """
    Save the dictionary <students> into a pickle file 
    
    """

    try:
        with open('students.pickle', 'wb') as f:
            pickle.dump(students, f, protocol=pickle.HIGHEST_PROTOCOL)
    except OSError as e:
        print("Unable to write file") 
        print(e)  



def read_file(filename= "students.pickle"):
    """
    Reads the dictionary "students.pickle"

    Returns:
        a dictionary of students with their names and ids

    """
    try:
        with open('students.pickle', 'rb') as f:
            students = pickle.load(f)
            return students
    except OSError as e:
        print("Unable to read file") 
        print(e)           



if __name__ == "__main__":
    
    ask_user() # new session; ask if user wants to add student     
    print("saving student list in 'students.pickle'")
    save_file(students) # save student list in a pickle file
    print("read back saved file 'students.pickle'")
    students = read_file()
    print("prints out student list")
    pp(students)


 