# Import Necessary Libraries
import sys

def doSomething(rows, cols, grid_chars):
    # Parse the input
    grid = [list(grid_chars[i:i+cols]) for i in range(0, len(grid_chars), cols)]

    # Sort each row
    sorted_grid = [''.join(sorted(row)) for row in grid]

    # Check if columns are sorted
    transposed_grid = list(zip(*sorted_grid))
    if all(''.join(col) == ''.join(sorted(col)) for col in transposed_grid):
        return "YES"
    else:
        return "NO"

# Take Input
record, grid_size, *characters = input().split(",")
rows, cols = map(int, grid_size.split())

# Process Output Using Function
result = doSomething(rows, cols, ''.join(characters))

# Print Output
print(result)
