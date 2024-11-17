doubles = [x * 2 for x in range(1, 11)]# x di kali dua untuk x di range 1 sampai 10
triples = [y * 3 for y in range(1, 11)]
squares = [z ** 2 for z in range(1, 11)]
print(doubles)
print(triples)
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits] # ubah semua huruf ke huruf besar
# fruits_chars = [fruit[0] for fruit in fruits]  # mengambil karakter pertama dari setiap buah
print(fruits)

numbers = [1, -2, 3, -4, 5, -6, -7, 8]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [85, 42, 79, 90, 56, 51, 30]
passing_frades = [grade for grade in grades if grades >= 60]
print(passing_frades)