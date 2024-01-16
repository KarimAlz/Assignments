# A11. Üçrəqəmli tam ədəd verilib. Bu ədədin rəqəmlərini sağdan sola oxuduqda alınan ədədi çıxışa verin.
n = str(input())
s = []
def req(m):
    global n             # global həqiqətən möhtəşəm əmrdi
    m = int(n) % 10
    n = int(n) // 10
    return m
for i in range(len(n)):
    s.append(req(n))
s = ''.join(map(str, s)) # s siyahısını yeganə string formatına keçirən əmr (araşdırıb öyrəndim 100% google də axtarıb ilk gördüyüm şəkildən əkməmişəm :D)
print(s)

# Kitabda verilən tapşırıq yanlız və yalnız 3 rəqəmli input tələb eləyib 3 rəqəmli output verir. Mənim yazdığım kod isə canavardı, istənilən rəqəmli ədədi tərsinə yazır (ʘ ͜ʖ ʘ)