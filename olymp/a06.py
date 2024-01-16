# A06. İkirəqəmli müsbət tam ədəd verilib. Onun rəqəmlərinin cəmini və hasilini tapın.
n = str(input())
if int(n) < 10 or int(n) > 99:
    print('False')
else:
    a, b = int(n[0:1:]), int(n[1:0:-1])
    #b = int(n[1:0:-1])
    #a, b = int(a), int(b)
    print((a + b), (a * b))