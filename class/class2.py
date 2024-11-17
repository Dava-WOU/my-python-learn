class Student:
    
    class_var = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("Spongebob", 20)
student2 = Student("Patrick", 21)

print(student1.name)
print(student2.age)
