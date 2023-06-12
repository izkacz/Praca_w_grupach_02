lista_B = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]

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

        
do_lewej(lista_B)