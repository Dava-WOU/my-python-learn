def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    else:
        print(kwargs.get("street"))
        
    print(f"{kwargs.get("city")} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake st.",
               apt="#100",
               city="Detroit",
               state="MI",
               zip="54321")