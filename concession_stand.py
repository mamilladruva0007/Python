menu={
    "pizza":100,
    "fries":70,
    "coke":25,
    "chips":20,
    "soda":30,
    "pretzel":40,
    "water":15,
    "juice":30
}
cart=[]
total=0

for key,value in menu.items():
    print(f"{key:10}: {value:.2f}")

while True:
    food=input("select an item (or 'quit' to exit):").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total+=menu[food]
        print("Item added to cart")
    else:
        print("Item not found")


for food in cart:
    total+=menu.get(food)
    print(food,end="\t")

print()
print(total)

    
