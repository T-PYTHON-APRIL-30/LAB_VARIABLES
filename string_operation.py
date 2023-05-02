
#string operations

student_name = "Abdulaziz"
course_name = "Building websites with Python"
random_number = "20"


print(student_name.upper())

print(student_name.startswith("Abdul"))

print(course_name.endswith("Python"))

print(course_name.count("with"))

print(random_number.isdigit())


#string interpolation, formatting , concatination
about_student = student_name + " is studying " + course_name

print(about_student)

about_student2 = "{} is studying {}".format(student_name, course_name)
print(about_student2)

about_student3 = f"{student_name} is studying {course_name}"
print(about_student3)


print("-"*14)
