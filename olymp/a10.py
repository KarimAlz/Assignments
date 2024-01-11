n = str(input())
if int(n) < 100 or int(n) > 999:
    print('False')
else:
    a, b, c = int(n[:1:]), int(n[1:2:]), int(n[2:3:])
    print((a + b + c), (a * b * c))