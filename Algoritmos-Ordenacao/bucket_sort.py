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
