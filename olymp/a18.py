# A18. Dördrəqəmli tam ədəd verilib. Bu ədədin palindrom olub-olmadığını müəyyən edin.
n = str(input())
def polyndrom():
    global n
    for i in range(len(n) // 2):
        if n[i] != n[:len(n) - 2:-1]:
            return 'NO'
        else:
            return 'YES'
print(polyndrom())

# Şərtdə dördrəqəmli deyilsə də istənilən rəqəmli ədədlə işləyir:)