# A19. Beşrəqəmli ədəd verilib. Bu ədədin ilk iki rəqəminin cəmi ilə son iki rəqəminin cəminin fərqini hesablayın.
n = str(input())
a, b, c, d = int(n[:1:]), int(n[1:2:]), int(n[len(n) - 2:len(n) - 1:]), int(n[len(n) - 1:len(n):]) # Yenədə şərtdə beş rəqəmli deməyinə baxmayaraq istənilən rəqəmli ədədlə işləyir
print((a + b) - (c + d))