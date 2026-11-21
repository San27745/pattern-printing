
# Number of rows
n = 5

# Outer loop controls rows
for i in range(n):

    # Inner loop controls columns
    for j in range(n):

        # First column and last row print stars
        if j == 0 or i == n - 1:
            print("*", end=" ")

        # Print diagonal star
        elif i == j:
            print("*", end=" ")

        # Print spaces between stars
        else:
            print(" ", end=" ")

    # Move to the next line
    print()
