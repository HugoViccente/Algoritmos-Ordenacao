def insertion_sort(arr):
    # Vantagens:
    # - Bom para listas pequenas ou quase ordenadas
    # - Estável e in-place
    # Desvantagens:
    # - Desempenho ruim em listas grandes (O(n²))

    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr
