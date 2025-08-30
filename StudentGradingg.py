def student_grade(marks):
    if marks >=90:
        return "A+"
    elif marks >=85:
        return "A"
    elif marks >= 75:
        return "B+"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C+"
    elif marks >=40:
        return "C"
    else:
        return "Fail"
        
students_num =int(input("enter number of students: "))
 
for i in range(students_num):
    print(f"\n enter details of student{i+1} ")
    student_name = input("enter student name: ")
    subjects_num= int(input("enter number of subjects: "))
    subjects ={}
    total = 0
        
    for j in range(subjects_num):
        subject = input(f"enter subject {j+1} name: ")
        marks = int(input(f"enter marks for {subject}: "))
        subjects[subject] = marks
        total +=marks
        
    percentage = total / subjects_num
    print(f"\n report card for {student_name}")
    for subject, mark in subjects.items():
        print(f"{subject}:Marks = {mark},Grade = {student_grade(mark)}")
    print(f"Total percentage:{percentage:.2f}%")
    print(f"final grade:{student_grade(percentage)}")
    
    
