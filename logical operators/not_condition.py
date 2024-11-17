# logical oprators = condisi multi evaluasi (or, and, not)
#                    or  = hanya ada satu kondisi yg benar/pilih salah satu/salah satu kondisi saja harus di penuhi
#                    and = kondisi keduanya harus benar/ kedua kondisi atau syarat harus di penuhi
#                    not = jika kondisinya(not False, not True)

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("Hari ini sangat panas dan cerah")
    print("ini hari yang cerah")
elif temp <= 0 and is_sunny:
    print("hari ini sangat dingin")
    print("ini hari yang cerah")
elif temp < 28 and temp > 0 and is_sunny:
    print("Hari ini sangat hangat dan cerah")
    print("ini hari yang cerah")
elif temp >= 28 and not is_sunny:
    print("Hari ini sangat panas dan cerah")
    print("ini hari yang berawan")
elif temp <= 0 and not is_sunny:
    print("hari ini sangat dingin")
    print("ini hari yang berawan")
elif temp < 28 and temp > 0 and not is_sunny:
    print("Hari ini sangat hangat dan cerah")
    print("ini hari yang berawan")