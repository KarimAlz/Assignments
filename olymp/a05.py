n = int(input())
if abs(n) < 10 or abs(n) > 99:
    print("False")
else:
    a = n % 10
    b = n // 10
    print(str(b) + '  ' + str(a))