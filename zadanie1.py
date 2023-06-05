
def read_list(list):


    # Using for loop
    print("[")
    for i in list:
        print('[',  end =" ")
        for j in i:

            print(j, end =" ")

        print(']')
    print(']')
lista_A=[[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
print(read_list(lista_A))