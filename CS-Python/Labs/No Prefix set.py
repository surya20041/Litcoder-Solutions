class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True

    def has_prefix(self, word):
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
            if node.is_end:
                return True
        return False

def doSomething(passwords):
    trie = Trie()
    for password in passwords:
        if trie.has_prefix(password):
            print("BAD PASSWORD")
            return False
        trie.insert(password)
    print("GOOD PASSWORD")
    return True

def main():
    input_str = input()
    passwords = input_str.split()

    doSomething(passwords)

if __name__ == "__main__":
    main()
