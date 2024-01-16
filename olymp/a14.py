# A14. Üçrəqəmli tam ədəd verilib. Bu ədədin yüzlüklərinin və onluqlarının yerini dəyişməklə alınan ədədi çıxışa verin.
n = int(input())
if n < 100 or n > 999:
    # Bu şərti yazmağdan barmaqlarım çürüdü, ona görə də bundan sonrakı kodlarda yazmayacam, inputa lazımlı ədədi şərtdə verəcək (bunu oxuyan kordusa şərt 1ci sətrdədi)
    print('False')
else:
    k, l = (n // 10) // 10, (n // 10) % 10
    n = n % 10
    print(str(l) + str(k) + str(n))