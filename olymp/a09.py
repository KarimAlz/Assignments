# A09. Üçrəqəmli tam ədəd verilib. Bu ədədin öncə sonuncu rəqəmini (təklikləri), sonra isə ortadakı rəqəmini (onluqları) çıxışa verin.
n = str(input())
if int(n) < 100 or int(n) > 999:
    print('False')
else:
    print(n[:0:-1])