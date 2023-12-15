def doSomething(size, queries):
    array = [0] * (size + 1)

    for _ in range(queries):
        left, right, value = map(int, input().split())
        array[left] += value
        if right + 1 <= size:
            array[right + 1] -= value

    max_val = array[1]
    for i in range(2, size + 1):
        array[i] += array[i - 1]
        max_val = max(max_val, array[i])

    return max_val

def main():
    size = int(input())
    queries = int(input())
    result = doSomething(size, queries)
    print(result)

if __name__ == "__main__":
    main()
