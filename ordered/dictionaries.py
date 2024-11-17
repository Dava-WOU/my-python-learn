capitals = {"USA": "Washington D.C>",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}#sebelah kiri adalah key dan di sebrang tanda ":" adalah nilainya

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("USA"))#untuk mengambil nilai dari key tertentu

#if capitals.get("Japan"):
#    print("That capitals exists")
#else:
#    print("That capitals does not exist")#untuk mengecek apakah key ada atau tidak

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})#untuk mengupdate key atau nilai, key dan nilai
#capitals.pop("China")#untuk menghapus key sekaligus nilai yg ada di dictionaries
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()#menampilkan key yg ada pada dictionaries dan menglompokan lagi menjadi list
#print(keys)
#for key in capitals.keys():
#    print(key)

#values = capitals.values()#menampilkan nilai yg ada pada dictionaries dan menglompokan lagi menjadi list
#print(values)
#for value in capitals.values():
#    print(value)

#items = capitals.items()#menampilkan item yg ada di dictionaries dan menglompokan semua menjadi list dan menglomokan lagi menjadi tuple
#print(items)
#for key, value in capitals.items():
#    print(f"{key}: {value}")