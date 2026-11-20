# Initialize the value of n
n = 5

# Outer loop controls the number of rows
for i in range(n):

    # Inner loop controls the number of columns
    for j in range(n):

        # Check whether the position is on the border
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:

            # Print star on the border
            print("*", end=" ")

        else:
            # Print blank space inside the square
            print(" ", end=" ")

    # Move to the next line after each row
    print()