str = '1+1 - 1'

token = '';
tokens = []
for c in str:
    if c == '+':
        tokens.append(int(token))
        tokens.append('+')