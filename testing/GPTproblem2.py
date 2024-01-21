# Girişdə 2 sözün anaqram olub-olmadığınl yoxlayır. (Araqram - 1 söz o biri sözün hərfəlindən ibarətdir)

n = str(input())
m = [str(word) for word in n.split()]

def are_anagrams(a, b):
    same_letter = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                same_letter += 1
    if same_letter == len(a) or same_letter == len(b):
        return True
    else:
        return False
print(are_anagrams(m[0], m[1]))




# Bu kodun daha effektiv və sadə həlli var

# def are_anagrams(a, b):
#     a = a.replace(' ', '').lower()
#     b = b.replace(' ', '').lower()
#     return sorted(a) == sorted(b)

# n = str(input())
# m = n.split()

# if len(m) == 2:
#     print(are_anagrams(m[0], m[1]))
# else:
#     print("2 söz daxil edin (boşluqla ayrılmaq şərti ilə)")

# Həmin şeydi sadəcə mənim kodumda dövrlər çoxdu ona görədə kodun işləmə vaxtını uzada bilər.