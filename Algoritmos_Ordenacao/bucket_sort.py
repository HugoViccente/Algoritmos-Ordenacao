def bucket_sort(arr):
    # Vantagens:
    # - Muito eficiente para dados uniformemente distribuídos
    # Desvantagens:
    # - Exige conhecimento prévio da distribuição dos dados
    # - Usa listas auxiliares (não in-place)

    if not arr:
        return arr

    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(num * bucket_count)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


lista_teste = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Lista original:", lista_teste)
print("Lista ordenada:", bucket_sort(lista_teste.copy()))
