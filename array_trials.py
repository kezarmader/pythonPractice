from bisect import bisect, bisect_left, bisect_right

a = [1, 2, 3, 4, 5, 6, 7]
a2 = [[1,2,3], [4,5]]

r = [x for row in a2 for x in row]

r2 = [[x**2 for x in row] for row in a2]

print(r2)

print(a[:1])