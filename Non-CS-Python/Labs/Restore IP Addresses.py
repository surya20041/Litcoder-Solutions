def restore_ip_addresses(s):
    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            result.append('.'.join(path))
            return
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if 0 <= int(segment) <= 255 and (segment == '0' or not segment.startswith('0')):
                backtrack(end, path + [segment])

    result = []
    backtrack(0, [])
    return result

# Take input from the user
user_input = input()
ip_addresses = restore_ip_addresses(user_input)

# Print the valid IP addresses

for ip in ip_addresses:
    print(ip)
