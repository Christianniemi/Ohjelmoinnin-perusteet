Children = 3
Hometown = "Lahti"

TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

RandomInformation = ["Mira", 48, Children, Hometown]

print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NumOfTowns = len(TownsInFinland)
print(TownsInFinland[NumOfTowns-1])

Municipality = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

MunicipalityAndTowns = [Municipality, Towns]
print(MunicipalityAndTowns[1][-2])

Towns.sort()
print(Towns)

teacher = {
    'name': 'Juha',
    'age': 50,
    'city': 'Lahti'
}

print(teacher["name"])
teacher['email'] = 'juha.hyytiainen@lab.fi'
print(teacher)

for key in teacher:
    print(key, end=" ")
    print(teacher[key])

Student = [
    {"name": "Mikko", "age": 25, "city": "Tampere"},
    {"name": "Maija", "age": 30, "city": "Espoo"},
    {"name": "Seppo", "age": 35, "city": "Helsinki"}
]

print(Student[0])

Cities = {
    "Finland": ["Tampere", "Espoo", "Helsinki"],
    "Sweden": ["Stockholm", "Malmo"]
}
print(Cities["Finland"][0])

for town in Towns:
    print(f"The town of {town}")
print(f"All the towns {Towns}")

for i in range (1,10):
    print(i)

for i in range (1,10):
    print(i, end=" ")
print("")
for i in range (1,10, 3):
    print(i)

print("")
Total = 0
for i in range (1,101):
    Total +=i
    print(Total)
print(Total)

for i in range (9):
    if (i == 3):
        continue
    print(i)

#while 1 < 10:
    #print("Do not try me at home xD")#

i = 0
while i < 10:
    print(f"Iteration number: {i}")
    i = i + 1

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False

while True:
    if input("Do you want to continue ") != "yes":
        break
    else:
        continue