#student class is defined
import re

class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades
        
#function to add grades to the student
    def add_grade(self, *grades):
        for grade in grades:
            self.grades.append(grade)
        
#function to calculate the average grade of the student      
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
#function to display the information of the student  
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade()}")
#function to return the grades as a tuple
    
    def grades_tuple(self):
        return tuple(self.grades)
        
#creating instances of the student class and adding grades to them
student1 = Student("Joe", "billyjoe@example.com", [85, 90, 78])
student2 = Student("Jessica", "jessica@example.com", [92, 89, 98])
student3 = Student("Michael", "michael@example.com", [88, 73, 55])
    
student1.add_grade(95, 87)
student2.add_grade(91, 94)
student3.add_grade(82, 79)

#display the information
student1.display_info()
student2.display_info()
student3.display_info()

#modify and catch errors for tuple of grades
grades_tuple = student1.grades_tuple()
print("original tuple:", grades_tuple)

try:
    grades_tuple[0] = 100
except TypeError:
    print("Error: Cannot modify a tuple. Tuples are immutable.")

#student email dictionary 
student_email_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

#function to get student by email using .get()
def get_student_by_email(email):
    return student_email_dict.get(email)


result = get_student_by_email("jessica@example.com")

if result:
    result.display_info()
else:
    print("Student not found")


#create a set of all unique grades across all students and print it
 
students = [student1, student2, student3]

all_unique_grades = set()

for student in students:
    for grade in student.grades:
        all_unique_grades.add(grade)

print("Unique grades:", all_unique_grades)

#remove the last grade from each student
student1.grades.pop()
student2.grades.pop() 
student3.grades.pop()

#print the first and last grade of each student after removing the last grade

for student in [student1, student2, student3]:
    if len(student.grades) > 0:
        print(f"{student.name}'s first grade: {student.grades[0]}")
        print(f"{student.name}'s last grade: {student.grades[-1]}")
    else:
        print(f"{student.name} has no grades.")

#number of grades each student has
print(f"Number of grades received by {student1.name}: {len(student1.grades)}")
print(f"Number of grades received by {student2.name}: {len(student2.grades)}")
print(f"Number of grades received by {student3.name}: {len(student3.grades)}")

#validate email addresses of students using regular expressions

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False 
    
for student in students:
    if validate_email(student.email):
        print(f"{student.email} is valid")
    else:
        print(f"{student.email} is invalid")
    
#amount of grades above 90 for all students
def count_grades_above_90(students):
    count = 0 
    for student in students:
        for grade in student.grades:
            if grade >90:
                count += 1
    return count
print(f"Number of grades above 90: {count_grades_above_90(students)}")
