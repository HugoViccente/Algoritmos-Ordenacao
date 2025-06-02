def merge_sort(arr):
    # Vantagens:
    # - Muito eficiente (O(n log n))
    # - Estável
    # Desvantagens:
    # - Usa memória extra (não é in-place)

    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = merge_sort(arr[:meio])
        direita = merge_sort(arr[meio:])

        resultado = []
        i = j = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1

        resultado += esquerda[i:]
        resultado += direita[j:]
        return resultado
    else:
        return arr


lista_teste = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista_teste)
print("Lista ordenada:", merge_sort(lista_teste.copy()))
