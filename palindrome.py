def main():
    n = int(input())
    if (n < 0):
        print(False)
        return

    r = reverse(n)
    print(r == n)

def reverse(n):
    result = 0
    while(n):
        d = n % 10
        result = result * 10 + d
        n = n // 10
    return result

if __name__ == '__main__':
    main()