# Initialize n
n = 6

# Outer loop controls rows in decreasing order
for i in range(n, 0, -1):

    # Print spaces before the stars
    for j in range(n-i):
        print(" ", end="")

    # Print decreasing odd numbers of stars
    for k in range(2*i - 1):
        print("*", end="")

    # Move to the next line
    print()