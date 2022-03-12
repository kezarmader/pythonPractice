def main():
    text = 'CXSAQWERT'
    words = {'CAT', 'CAR', 'CART', 'ART', 'CAAAT'}

    searchWordTable = buildIndexTable(text) #O(N)
    wordDic = buildWordDic(words) #O(N)

    result = []
    for i in range(len(text)): #O(N^2)
        if text[i] in wordDic:
            slate = [text[i]]
            dfs(text[i], wordDic, slate, i, searchWordTable, result)

    print(result)

def dfs(node, wordDic, slate, i, searchWordTable, result):
    if not wordDic or node not in wordDic:
        return

    if node == 'end':
        result.append(''.join(slate))
        return
        
    for child in wordDic[node]:
        if child in searchWordTable and searchWordTable[child] > i:
            slate.append(child)
            dfs(child, wordDic[node], slate, i + 1, searchWordTable, result)
            slate.pop()
        elif child == 'end':
            dfs(child, wordDic[node], slate, i + 1, searchWordTable, result)

def buildWordDic(words):
    trie = {}
    for word in words:
        temp = trie
        for c in word:
            if not c in temp:
                temp[c] = {}
            temp = temp[c]
        temp['end'] = {}
    
    return trie

def buildIndexTable(text):
    table = {}
    for i in range(len(text)):
        table[text[i]] = i
    
    return table

if __name__ == '__main__':
    main()