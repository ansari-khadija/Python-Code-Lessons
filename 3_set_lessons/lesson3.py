# Set Operations

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 1. Union

print("Union:", a | b)

# 2. Intersection

print("Intersection:", a & b)

# 3. Difference

print("Difference:", a - b)

# 4. Difference

print("Difference:", b - a)

# 5. Symmetric Difference

print("Symmetric Difference:", a ^ b)

# 6. Subset

c = {1, 2, 3}
print("Subset:", c <= a)

# 7. Superset

print("Superset:", a >= c)

# 8. Disjoint

d = {10, 20, 30}
print("Disjoint:", a.isdisjoint(d))