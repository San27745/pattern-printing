# Initialize the value of n
n = 4

# Outer loop controls the number of rows
for i in range(n+1):

    # Inner loop controls the number of columns
    for j in range(n+1):

        # Print star on the same line with a space
        print("*", end=" ")

    # Move to the next line after printing each row
    print()