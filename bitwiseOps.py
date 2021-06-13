CACHE = {
    0x0:0x0,
    0x1:0x8000,
    0x2:0x4000,
    0x3:0xC000,
    0x4:0x2000,
    0x5:0xA000,
    0x6:0x6000
}

def main():
    number = input()

    rev = reverse(number)
    print(rev)

 # << (3 * MASK_SIZE))
    '''
            | CACHE[(number >> MASK_SIZE) & MASK] << (2 * MASK_SIZE)
            | CACHE[(number >> (2 * MASK_SIZE)) & MASK] << MASK_SIZE
            | CACHE[(number >> (3 * MASK_SIZE)) & MASK])
            '''
def reverse(number:int):
    MASK = 0xFFFF
    MASK_SIZE = 16

    return ((number * 1) & MASK)
    


if __name__ == '__main__':
    main()