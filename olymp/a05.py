# A05. İkirəqəmli tam ədəd verilib. Bu ədədin öncə soldakı rəqəmini (onluqları), sonra isə 2 boşluq simvolundan sonra sağdakı rəqəmini (təklikləri) çıxışa verin.
n = int(input())
if abs(n) < 10 or abs(n) > 99:
    print("False")
else:
    a = n % 10
    b = n // 10
    print(str(b) + '  ' + str(a))