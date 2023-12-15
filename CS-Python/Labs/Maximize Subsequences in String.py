def do_something(text, pattern):
    res = 0
    cnt1 = 0
    cnt2 = 0
    for c in text:
        if c == pattern[1]:
            res += cnt1
            cnt2 += 1
        if c == pattern[0]:
            cnt1 += 1
    return res + max(cnt1, cnt2)

def main():
    text = input()
    pattern = input()

    result = do_something(text, pattern)
    print(result)

if __name__ == "__main__":
    main()
