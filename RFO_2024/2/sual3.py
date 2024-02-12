n, k = map(int, input().split())
s = [int(e) for e in str(input())]
count, ncount = 0, 0

def longestsequenceof0(s, count, ncount):
    nstart, nend, start, end = 0, 0, 0, 0
    j = {}
    for e in s:
        if e == 0:
            j[e] = j.get(e, 0) + 1
            ncount = j.get(e, 0)
            nend += 1
        if e == 1:
            count = ncount
            nstart += 1
            j = {}
        if int(count) < int(ncount):
            count = int(ncount)
            start, end = nstart, nend
    return map(int, [start, end])

def longestsequenceof1(s, count, ncount):
    for i in s:
        if int(i) == 1:
            ncount += 1
        if int(i) == 0:
            count = ncount
            ncount = 0
    if count < ncount:
        count = ncount
    return count

for i in range(k):
    a, b = longestsequenceof0(s, count, ncount)
    print(a, b)
    s[a], s[b] = int(1), int(1)
    print(s)
    c = longestsequenceof1(s, 0, 0)
    s = [0 if i == 1 else i for i in s]
    s[a], s[b] = 1, 1
    print(s)

print(c)