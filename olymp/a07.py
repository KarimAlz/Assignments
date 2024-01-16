# A07. İkirəqəmli tam ədəd verilib. Bu ədədin rəqəmlərinin yerini dəyişməklə çıxışa verin.
n = str(input())
if abs(int(n)) < 10 or abs(int(n)) > 99:
    print('False')
else:
    a, b = int(n) % 10, int(n) // 10
    if a == 0:
        print(b)
    elif b == 0:
        print(a)
    else:
        print(str(a) + str(b))