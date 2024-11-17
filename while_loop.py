 #while loop = execute some code WHILE some condition remains true

nama = input('masukan nama mu: ')
food = input("masukan makanan favorit mu (q/Q to quit): ")
num = int(input("masukan sebuah angka antara 1 - 10:"))
 
while nama == "":
    print("nama tidak boleh kosong")
    nama = input('masukan nama mu: ')
print("selamat datang", nama)

while not food == "q":
    print(f"kamu suka {food}")
    food = input("masukan makanan favorit mu (q/Q to quit): ")
print("bye")
    
while num < 1 or num > 10:
    print("angka harus antara 1 - 10")
    num = int(input("masukan sebuah angka antara 1 - 10:"))
print(f"angka yang kamu masukan adalah {num}")