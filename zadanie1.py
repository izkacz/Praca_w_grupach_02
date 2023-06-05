lista_B = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]

def znajdz_max(lista):
    max_element = 0
    for i in lista:
        for j in i:
            k = str(j)
            if len(k) > max_element:
                max_element = len(k)
    return max_element

#max = znajdz_max(lista_B))
print(znajdz_max(lista_B))
# print(lista_B)
def do_lewej(lista):
    maxLen = znajdz_max(lista)
    for i in lista:
        for index, j in enumerate(i):
            k = str(j)
            if k < str(maxLen):
                spacebarAmount = maxLen - len(k)
                result = " "*spacebarAmount + k
                #print(result)
                i[index] = result
    return lista

print(do_lewej(lista_B))