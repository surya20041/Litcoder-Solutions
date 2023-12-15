def doSomething(matrix):
    # Get the size of the matrix (assuming it's a square matrix)
    size = len(matrix)

    # Initialize variables to store the sums of the diagonals
    ltr_sum = 0  # Left-to-right diagonal sum
    rtl_sum = 0  # Right-to-left diagonal sum

    # Loop through the matrix to calculate the diagonal sums
    for i in range(size):
        ltr_sum += matrix[i][i]  # Add elements from the left-to-right diagonal
        rtl_sum += matrix[i][size - 1 - i]  # Add elements from the right-to-left diagonal

    # Calculate the absolute difference between the diagonal sums
    abs_diff = abs(ltr_sum - rtl_sum)

    return abs_diff

# Take input from the user for the matrix
size = int(input())
matrix = []

for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)

result = doSomething(matrix)
print(result)
