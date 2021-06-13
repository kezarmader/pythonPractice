def binSearch(a, e):
    L, H = 0, len(a) - 1
    while (L < H):
        M = L + (H - L) // 2
        if a[M] < e:
            L = M + 1
        elif a[M] == e:
            return M
        else:
            H = M - 1
    return -1

print(binSearch([10,20,30,40,50,60], 50))
print(binSearch([10,20,30,40,50,60], 51))