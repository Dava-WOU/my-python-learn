students = {"Spongebob",  "Patrick", "Sandy", "Squidward"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")
    
grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

email = "Dava45@gmail.com"

if "@" in email and "." in email:
    print("This is a valid email")
else:
    print("This is not a valid email")