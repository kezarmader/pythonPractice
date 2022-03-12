'''
Given an array of points(x,y) and integer m, return m points closest to origin

Input: points = [[3,3],[5,-1],[-2,4]], m = 2
Output: [ [3,3],[-2,4]]

'''
import heapq

def main():
    h = []
    
    k = int(input())
    n = int(input())
    
    points = []
    for _ in range(n):
        token = input().split(' ')
        point = [] * 2
        point.append(int(token[0]))
        point.append(int(token[1]))
        points.append(point)

    for point in points: #[[3,3],[5,-1],[-2,4]]
        distance = calcDist(point) #18, 26
        heapq.heappush(h, (-distance, point)) #3 elemens (18, 3, 3)
        
        if len(h) > k: #[20, 18]
            heapq.heappop(h)
    
    print([point for (_, point) in h])

def calcDist(point):
    return point[0]**2 + point[1]**2
    
    
if __name__ == '__main__':
    main()