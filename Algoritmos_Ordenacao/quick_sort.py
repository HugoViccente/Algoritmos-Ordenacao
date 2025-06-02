def quick_sort(arr):
    # Vantagens:
    # - Muito rápido em média (O(n log n))
    # - In-place (versões otimizadas)
    # Desvantagens:
    # - Desempenho ruim no pior caso (O(n²))
    # - Não é estável

    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]
        menores = [x for x in arr[1:] if x <= pivo]
        maiores = [x for x in arr[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)


lista_teste = [10, 7, 8, 9, 1, 5]
print("Lista original:", lista_teste)
print("Lista ordenada:", quick_sort(lista_teste.copy()))
