places = ["Jepang", "Swiss", "Paris", "Korea Selatan", "Madinah"]

print("Daftar awal:")
print(places)

print("\nUrutan alfabetis:")
print(sorted(places))

print("\nDaftar asli:")
print(places)

print("\nUrutan alfabetis terbalik:")
print(sorted(places, reverse=True))

places.reverse()
print("\nSetelah reverse():")
print(places)

places.reverse()
print("\nSetelah reverse() kedua:")
print(places)

places.sort()
print("\nSetelah sort():")
print(places)

places.sort(reverse=True)
print("\nSetelah sort(reverse=True):")
print(places)