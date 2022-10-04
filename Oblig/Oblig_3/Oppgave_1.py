student = {
    "first name" : "Ola",
    "last name" : "Nordmann",
    "favorite course" : "Programmering 1"
}
print(student["first name"], student["last name"])
student['favorite course'] = 'ITF10219 Programmering 1'
student['student age'] = '21'
print()
print(student)
print(f"\n{student.get('first name')} {student.get('last name')} is {student.get('student age')} years old, "
      f"and attends the {student.get('favorite course')} course")