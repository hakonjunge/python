course_name = "Programmering 42"
print(course_name)
print("course_name")

course_name = "Programmering 1"
print(course_name)

variable = None
print(variable)

course_credits = 10
print(f"Kurset {course_name} vil gi {course_credits} studiepoeng")
#Alternativ v
print("Kurset {} vil gi {} studiepoeng".format(course_name, course_credits))
#Gammel måte v
print("Kurset %s vil gi %d studiepoeng" % (course_name, course_credits))

print('Jeg bruker "gåseøyne" for å sitere ting')

quote = "To climb a mountain you must first become the mountain"
author = "Mahatma Ghandi"
print(" ")
print(" ")
print(f'Sitat: "{quote}" - {author}')
quote, author = "Do you even skate bro", "Joe Biden"
print('Sitat: "{}" - {}'.format(quote, author))
print(" ")
print(" ")
courses_passed = 5
total_credits = course_credits * courses_passed
print(total_credits)