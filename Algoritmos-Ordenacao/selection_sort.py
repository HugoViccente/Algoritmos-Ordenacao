def selection_sort(arr):
    # Vantagens:
    # - Simples de entender e implementar
    # - Pouco uso de memória (in-place)
    # Desvantagens:
    # - Ineficiente para listas grandes (O(n²))

    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
