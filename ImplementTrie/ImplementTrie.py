class Trie:

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.child = { char : None for char in self.alphabet }
        self.wordEnd = False

    def insert(self, word: str) -> None:
        """
        To insert, we break it up into characters. The idea is that, we start from the self.child.

        if self.child[currentCharacter] is None:
            Create new Trie node at self.child[currentCharacter]
        
        if currentCharacter is final:
            Mark that Trie node as wordEnd
        else:
            recursively call childTrie.insert(word[:everything after this character])
        """
        currentCharacter = word[0]
        
        if self.child[currentCharacter] is None:
            self.child[currentCharacter] = Trie()
        
        if len(word) == 1:
            self.child[currentCharacter].wordEnd = True
        else:
            self.child[currentCharacter].insert(word[1:])

    def search(self, word: str) -> bool:
        currentCharacter = word[0]

        if self.child[currentCharacter] is None:
            return False
        else:
            if len(word) == 1:
                return self.child[currentCharacter].wordEnd
            return self.child[currentCharacter].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        """
        
        """
        currentCharacter = prefix[0]

        # if the self.child[currentCharacter] == None: we return False
        if self.child[currentCharacter] is None:
            return False
        else:
            if len(prefix) == 1:
                return True
            return True and self.child[currentCharacter].startsWith(prefix[1:])



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
