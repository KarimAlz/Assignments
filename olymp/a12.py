# A12. Üçrəqəmli tam ədəd verilib. Onun soldan birinci rəqəmini pozub ədədin sağına yazdılar. Alınan ədədi çıxışa verin.
n = int(input())
if n < 100 or n > 999:
    print('False')
else:
    m = n % 100
    n = n // 100
    print(str(m) + str(n))