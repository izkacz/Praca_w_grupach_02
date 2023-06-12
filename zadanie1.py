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