# A01. Üçrəqəmli ədəd verilib. Bu ədədin rəqəmləri arasına boşluq simvolu qoymaqla çıxışa verin.
n = int(input())
l = []
if n < 100 or n > 999:
    print("False")
else:
    for i in range(3):
        l.append(n % 10)
        n //= 10
a, b, c = l
print(c, b, a)