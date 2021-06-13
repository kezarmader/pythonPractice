import collections

d = collections.defaultdict(list)

d[1] = 1

if not d.get(2):
    print('empty')