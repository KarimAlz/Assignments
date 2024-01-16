# A08. Verilmiş natural ədədin sağdan üçüncü rəqəmini çıxışa verin.
n = input()
if int(n) < 100:
    print(0)
else:
#    n = int(n) // 100
#    l = n % 10
#    print(l)
    print(n[len(n) - 3:len(n) - 2:]) # bunu tapana qədər ürəyim çürüdü