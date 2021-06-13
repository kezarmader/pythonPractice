
def main():
    plainUrl = list(input())
    charCount = int(input())
    encodeUrl = [None] * len(plainUrl)
    counter = 0
    encodeMap = {
        ' ': ['%','2','0'],
        '/': ['%', '3', '0', '1']
    }
    for i in range(charCount+1):
        if plainUrl[i] in encodeMap:
            replace = encodeMap[plainUrl[i]]
            replaceLen = len(replace)
            encodeUrl[counter:counter+replaceLen] = replace
            counter += replaceLen
        else:
            encodeUrl[counter] = plainUrl[i]
            counter += 1
    print(''.join(encodeUrl))


if __name__ == '__main__':
    main()