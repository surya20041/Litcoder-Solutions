import sys

def doSomething(board, word):
    def dfs(i, j, k):
        # Base case: Check if current position (i, j) is within the boundaries of the board
        # or if the current character on the board does not match the corresponding character in the word
        if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[k]:
            return False
        
        # If we have matched all characters in the word, return True
        if k == len(word) - 1:
            return True

        # Temporarily mark the current position on the board as visited
        temp, board[i][j] = board[i][j], '/'
        
        # Recursively explore all possible directions (up, down, left, right) to find the word
        res = (
            dfs(i + 1, j, k + 1) or
            dfs(i - 1, j, k + 1) or
            dfs(i, j + 1, k + 1) or
            dfs(i, j - 1, k + 1)
        )
        
        # Restore the original character on the board
        board[i][j] = temp
        return res

    # Check if the board is empty
    if not board or not board[0]:
        return "No"

    # Get the dimensions of the board
    m, n = len(board), len(board[0])

    # Iterate through each cell on the board and start the DFS search
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return "Yes"
    
    # If the word is not found in any starting position, return "No"
    return "No"

# Read input: Number of rows, number of columns, and the target word
row = int(sys.stdin.readline().strip())
col = int(sys.stdin.readline().strip())
word = sys.stdin.readline().strip()

# Initialize an empty grid
grid = []
for _ in range(row):
    row_input = sys.stdin.readline().strip().split()
    grid.append(row_input)

# Call the function with user input
result = doSomething(grid, word)

# Print the result
print(result)
