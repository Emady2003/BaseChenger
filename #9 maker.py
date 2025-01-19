#nine__maker
#and_0_maker
def tavan(a,b):
    if b==0 :
        return(1)
    else :
        b = b - 1
        return(a*(tavan(a,b)))
z = 10
y = 0
print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
x = int ( input (" !%%#^&@*&@!$+ : "))
x_first = x
if x == 0 :
    print("you cant use 0")
    exit()
else :
    x = x - 1
    while x>=0:
        y = y + (tavan(z,x))
        x = x - 1
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    print("bozorgtarin adade ",x_first," raghami brabar ast ba : ",(9*y))
k = (9*y)+1
print("va kochektarin adade",x_first," raghami brabar ast ba : ",(k/10))
