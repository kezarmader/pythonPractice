import collections

class Queue:
    def __init__(self) -> None:
        self._data = collections.deque()
    def enque(self, value) -> None:
        self._data.append(value)
    def deque(self) -> int:
        return self._data.popleft()
    def max(self) -> int:
        return max(self._data)
    def __str__(self) -> str:
        result = ''
        for d in self._data:
            result += ' = ' + str(d)
        return result
        

def main():
    q = Queue()
    q.enque(10)
    q.enque(20)
    q.enque(30)
    q.deque()
    print(q)

if __name__ == '__main__':
    main()