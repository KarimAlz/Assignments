# A13. Üçrəqəmli tam ədəd verilib. Onun sağdan birinci rəqəmini pozub ədədin soluna yazdılar. Alınan ədədi çıxışa verin.
n = int(input())
if n < 100 or n > 999:
    print('False')
else:
    m = n % 10
    n = n // 10
    if m == 0: #Bu şərt 120 yazanda 012 output verməsin deyə burdadı. Görəsən bunun daha rahat yolu var? 🤔
        m = ''
    print(str(m) + str(n))