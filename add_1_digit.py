def main():
    a = [int(x) for x in input().split(' ')]

    carry = 0
    result = a[-1] + 1
    carry = (result // 10) % 10
    for i in range(len(a) - 1, -1, -1):
        result = a[i] + carry
        a[i] = result % 10
        carry = (result // 10) % 10
    
    if(carry > 0):
        a.insert(0, carry)
    print(a)

if __name__ == '__main__':
    main()