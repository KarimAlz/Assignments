# İstənilən natural ədəd götürüb rəqəmlərinin kvadratlarını cəmləyək. Alınan yeni
# natural ədəd üzərində də həmin əməliyyatı aparaq. Bu prosesin sonlu sayda
# təkrarlanmasından sonra nəticədə birrəqəmli ədəd alarıq. Məsələn, 324 ədədi
# üçün proses belə olacaq:
#       а1 = 324
#       а2 = 3.3 + 2.2 + 4.4 = 29
#       а3 = 2.2 + 9.9 = 85
#       а4 = 8.8 + 5.5 = 89
#       а5 = 8.8 + 9.9 = 145
#       а6 = 1.1 + 4.4 + 5.5 = 42
#       а7 = 4.4 + 2.2 = 20
#       а8 = 2.2 + 0.0 = 4 … (prosesin sonu)
# [1, 1000] intervalında yerləşən natural ədədlər içərisindən yuxarıda göstərilən
# prosesin 1-lə nəticələndiyi bütün ədədləri aşkarlayan proqram tərtib edin.

def keks(a):
    m = [int(k) for k in str(a)]
    s = 0
    while len(m) > 1:
        s = 0
        for i in m:
            s += i * i
        if s == 0:
            break
        m = [int(k) for k in str(s)]
    return s

num = []
for i in range(1,1000):
    if keks(i) == 1:
        num.append(i)
print(num)