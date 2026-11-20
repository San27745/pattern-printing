# Initialize n
n = 5

# Increasing diamond pattern
for i in range(1, n + 1):

    # Print spaces before stars
    for j in range(n-i):
        print("  ", end="")

    # Print odd numbers of stars with spaces
    for k in range(2*i - 1):
        print("*", end=" ")

    # Move to the next line
    print()

# Decreasing diamond pattern
for i in range(n-1, 0, -1):

    # Print spaces before stars
    for j in range(n-i):
        print("  ", end="")

    # Print decreasing odd numbers of stars
    for k in range(2*i - 1):
        print("*", end=" ")

    # Move to the next line
    print()