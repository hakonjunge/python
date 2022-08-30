person1 = 5
person2 = 9
person3 = 2.5
person4 = 21
person5 = 0

antall_kaker = (person1+person2+person3+person4+person5)
gjennomsnitt = int(antall_kaker/5) #her har jeg regnet frem til gjennomsnittet inni en int og dermed fått et helt tall.

print("Første person har spist {} kakestykker".format(person1))
print("Andre person har spist {} kakestykker".format(person2))
print("Tredje person har spist {} kakestykker".format(person3))
print("Fjærde person har spist {} kakestykker".format(person4))
print("Femte person har spist {} kakestykker".format(person5))
print()
print(f"Summen av alle stykkene spist blir {antall_kaker}")

print(f"{antall_kaker}/5 rundet ned til helt tall blir {gjennomsnitt}") #svaret ble 7


