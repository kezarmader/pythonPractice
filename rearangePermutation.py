def main():
    a = [x for x in input().split(' ')]
    p = [int(x) for x in input().split(' ')]

    #r = rearrangeWithSpace(a, p)
    #print(r)
    r = rearrange(a, p)
    print(r)

def rearrange(a, p):
    for i in range(len(a)):
        next = i
        while p[next] >= 0:
            print(p)
            print(a)
            a[p[next]], a[i] = a[i], a[p[next]]
            temp = p[next]
            p[next] -= len(p)
            next = temp
    return a

def rearrangeWithSpace(a, p):
    set = {}

    for i in range(len(p)):
        if i != p[i]:
            set[i] = a[i]
            if p[i] in set:
                a[i] = set[p[i]]
            else:
                a[i] = a[p[i]]
    return a

if __name__ == '__main__':
    main()