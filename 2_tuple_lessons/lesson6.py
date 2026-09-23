# Tuple Operations

tuple1 = tuple(map(int, input("Enter numbers for Tuple 1: ").split()))
tuple2 = tuple(map(int, input("Enter numbers for Tuple 2: ").split()))


print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# 1. Concatenation/arithmetic-addition
print("\n--- Concatenation ---")

combined = tuple1 + tuple2
print("Combined tuple:", combined)


# 2. Repetition/arithmetic-multiplication
print("\n--- Repetition ---")

repeated = tuple1 * 2
print("Repeated tuple1:", repeated)
repeated = tuple2 * 2
print("Repeated tuple2:", repeated)
repeated = combined * 2
print("Repeated combine tuple:", repeated)


# 3. Membership operator
print("\n--- Membership ---")

print(tuple1 in tuple2)
print(tuple2 in tuple1)


# 4. Not in operator
print("\n--- Not in ---")

print(tuple1 not in combined)
print(tuple2[0] not in combined)


# 5. Length of tuple
print("\n--- Length ---")

print("Length of tuple1:", len(tuple1))
print("Length of tuple2:", len(tuple2))
print("Length of combined tuple:", len(combined))