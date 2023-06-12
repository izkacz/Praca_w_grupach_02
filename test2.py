
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
        for j in i:

        f l != len(list):

        else:
            k=0
            for j in i:
                k = k + 1

                if k != len(i):
                    c=str(j)+", "
                    wynik=wynik+c
                else:
                    c=str(j)+']'
                    wynik = wynik + c
                    wynik=wynik+']'
    return wynik




lista_A=[[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
print(read_list(lista_A))