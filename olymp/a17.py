# A17. 999-dan böyük tam ədəd verilib. Bir qalıqsız bölmə (div) və bir bölmənin qalığını alma (mod) əməlindən 
# istifadə etməklə həmin ədədin yazılışındakı minlik mərtəbənin rəqəmini tapın.
n = str(input())
print(n[len(n) - 4:len(n) - 3:])



#m = (n // 1000) % 10
#print(m)                 Bu üsul üçün əvvəldəki str - nı int ilə əvəz eləmək lazımdı (mən belə uşaq - uşaq kodlar yazmıram)