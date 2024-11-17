# logical oprators = condisi multi evaluasi (or, and, not)
#                    or  = hanya ada satu kondisi yg benar/pilih salah satu/salah satu kondisi saja harus di penuhi
#                    and = kondisi keduanya harus benar/ kedua kondisi atau syarat harus di penuhi
#                    not = jika kondisinya(not False, not True)

# contoh or condition
temp = 30
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("event di luar di batalkan")
else:
    print('event nya di laksanakan')