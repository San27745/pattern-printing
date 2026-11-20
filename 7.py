# Initialize n
n = 6

# Outer loop controls the number of rows
for i in range(1, n + 1):

    # Print spaces before the stars
    for j in range(n-i):
        print(" ", end="")

    # Print odd numbers of stars in each row
    for k in range(2*i - 1):
        print("*", end="")

    # Move to the next line
    print()