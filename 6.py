# Initialize n
n = 5

# Outer loop controls the number of rows
for i in range(n+1):

    # Print spaces first, then print stars
    print(" " * (n-i) + "*" * i)