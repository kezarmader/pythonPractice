def main():
    rpn = input()
    print(evaluate(rpn))

operation = {
        '+': lambda second, first: first + second,
        '-': lambda second, first: first - second,
        'x': lambda second, first: first * second,
        '/': lambda second, first: first / second,
    }

def evaluate(rpn):
    tokens = rpn.split(',')
    
    if(len(tokens) == 0):
        return float('inf')

    stack = [int(tokens[0])]
    for t in tokens:
        if t in operation:
            result = operation[t](stack.pop(),stack.pop())
        else:
            result = int(t)
        stack.append(result)
    return stack[-1]


if __name__ == '__main__':
    main()