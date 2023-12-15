from collections import deque

def doSomething(arr, k, n):
    result = []
    dq = deque()

    for i in range(len(arr)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0] + n - 1])

    return result

def main():
    arr = list(map(int, input().split()))
    k = int(input())
    n = int(input())

    result = doSomething(arr, k, n)

    for val in result:
        print(val, end=" ")

if __name__ == "__main__":
    main()
