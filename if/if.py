# if = melakukan hanya jika kode dalam kondisi True
#      Else kondisi sebaliknya

age = int(input("masukan umur mu: "))

if age >= 100:
    print("you are too old to sign up")
elif age >= 18:
    print("you are now signed up!")
elif age < 0:
    print("you haven't born yet")
else:
    print("you mus be 18+ to sign up")
    
respon = input("apakah kamu suka makan? (Y/N): ")

if respon == "Y":
    print("Have some food1")
else:
    print("No food for you")
    
for_sale = True

if for_sale:
    print("this item is for sale")
else:
    print("this item isn't for sale")