student = {"first name": "Ola", "last name": "Nordmann", "favorite course": "Programmering 1"
}
print(student["first name"], student["last name"])
student['favorite course'] = 'ITF10219 Programmering 1'
student['student age'] = '21'
print()
print(student)
# Printer ut alt for å se i terminalen at det fungerer
print(f"\n{student['first name']} {student['last name']} is {student['student age']} years old, "
      f"and attends the {student['favorite course']} course")
