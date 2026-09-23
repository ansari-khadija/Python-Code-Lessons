# List Operations

lst1 = list(map(int, input("Enter numbers for List 1: ").split()))
lst2 = list(map(int, input("Enter numbers for List 2: ").split()))


print("List 1:",lst1)
print("List 2:",lst2)

# 1. Concatenation/arithmetic-addition
print("\n--- Concatenation ---")

combined = lst2 + lst2
print("Combined list:", combined)


# 2. Repetition/arithmetic-multiplication
print("\n--- Repetition ---")

repeated = lst1 * 2
print("Repeated list 1:", repeated)
repeated = lst2 * 2
print("Repeated list 2:", repeated)
repeated = combined * 2
print("Repeated combine list:", repeated)


# 3. Membership operator
print("\n--- Membership ---")

print(lst1 in lst2)
print(lst2 in lst1)


# 4. Not in operator
print("\n--- Not in ---")

print(lst1 not in combined)
print(lst2[0] not in combined)


# 5. Length of tuple
print("\n--- Length ---")

print("Length of tuple1:", len(lst1))
print("Length of tuple2:", len(lst2))
print("Length of combined tuple:", len(combined))