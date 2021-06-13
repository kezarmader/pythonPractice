def main():
    n = int(input())
    sign = 1
    result = 0
    position = 1

    if (n < 0):
        n = -n
        sign = -1
    
    while(n > 0):
        d = n % 10
        result = 10 * result + d
        n = n // 10
    
    print(sign * result)

if __name__ == '__main__':
    main()