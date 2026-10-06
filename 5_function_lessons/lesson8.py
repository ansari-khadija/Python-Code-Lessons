# ==============================
# E-COMMERCE ORDER ANALYZER
# ==============================

orders = [
    {"customer": "Alex", "product": "Laptop", "price": 75000, "quantity": 1},
    {"customer": "Mia", "product": "Phone", "price": 40000, "quantity": 2},
    {"customer": "Sam", "product": "Headphones", "price": 5000, "quantity": 3},
    {"customer": "Noah", "product": "Monitor", "price": 18000, "quantity": 2},
    {"customer": "Emma", "product": "Keyboard", "price": 3000, "quantity": 1},
    {"customer": "Ryan", "product": "Laptop", "price": 75000, "quantity": 2}
]


# Calculate Order Total
for order in orders:
    order["total"] = order["price"] * order["quantity"]


# Apply Discount
for order in orders:
    order["discount"] = (
        order["total"] * 0.10
        if order["total"] >= 50000
        else 0
    )


# Calculate Final Amount
for order in orders:
    order["final"] = order["total"] - order["discount"]


# ==============================
# SORT BY FINAL PRICE
# ==============================

orders = sorted(
    orders,
    key=lambda order: order["final"],
    reverse=True
)


print("===== ALL ORDERS =====")

for order in orders:
    print(
        order["customer"],
        "|",
        order["product"],
        "| Final:", order["final"]
    )


# ==============================
# HIGH VALUE ORDERS
# ==============================

high_value = list(
    filter(
        lambda order: order["final"] >= 50000,
        orders
    )
)

print("\n===== HIGH VALUE ORDERS =====")

for order in high_value:
    print(
        order["customer"],
        "|",
        order["product"],
        "| Final:", order["final"]
    )


# ==============================
# MOST EXPENSIVE ORDER
# ==============================

most_expensive = max(
    orders,
    key=lambda order: order["final"]
)

print("\n===== MOST EXPENSIVE =====")

print(
    most_expensive["customer"],
    "|",
    most_expensive["product"],
    "|",
    most_expensive["final"]
)


# ==============================
# LAPTOP ORDERS
# ==============================

laptops = list(
    filter(
        lambda order: order["product"] == "Laptop",
        orders
    )
)

print("\n===== LAPTOP ORDERS =====")

for order in laptops:
    print(
        order["customer"],
        "| Quantity:", order["quantity"],
        "| Final:", order["final"]
    )
