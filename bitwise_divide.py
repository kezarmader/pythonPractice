def main():
    a = int(input())
    b = int(input())

    c = divide(a, b)
    print (c)

def divide(a, b):
    result = 0
    temp = 0

    for i in range(31, -1, -1):
        if (temp + (b << i) <= a):
            print(bin(b << i), b << i)
            temp += (b << i)
            print('temp', bin(temp), temp)
            result |= 1 << i
            print('result', bin(result), result)

    return result

if __name__ == '__main__':
    main()