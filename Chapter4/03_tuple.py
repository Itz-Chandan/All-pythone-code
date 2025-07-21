a = (2, 3, 5, 6, 8)
print(type(a))
b = (1, 4, 5, 9)
print(type(b))

b = (1, 4, 5, 9)
print(sum(b))  # Output: 19

print(min(b)) # Output: 1
print(max(a)) # Output: 8

concatenated = a + b 
print(concatenated) # output: (2, 3, 5, 6, 8, 1, 4, 5, 9)
