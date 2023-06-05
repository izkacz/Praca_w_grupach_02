

def read_list(list):
    list_string = []



    # Using for loop

    for i in list:

        for j in i:
            k= str(j)
            list_string.append(k)

    dlugosc = len(max(list_string, key=len))

    print(list_string)
    print(list)

    print("[")
    for i in list:
        print('[', end=" ")
        for j in i:

            if(i.index(j)< len(i)-1):
                print(str(j), end=",")
            else:
                print(str(j), end="")


            if(len(str(j)) != dlugosc):
                for l in range(len(str(j)), dlugosc):
                    print("*", end="")
            else:
                print("", end="")


        print(']')
    print(']')






lista_A=[[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
print(read_list(lista_A))

