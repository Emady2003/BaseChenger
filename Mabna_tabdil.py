i = 1
decimal = 0
list_baghi_mande_ha = []
condition = True
whilee = True
print(" ##  rahnamaie : A=10  B=11  C=12  D=13  E=14  F=15  ... ## ")
print("adade khod ra jahate tabdil mabna vared knid (CAPITALL): ")
x = str(input())
x_1, x_2 = x.split('.')
print("in adad dar che mabnaie ast ? : ")
y = int(input())
result = list(str(x_1))
mapping = {'0':0, '1':1 , '2':2 ,'3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9 ,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G':16, 'H':17 ,'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35 }
char_list = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

for item in result:
    if item not in char_list:
        print(item,"tamami character ha baiad besorat bozorg (capitall) neveshte shavad")
        raise SystemExit

numeric_list = [mapping[char] for char in result]
print(numeric_list)
if any(number > y for number in numeric_list):
    print("!!--tamamie uadade dakhele adade morede nazar mibayest kochektar az mabna bashad !--!! ")
    raise SystemExit
print("be che mabnaie baiad bravad ? :")
z = int(input())
if z >= 35 : 
    print(" motasefane nemitavan balatar az mabnaie 35 ra mohasebe kard ! ")
    raise SystemExit
if '.' not in numeric_list:
    numeric_list.append('.')

print("numeric list : ",numeric_list)

###################################
dot_index = numeric_list.index('.')
before_dot = numeric_list[:dot_index]
after_dot = numeric_list[dot_index+1:]
while condition == True :
    before_dot_number = (before_dot[-i])*(y**(i-1))
    decimal = decimal + before_dot_number
    i +=1
    if i-1 == len(before_dot) :
        condition = False

print(decimal," mishe dar mabnaie 10 esh")
if decimal == 0:
    print(0)
else:
    while decimal > z :
        baghimande = decimal % z
        decimal = decimal // z
        list_baghi_mande_ha.append(baghimande)
        if decimal < z :
            list_baghi_mande_ha.append(decimal)

    print(list_baghi_mande_ha)
    number = int(''.join(map(str, list_baghi_mande_ha[::-1])))
    print("ghesmate sahih adad brabar ast ba  :  ",number)
    print(x,y,z)
    print(after_dot)

    decimal_number = float('0.' + ''.join(map(str, after_dot)))
    print(decimal_number)

##########################################################
print("#########################")
print(x_2)
if x_2 == '0':
    print( " do do 00 ")
    raise SystemExit
i = 1
decimal = 0
list_baghi_mande_ha = []
list_hasele_zarba = []
hasele_zarb = []
condition = True
whilee = True

result = list(str(x_2))
for item in result:
    if item not in char_list:
        print(item,"tamami character ha baiad besorat bozorg (capitall) neveshte shavad")
        raise SystemExit

numeric_list = [mapping[char] for char in result]
print(numeric_list)
if any(number > y for number in numeric_list):
    print("!!--tamamie uadade dakhele adade morede nazar mibayest kochektar az mabna bashad !--!! ")
    raise SystemExit

print("pas adde morede nazar :")
print(x,"mibashad !")
print("ke dar mabnaie  :  ",y,"  ast ")
print("va mibaiest be mabnaie  ",z," tabdil shavad")

if '.' not in numeric_list:
    numeric_list.append('.')

print(numeric_list)


dot_index = numeric_list.index('.')
before_dot = numeric_list[:dot_index]
after_dot = numeric_list[dot_index+1:]

while condition == True :
    before_dot_number = (before_dot[i-1])/(y**(i))
    decimal = decimal + before_dot_number
    i +=1
    print(decimal)
    if i == len(before_dot)+1 :
        condition = False

print(decimal," mishe dar mabnaie 10 esh")


i = 0
while decimal != 0.0:
    i += 1
    decimal = decimal * z
    k = decimal//1
    print(k,"  0.0.0  ",decimal)
    list_hasele_zarba.append(k)
    if decimal > 1:
        decimal=decimal-(k)
        print(k,"  1.1.1  ",decimal)

    if i == 11 :
        decimal = 0.0
print("decimal ;",decimal)
print(list_hasele_zarba)

result = float("".join(str(int(v)) for v in list_hasele_zarba)) / 1000
print(result)
print(number+result)
print(x)