motorcycles = ["Honda", "Yamaha", "Suzuki"]

# Menampilkan daftar
print(motorcycles)

# Mengakses elemen
print(motorcycles[0])

# Mengubah elemen
motorcycles[0] = "Ducati"
print(motorcycles)

# Menambahkan elemen
motorcycles.append("Kawasaki")
print(motorcycles)

motorcycles.insert(1, "BMW")
print(motorcycles)

# Menghapus elemen
del motorcycles[0]
print(motorcycles)

motorcycles.pop()
print(motorcycles)

motorcycles.remove("Yamaha")
print(motorcycles)

# Mengurutkan daftar
motorcycles.sort()
print(motorcycles)

motorcycles.reverse()
print(motorcycles)

# Menghitung jumlah elemen
print(len(motorcycles))