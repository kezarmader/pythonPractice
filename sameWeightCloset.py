def main():
    x = int(input())

    if x & 1 == 1: 
        x = (x - 1)|(x + 1)
    else:
        x = (x - 1)^(x + 1)
    print(bin(x))


if __name__ == '__main__':
    main()