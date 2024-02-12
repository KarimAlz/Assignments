a = str(input())
b = str(input())

if len(a) == len(b):
    c = ''.join([x + y for x, y in zip(a, b)])
else:
    d = a[len(a) - 1:len(a):]
    a = a[:len(a) - 1:]
    c = ''.join([x + y for x,y in zip(a, b)] + list(d))

print(c)
