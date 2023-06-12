def znajdz_max(lista):
    max_element = 0
    for i in lista:
        for j in i:
            k = str(j)
            if len(k) > max_element:
                max_element = len(k)
    return max_element

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



lista_B = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
do_lewej(lista_B)
#assert read_list([[2, 7, 209, 3],[1000, 32, 128, 6],[87, 5432, 9, 7000]])=="[[   2,    7, 209,    3],\n[1000,   32, 128,    6],\n[  87, 5432,   9, 7000]]"
assert do_lewej([[2, 7, 209, 3],[1000, 32, 128, 6],[87, 5432, 9, 7000]])=="[[2,    7,    209, 3],\n[1000, 32,   128, 6],\n[87,   5432, 9,   7000]]"
