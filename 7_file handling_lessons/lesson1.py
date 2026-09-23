import csv

# Take shopping details from user
product = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

# Save CSV inside shopping_data folder
with open("shopping_data/shopping.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Product", "Price", "Quantity"])
    writer.writerow([product, price, quantity])

print("Shopping details saved successfully!")
