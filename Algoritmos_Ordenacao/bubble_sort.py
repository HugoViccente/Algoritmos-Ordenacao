def bubble_sort(arr):
    # Vantagens:
    # - Fácil de implementar
    # - Detecta se o array já está ordenado (versão otimizada)
    # Desvantagens:
    # - Muito lento em listas grandes (O(n²))

    n = len(arr)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocado = True
        if not trocado:
            break
    return arr

lista_teste = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista_teste)
print("Lista ordenada:", bubble_sort(lista_teste.copy()))
