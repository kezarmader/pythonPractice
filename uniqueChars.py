import sys

def main():
    s = input()

    result = haveDuplicates(s)
    print(result)

def haveDuplicates(s:str):
    checker = 0

    if len(str) > 26:
        return False

    for c in s:
        if(checker & (1 << (c - 'a'))):
            return False
        checker |= (1 << (c - 'a'))
    return True

if __name__ == "__main__":
    main()