# N simvoldan ibarət (N < 20000) A mətni verilib.
# Mətndə sözlər bir-birindən ya boşluq, ya da vergül işarəsi ilə, cümlələr isə nöqtəilə ayrılıb. 
# M (M < 200) simvoldan ibarət olan və A mətni kimi təsvir edilmiş başqa bir B mətni də verilib.
# A mətnindən ayrı-ayrı sözləri, vergülləri, yaxud nöqtələri silməklə B mətninin
# alınıb-alınmadığını müəyyən edən proqram tərtib edin (sözlərin yerini dəyişmək olmaz).
def check(a, b):
    a_2 = [char for char in a if char.isalpha()] # Şərtdə tam başa düşmürəm orda boşluqların silinməyini istəyir yoxsa yox
#   a_2 = [char for char in a if char.isalpha() or char.isspace()] # Bu giriş boşluqları silmədən list yaradır
    return ''.join(a_2) == b

a = 'Salam, keks'
b = 'Salamkeks'
print(check(a, b))


if check(a, b):
    print('YES')
else:
    print('NO')

# Bu məsələnin şərtini tam başa düşmədiyim üçün bir az ChatGPT-dan kömək aldım, amma axır alqoritm mən fikirləşdiyim oldu. ChatGPT-dan götürdüyüm yeganə kod hissəsi "char.isalpha()"
# -dır. Bu metod sətir tipli dəyişənin seçilmiş simvolunun əlifbadan olub-olmadığını yoxlayır (yəni:
# char = "a"
# print(char.isalpha())  olarsa çıxışda "True" çıxacaq, amma,
# 
# char = "."
# print(char.isalpha())  olarsa çıxışda "False" cıxacaq