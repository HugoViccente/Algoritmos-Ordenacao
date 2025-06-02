def counting_sort(arr):
    # Vantagens:
    # - Muito rápido para inteiros pequenos (O(n + k))
    # - Estável
    # Desvantagens:
    # - Só funciona com números inteiros
    # - Usa memória extra proporcional ao maior valor

    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    resultado = [0] * len(arr)
    for num in reversed(arr):
        resultado[count[num] - 1] = num
        count[num] -= 1

    return resultado


lista_teste = [4, 2, 2, 8, 3, 3, 1]
print("Lista original:", lista_teste)
print("Lista ordenada:", counting_sort(lista_teste.copy()))
