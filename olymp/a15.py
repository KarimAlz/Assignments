# A15. Üçrəqəmli tam ədəd verilib. Bu ədədin onluqlarının və təkliklərinin yerini dəyişməklə alınan ədədi çıxışa verin.
n = int(input())
k, l = (n // 10) % 10, n % 10
n = n // 100
print(str(n) + str(l) + str(k))