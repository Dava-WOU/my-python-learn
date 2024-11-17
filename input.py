#input() = berfungsi untuk membolehkan user memasukan data saat program di jalankan
#          dan data yg di masukan akan menajadi tipe data string.

nama = input("siapa namamu?: ")
umur = int(input("berapa usiamu?: "))

#atau bisa juga menggunakan:
#umur = int(umur)
umur = umur + 1

print(f"halo {nama}!")
print("SELAMAT ULANG TAHUN!!")
print(f"usiamu {umur} tahun")