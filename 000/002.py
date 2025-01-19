deci2 = 0.12890625
yelistdige = []
listo = []
z = 8
adadasli2 = 0

while (deci2 % 1) != 0.0 :
    deci2 = deci2 * z
    baghideci2 = deci2//1
    yelistdige.append(baghideci2)
    deci2 = deci2 - (deci2//1)
i = len(yelistdige)
n = 0
while i > 0 :
    adadasli2 = adadasli2 + (yelistdige[i-1]*(10**n))
    i = i - 1 
    n = n + 1
listo.append(adadasli2)
javabenahaie = adadasli2/(10**len(yelistdige))
print("javabe akhar = ",javabenahaie)