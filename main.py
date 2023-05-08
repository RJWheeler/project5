
def display(collection, e=-1):
    c = collection
    if not e == -1:
        c = collection[:e]
    if len(c) > 0:
        print(f"Pizzas - {len(c)}")
        for i in c:
            print(i)
        print()
        print(f"First pizza: {c[0]}")
        print(f"Last Pizza: {c[- 1]}")
    else:
        print("No pizzas")
    print()


def add_user_pizza(collection):

    p = input("Add your pizza: ")
    if p.lower() in collection:
        print("Error: This pizza already exists.")
    else:
        collection.append(p)


pizzas = ["4 cheese", "deluxe", "3 meats", "hawaiian", "meat lovers"]
add_user_pizza(pizzas)
display(pizzas)

