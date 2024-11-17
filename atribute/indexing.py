# indexing adalah cara untuk mengakses elemen tertentu dalam sebuah array menggunakan [] indeks oprator
#           [start:end:step]

credit_number = "1234-5678-9012-3456"

#credit_number = credit_number[::-1] output will be 6543-2109-8765-4321

last_digits = credit_number[-4:]

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-5])
print(credit_number[::2])
print(f"xxxx-xxxx-xxxx-xxxx-{last_digits}")