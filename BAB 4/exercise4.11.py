pizzas = ["Pepperoni", "Cheese", "Beef"]
friend_pizzas = pizzas[:]

pizzas.append("Mushroom")
friend_pizzas.append("Chicken")

print("Pizza saya:")
for pizza in pizzas:
    print(pizza)

print("Pizza teman saya:")
for pizza in friend_pizzas:
    print(pizza)