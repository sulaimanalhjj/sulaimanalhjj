guests = ["Andi", "Doni", "Citra"]

print("Saya menemukan meja makan yang lebih besar.")

guests.insert(0, "Eko")
guests.insert(2, "Fajar")
guests.append("Gilang")

print(guests)

for guest in guests:
    print(f"Halo {guest}, kamu diundang makan malam.")