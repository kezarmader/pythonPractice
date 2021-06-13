def main():
    s1 = input()
    s2 = input()

    result = isPermuted(s1, s2)

    print(result)

def isPermuted(s1:str, s2:str) -> bool:
    d = {}

    if len(s1) != len(s2):
        return False

    for c in s1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for c in s2:
        if c in d:
            d[c] -= 1
            if d[c] == 0:
                d.pop(c)
    
    if len(d) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    main()