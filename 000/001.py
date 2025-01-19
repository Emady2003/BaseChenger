i = 1
listo = []
list_baghi_mande_ha = []
condition = True
whilee = True
yelistebafgimande = []
yelistdige = []
#checking x 
def inputX(counter): 
    if counter == 1 :
        print("adade khod ra vared knid")
        x = input()
        x = x.upper()
        listo.append(x)
    else :
        while counter <= 0 :
            print("do you want to countinue ? ")
            YesOrNo = input("Y/n : ")
            if YesOrNo == "y" :
                counter = 1
                print("adade khod ra vared knid")
                x = input()              
            elif YesOrNo =="n":
                raise SystemExit
            else:
                counter = counter - 0.48
                if counter == -0.96 :
                    print("motasefane ...")
                    raise SystemExit
    string = x
    if string.count('.') >= 2:
        print("vorodi ra be sorate sahih vared knid !!! ")
        inputX(0)
    elif string.count('.') == 0 :
        string = string + '.0'
        listo.append(string)
        return x 
    else :
        listo.append(x)
        return x 
#checking y     
def inputY(counter):
    while counter <= 0:
        print("do you want to countinue ? ")
        YesOrNo = input("Y/n : ")
        if YesOrNo == "y" :
            counter = 1
        elif YesOrNo =="n":
            raise SystemExit
        else:
            counter = counter - 0.48
            if counter == -0.96 :
                print("motasefane ...")
                raise SystemExit
    print("az mabnaie ... ")
    y = int(input())
    if y >= 35 : 
        print(" motasefane nemitavan mabnaie balatar az mabnaie 35 ra mohasebe kard ! ")
        inputY(0)
    xALL = listo[-1]
    x_1, x_2 = xALL.split('.')
    result = list(str(x_1))
    result2 = list(str(x_2))
    result = [item.upper() if isinstance(item, str) else item for item in result]
    result2 = [item.upper() if isinstance(item, str) else item for item in result2]
    mapping = {'0':0, '1':1 , '2':2 ,'3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9 ,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G':16, 'H':17 ,'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35 }
    numeric_list = [mapping[char] for char in result]
    if any(number >= y for number in numeric_list):
        print("!!--tamamie uadade dakhele adade morede nazar mibayest kochektar az mabna bashad !--!! ")
        inputY(0)
    numeric_list2 = [mapping[char] for char in result2]
    if any(number >= y for number in numeric_list2):
        print("!!--tamamie uadade dakhele adade morede nazar mibayest kochektar az mabna bashad !--!! ")
        inputY(0)
    listo.append(y)
    listo.append(numeric_list)
    listo.append(numeric_list2)
    return y,numeric_list, numeric_list2
#checking z 
def inputZ(counter):
    while counter <= 0:
        print("do you want to countinue ? ")
        YesOrNo = input("Y/n : ")
        if YesOrNo == "y" :
            counter = 1
        elif YesOrNo =="n":
            raise SystemExit
        else:
            counter = counter - 0.48
            if counter == -0.96 :
                print("motasefane ...")
                raise SystemExit
    print("be mabnaie ... ")
    z = int(input())
    if z >= 35 : 
        print(" motasefane nemitavan mabnaie balatar az mabnaie 35 ra mohasebe kard ! ")
        inputZ(0)
    return z 

def tabdilXbe10(numeric_list,numeric_list2,y):
    i = 1
    condition = True
    decimal = 0
    ## braie ghesmate sahih
    # numeric_list liste sahih
    # numeric_list2 liste asharii 
    while condition == True :
        numeric_liste = (numeric_list[-i])*(y**(i-1))
        decimal = decimal + numeric_liste
        i = i + 1
        if i-1 == len(numeric_list) :
            condition = False
    ## baraie ghesmate ashari 
    condition = True
    i = 1
    while condition == True :
        numeric_liste2 = (numeric_list2[i-1])/(y**(i))
        decimal = decimal + numeric_liste2
        i = i + 1
        if i == (len(numeric_list2)+1) :
            condition = False
        if decimal == 0:
            print(" 0 mishavad ! ")
    print(decimal," mishe dar mabnaie 10 esh")
    listo.append(decimal)
    return decimal
    

def tabdil10beZ(decimal,z):
    adadasli = 0
    adadasli2 = 0
    deci1 = decimal//1
    deci2 = decimal - deci1
    while deci1 > z : 
        yelistebafgimande.append(deci1%z)
        deci1 = deci1 // z
        if deci1 < z :
            yelistebafgimande.append(deci1)
    i = len(yelistebafgimande)
    n = 0
    while i > 0 :
        adadasli = adadasli + (yelistebafgimande[-i]*(10**n))
        i = i - 1 
        n = n + 1
    listo.append(adadasli)

    baghideci2 = 0

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
    javabenahaie = javabenahaie + adadasli
    print("adade shoma dar  kholase ke javab mishe --- > ",javabenahaie)


# def order
def main():
    x = inputX(1)
    ymain,y1,y2 = inputY(1)
    tabdilXbe10(y1,y2,ymain)
    z = inputZ(1)
    tabdil10beZ(listo[-1],z)





main()
