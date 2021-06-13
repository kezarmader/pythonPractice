def main():
    num1 = int(input())
    num2 = int(input())
    
    result = multiply(num1, num2)
    print(result)

def multiply(num1, num2):
    result = 0
    current = num2
    
    while(current != 0):
        lsb = current & 1
        
        if (lsb == 1):
            result = add(num1, result)
            
        current = current >> 1
        num1 = num1 << 1
    return result

def add(num1, num2):
    while(num2 != 0):
        print(bin(num1), bin(num2))
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
        
    print(bin(num1), bin(num2))
    return num1

if __name__ == '__main__':
    main()