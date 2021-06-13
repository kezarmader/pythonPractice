from typing import Collection


import collections
Rectangle = collections.namedtuple('Rectangle', 'x y width height')

def main():
    a = Rectangle(1,2,4,3)
    b = Rectangle(2,2,1,1)

    c = intersect(a, b)
    print(c)

def isIntersect(a, b):
    return (a.x <= b.x and a.x + a.width >= b.x + b.width) or (a.y <= b.y and a.y + a.height >= b.y + b.height)

def intersect(a, b):
    if not isIntersect(a,b):
        return Rectangle(0,0,-1,-1)
    else:
        return Rectangle(
            max(a.x, b.x),
            max(a.y, b.y),
            min(a.x + a.width, b.x + b.width) - max(a.x, b.x),
            min(a.y + a.height, b.y + b.height) - max(a.y, b.y)
        )

if __name__ == '__main__':
    main()