'''
After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters. The word may
start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches,
return any one.

grid1 = [
	['c', 'c', 'x', 't', 'i', 'b'],
	['c', 'c', 'a', 't', 'n', 'i'],
	['a', 'c', 'n', 'n', 't', 't'],
	['t', 'c', 's', 'i', 'p', 't'],
	['a', 'o', 'o', 'o', 'a', 'a'],
	['o', 'a', 'a', 'a', 'o', 'o'],
	['k', 'a', 'i', 'c', 'k', 'i'],
]
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
find_word_location(grid1, word2) =>
       [(0, 1), (1, 1), (2, 1), (3, 1)]
    OR [(0, 0), (1, 0), (1, 1), (2, 1)]
    OR [(0, 0), (0, 1), (1, 1), (2, 1)]
    OR [(1, 0), (1, 1), (2, 1), (3, 1)]
find_word_location(grid1, word3) => [(3, 2)]
find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
find_word_location(grid1, word6) => [(6, 4), (6, 5)]
find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
find_word_location(grid2, word9) => [(0, 0)]

Complexity analysis variables:

r = number of rows
c = number of columns
w = length of the word
'''

grid1 = [
	['c', 'c', 'x', 't', 'i', 'b'],
	['c', 'c', 'a', 't', 'n', 'i'],
	['a', 'c', 'n', 'n', 't', 't'],
	['t', 'c', 's', 'i', 'p', 't'],
	['a', 'o', 'o', 'o', 'a', 'a'],
	['o', 'a', 'a', 'a', 'o', 'o'],
	['k', 'a', 'i', 'c', 'k', 'i']
]

word1 = "catnip"
word2 = "cccc"
word3 = "s" 
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

def dfs(grid, word, i, x, y, visited, path):
    if visited[x][y] == -1:
        visited[x][y] = 1

        if i == len(word) - 1:
            return word[i] == grid[x][y]

        if word[i] != grid[x][y]:
            return False
        
        for nx,ny in getNeighbours(x,y,grid):
            if visited[nx][ny] == -1:
                path.append((nx,ny))
                if dfs(grid, word, i+1, nx, ny, visited, path) == True:
                    return True
                path.pop()
        
def getNeighbours(x,y,grid):
    dirr = [(1,0),(0,1)]
    result = []

    for dx, dy in dirr:
        if dx+x < len(grid) and dy+y < len(grid[0]):
            result.append((dx+x, dy+y))

    return result

def findWord(grid, word):
    r = len(grid)
    c = len(grid[0])
    
    for x in range(r):
        for y in range(c):
            visited = [[-1 for _ in range(c)] for _ in range(r)]
            path = [(x,y)]
            if dfs(grid, word, 0, x, y, visited, path) == True:
                return path
            
    return []

print(findWord(grid1, word1))
print(findWord(grid1, word1) == [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ])
print(findWord(grid1, word2))
print(findWord(grid1, word2) == ([(0, 0), (1, 0), (1, 1), (2, 1)]))
print(findWord(grid1, word3))
print(findWord(grid1, word3) == [(3, 2)])
print(findWord(grid1, word4))
print(findWord(grid1, word4) == [(0, 5), (1, 5), (2, 5)])
print(findWord(grid1, word5))
print(findWord(grid1, word5) == [(4, 5), (5, 5), (6, 5)])
print(findWord(grid1, word6))
print(findWord(grid1, word6) == [(6, 4), (6, 5)])
print(findWord(grid1, word7))
print(findWord(grid1, word7) == [(5, 1), (5, 2), (5, 3)])
print(findWord(grid1, word8))
print(findWord(grid1, word8) == [(4, 1), (4, 2), (4, 3)])
print(findWord(grid1, word9))
print(findWord(grid2, word9) == [(0, 0)])