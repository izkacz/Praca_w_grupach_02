lista_B = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]

def znajdz_max(lista):
    max_element = 0
    for i in lista:
        for j in i:
            k = str(j)
            if len(k) > max_element:
                max_element = len(k)
    return max_element

def read_list(list):
    lista_wynik=[]
    max_v=len(str((max([sublist[-1] for sublist in lista_A]))))


    # Using for loop
    a="["
    l=0
    wynik=a
    for i in list:
        k = 0
        l=l+1
        b='['

        wynik=wynik+b


        if l != len(list):
            for j in i:
                k=k+1
                if k != len(i):
                    d=''
                    for f in range(0,max_v-len(str(j))):
                        d=d+" "


                    c=d+str(j)+', '
                    wynik = wynik + c



                else:
                    d = ''
                    for f in range(0, max_v - len(str(j))):
                        d = d + " "
                    c=d+str(j) +']'+',\n '
                    wynik = wynik + c




        else:
            k=0
            for j in i:
                k = k + 1

                if k != len(i):
                    d=""
                    for f in range(0,max_v-len(str(j))):
                        d=d+" "
                    c=d+str(j)+", "
                    wynik=wynik+c
                else:
                    d=""
                    for f in range(0,max_v-len(str(j))):
                        d=d+" "
                    c=d+str(j)+']'
                    wynik = wynik + c
                    wynik=wynik+']'
    return wynik




lista_A=[[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
print(read_list(lista_A))



def do_lewej(lista):
    maxLen = znajdz_max(lista)
    for i in lista:
        additionalList = []
        for index, j in enumerate(i):
            k = str(j)
            if k < str(maxLen):
                spacebarAmount = maxLen - len(k)
                result = k+ " "*spacebarAmount
                additionalList.append(result)
                if j == i:
                    print('\n')
        print(additionalList)
        additionalList.clear()


do_lewej(lista_B)