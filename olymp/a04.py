# A04. İkirəqəmli tam ədəd verilib. Onun cüt olub-olmadığını müəyyənləşdirin.
n = int(input())
if n < 10 or n > 99:
    print("False")
else:
    if n % 2 == 0:
        print("YES")
    else:
        print("NO")