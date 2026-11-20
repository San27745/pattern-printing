# Outer loop controls the number of rows
for i in range(1, 6):

    # Inner loop prints numbers from 1 to i
    for j in range(1, i+1):

        # Print numbers on the same line with a space
        print(j, end=" ")

    # Move to the next line after each row
    print()