
# Number of rows in the upper half
n = 5

# Upper half of the pattern
for i in range(n):

    # Print left-side stars
    for j in range(i + 1):
        print("*", end=" ")

    # Print middle spaces
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")

    # Print right-side stars
    for j in range(i + 1):
        print("*", end=" ")

    # Move to the next line
    print()


# Lower half of the pattern
for i in range(n - 1):

    # Print left-side stars
    for j in range(n - i - 1):
        print("*", end=" ")

    # Print middle spaces
    for j in range(2 * (i + 1)):
        print(" ", end=" ")

    # Print right-side stars
    for j in range(n - i - 1):
        print("*", end=" ")

    # Move to the next line
    print()
