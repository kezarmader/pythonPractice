def main():
    x = float(input())
    y = int(input())
    z = powerOfY(x, y)

    print(z)

def powerOfY(x, y):
    result, power = 1.0, y
    if(x < 0):
        power = -power
        x = 1/x
    
    while(power):
        if (power & 1):
            result = result * x
        x = x * x
        power = power >> 1
        print(bin(power))
    
    return result

if __name__ == '__main__':
    main()