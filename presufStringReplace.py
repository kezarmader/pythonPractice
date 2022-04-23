class Trie:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        trav = self.trie
        for c in word:
            if c not in trav:
                trav[c] = {}
            trav = trav[c]
        trav['#'] = {}

    def findWord(self, word):
        trav = self.trie

        for c in word:
            if c in trav:
                trav = trav[c]
            else:
                return False

        if '#' in trav:
            return True
        
        return False
    def exists(self, char):
        return char in self.trie

    
def Solution(text, findWordList):
    trie = Trie()
    consLen = 0
    for word in findWordList:
        trie.addWord(word)
        consLen = len(word)
    
    result = []
    i = 0
    while i < len(text):
        if trie.exists(text[i]):
            if trie.findWord(text[i:i + consLen]):
                result.append('$')
                result.append(text[i:i + consLen])
                result.append('@')
                i += consLen
                continue

        result.append(text[i])
        i += 1
    
    return ''.join(result)

print(Solution('abcdefg', ['bc', 'ef']))