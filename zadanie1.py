lista_B = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
lista_C = [[1, 7, 909, 1024], [24, 66, 89, 100], [77, 24, 3, 208]]

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
        for j in i:
            k = str(j)
            result = k.ljust(maxLen)
            additionalList.append(result)
        print(additionalList)
        additionalList.clear()
    print('\n')

do_lewej(lista_B)
print('\n')
do_lewej(lista_C)

assert read_list([[2, 7, 209, 3],[1000, 32, 128, 6],[87, 5432, 9, 7000]])=="[[   2,    7, 209,    3],\n[1000,   32, 128,    6],\n[  87, 5432,   9, 7000]]"
assert do_lewej([[2, 7, 209, 3],[1000, 32, 128, 6],[87, 5432, 9, 7000]])=="[[2,    7,    209, 3],\n[1000, 32,   128, 6],\n[87,   5432, 9,   7000]]"
