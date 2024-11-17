def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street='123 Main St', city='Anytown', state='CA', zip_code="54321")