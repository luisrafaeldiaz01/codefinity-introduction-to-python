produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for section in groceries:
    print(section)
    for Item in section:
        print("Item name: ", Item)