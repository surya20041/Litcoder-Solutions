import sys

class Solution:
    def do_something(self, num, k=None):
        if num == 0:
            return 0
        if k is None:
            # Default value for k if not provided
            k = 1

        for i in range(1, num + 1):
            t = num - k * i
            if t >= 0 and t % 10 == 0:
                return i
        return -1

def main():
    solution = Solution()
    
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = int(input())
    
    try:
        if len(sys.argv) > 2:
            k = int(sys.argv[2])
        else:
            k = int(input())
    except ValueError:
        # Handle the case where k is not a valid integer
        k = None

    result = solution.do_something(num, k)
    if result == -1:
        print("-1")
    else:
        print(result)

if __name__ == "__main__":
    main()
