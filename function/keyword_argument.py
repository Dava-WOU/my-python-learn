#def hello(greeting, title, first, last):
#    print(f"{greeting} {title}{first} {last}")

#hello("Hello", title="Mr.", first="John", last="Doe") #bisa di ubah posisinya

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=62, area=882, first=8767, last=3625)

print(phone_num)