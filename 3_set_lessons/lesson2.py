# Set Methods
# Creating sets

a = {"Python", "Java", "C++"}
b = {"Java", "HTML", "CSS"}

# 1. add()

a.add("SQL")
print(a)

# 2. remove()

a.remove("C++")
print(a)

# 3. discard()

a.discard("Java")
print(a)

# 4. pop()

a.pop()
print(a)

# 5. clear()

c = {"Python", "Java", "C++"}
c.clear()
print(c)

# 6. union()

a = {"Python", "Java", "C++"}
b = {"Java", "HTML", "CSS"}
print(a.union(b))

# 7. intersection()

print(a.intersection(b))

# 8. difference()

print(a.difference(b))

# 9. symmetric_difference()

print(a.symmetric_difference(b))

# 10. update()

a.update(b)
print(a)