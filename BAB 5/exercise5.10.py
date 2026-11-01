current_users = ["Andi", "Budi", "Citra", "Doni", "Eko"]
new_users = ["andi", "Fajar", "Gilang", "budi", "Hani"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Nama {new_user} sudah digunakan. Pilih nama lain.")
    else:
        print(f"Nama {new_user} tersedia.")