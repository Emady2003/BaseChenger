counter = -1
i = 1
list_baghi_mande_ha = []
whilee = True
x=y=z=0
# functions
def CheckXorY(x,y):
#    x_1, x_2 = x.split('.')
    result = list(str(x))
    result = [item.upper() if isinstance(item, str) else item for item in result]
    mapping = {'0':0, '1':1 , '2':2 ,'3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9 ,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G':16, 'H':17 ,'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35 ,'.':0}
    numeric_list = [mapping[char] for char in result]
    if any(number > y for number in numeric_list):
        print("!!--tamamie uadade dakhele adade morede nazar mibayest kochektar az mabna bashad !--!! ")
#        InputAgain(x,y,z,counter)
    else :
        AshariYaSahih(numeric_list)
    
def CheckZ(z):
    if z >= 35 : 
        print(" motasefane nemitavan mabnaie balatar az mabnaie 35 ra mohasebe kard ! ")
#        InputAgain(x,y,z,counter)

def AshariYaSahih(numeric_list):
        dot_index = numeric_list.index('.')
        before_dot = numeric_list[:dot_index]
        after_dot = numeric_list[dot_index+1:]
        TabdelBeDecimal(before_dot)

def TabdelBeDecimal(before_dot):
    decimal = 0
    condition = True
    while condition == True :
        before_dot_number = (before_dot[-i])*(y**(i-1))
        decimal = decimal + before_dot_number
        i +=1
        if i-1 == len(before_dot) :
            print("decimal is",decimal)
            condition = False
            if decimal == 0:
                print(0)
            else :
                print(decimal," mishe dar mabnaie 10 esh")
            return decimal


    
# functions
counter = -1
def InputAgain(x,y,z,counter):
    counter = counter +1
    if counter == 0 :
        

        print(" $$$ let's begin $$$ ")
    else :
        continuee=input("do you want to countinue y/n")

        if continuee =="n":
            raise SystemExit
        
    print(" ##  rahnamaie : A=10  B=11  C=12  D=13  E=14  F=15  ... ## ")
    print("adade khod ra jahate tabdil mabna vared knid (CAPITALL): ")
    #x = str(input("-----> : "))
    x = ("123EA")    

    print("in adad dar che mabnaie ast ? : ")
    #y = int(input("-----> : "))
    y = 10
    CheckXorY(x,y)

    print("be che mabnaie baiad bravad ? : ")
    #z = int(input("-----> : "))
    z = 2
    CheckZ(z)




InputAgain(x,y,z,counter)
print(decimal)
#x_1, x_2 = x.split('.')