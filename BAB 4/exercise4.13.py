foods = ("Nasi", "Ayam", "Ikan", "Sayur", "Buah")

print("Menu awal:")
for food in foods:
    print(food)

# Tuple tidak dapat diubah langsung.
# Untuk mengganti menu, buat tuple baru.
foods = ("Nasi", "Daging", "Ikan", "Sup", "Buah")

print("Menu baru:")
for food in foods:
    print(food)