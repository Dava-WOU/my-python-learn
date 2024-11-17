# conditional expression adalah if statement yg lebih singkat

num = 5
a = 6
b = 7
age = 17
temprature = 30
user_role = "admin"

#print("positive" if num > 0 else "negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#status = "adult" if age >= 18 else "child"
#weather = "hot" if temprature > 20 else "cold"
access_level = "full access" if user_role == "admin" else "limited access"

print(access_level)