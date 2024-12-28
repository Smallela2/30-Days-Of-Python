# 1. Iterate 0 to 10 using for loop and while loop
print("Iterate 0 to 10 using for loop:")
for i in range(11):
    print(i)

print("\nIterate 0 to 10 using while loop:")
i = 0
while i <= 10:
    print(i)
    i += 1

# 2. Iterate 10 to 0 using for loop and while loop
print("\nIterate 10 to 0 using for loop:")
for i in range(10, -1, -1):
    print(i)

print("\nIterate 10 to 0 using while loop:")
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Print a triangle pattern
print("\nTriangle Pattern:")
for i in range(1, 8):
    print("#" * i)

# 4. Create an 8x8 grid using nested loops
print("\n8x8 Grid:")
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()  # Move to the next line after each row

# 5. Print the multiplication pattern
print("\nMultiplication Pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

