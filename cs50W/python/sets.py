# create an empty set
s = set()

# Add new elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s) # prints all the added elements

# Try adding a duplicate to a set
s.add(3) # has no effect as no element appears twice in a set
print(s) # prints elements without duplicates

# Remove an element from a set
s.remove(2)
print(len(s)) # print the total number of elements in a set
print(f"The set has {len(s)} elements.") # prints number of elements using an f-string