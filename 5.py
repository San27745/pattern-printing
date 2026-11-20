# Outer loop controls the number of rows
for i in range(1, 6):

    # Inner loop prints the row number i times
    for j in range(1, i+1):

        # Print i on the same line with a space
        print(i, end=" ")

    # Move to the next line
    print()