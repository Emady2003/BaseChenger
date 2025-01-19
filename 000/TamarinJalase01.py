#001
day = int(input("tedade roz ra vared knid (jahate tabdil be salo maho hafte va roz): "))
year = (day//365)
day = day - (year*(365))
month = (day//30)
day = day - (month*(30))
week = (day//7)
day = day - (week*(7))
print(" = ",year," sal va ",month,"mah va ",week," hafte va ",day," roz")
print("-------------------------------------------------")
#002
dama = float(input("dama ra vared knid (be farenhaight)(jahate tabdile an be selsius)"))
dama = (dama-32)/1.8
print(dama)
print("-------------------------------------------------")
#003
counter = 0
AdadeSeRaghami = int(input("yek adade se raghami vared knid (jahate mohasebeie gamee arghame an ba ham)"))
sadgan = AdadeSeRaghami//100
print(sadgan)
dahgan = ((AdadeSeRaghami-(100*sadgan)))//10
print(dahgan)
yekan = (((AdadeSeRaghami-(100*sadgan)-(10*dahgan))))//1
print(yekan)
GameeArgham = sadgan + dahgan + yekan
print(GameeArgham)
print("-------------------------------------------------")
#004
print("3 adad vared knid (jahate miangin gereftan): ")
x = int(input())
y = int(input())
z = int(input())
miangin = ((x+y+z)/3)
print(miangin)
print("-------------------------------------------------")
#005
print("2 adad vared knid (jahate mohasebeie baghimande va khareje ghesmate taghsim in do bar ham)")
AdadeAval = float(input())
AdadeDovom =float(input())
print("baghi mande taghsim --> ",(AdadeAval%AdadeDovom))
print("khareje ghesmat -->",(AdadeAval//AdadeDovom))
print("-------------------------------------------------")
#006
s = int(input("zaman ra be sanie vared knid (jahate tabdil be sauat va daghighe va sanie): "))
m = s//60
h = m//60
m = m%60
s = s%60
print(h,"suat o ",m,"daghighe o ",s,"sanie")
print("-------------------------------------------------")
#007
print(" 2 adad vared knid(jahate ba tavan resandan be ham)")
a = int(input())
b = int(input())
haseleTavan = a**b
print(haseleTavan)
print("-------------------------------------------------")