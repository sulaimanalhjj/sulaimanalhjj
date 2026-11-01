guests = ["Eko", "Andi", "Fajar", "Doni", "Citra", "Gilang"]

print("Maaf, meja makan yang tersedia hanya untuk dua orang.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, undangan dibatalkan.")

for guest in guests:
    print(f"Halo {guest}, kamu tetap diundang.")

del guests[0]
del guests[0]

print("Daftar tamu terakhir:")
print(guests)