# 🧠 Algoritmos de Ordenação em Python

Este repositório contém implementações em Python de diversos algoritmos clássicos de ordenação. Cada algoritmo está acompanhado de comentários explicativos e exemplos simples para facilitar o aprendizado.

## 📚 Algoritmos Implementados

### 🔢 Algoritmos Simples
- **Selection Sort**  
  Ordena selecionando repetidamente o menor elemento e movendo para o início.

- **Bubble Sort**  
  Compara elementos adjacentes e os troca até que a lista esteja ordenada.

- **Insertion Sort**  
  Insere cada elemento na posição correta em relação aos anteriores.

### ⚙️ Algoritmos Eficientes (Dividir e Conquistar)
- **Merge Sort**  
  Divide a lista em sublistas menores, ordena e mescla de forma eficiente.

- **Quick Sort**  
  Escolhe um "pivô" e ordena os elementos menores e maiores em torno dele.

### 🏗️ Algoritmos Baseados em Estruturas
- **Heap Sort**  
  Constrói uma heap e extrai o maior (ou menor) elemento repetidamente.

### 📊 Algoritmos Não-Comparativos
- **Counting Sort**  
  Conta a frequência dos elementos e reconstrói a lista ordenada. Ideal para inteiros em um intervalo pequeno.

- **Radix Sort**  
  Ordena dígito a dígito (ou caractere a caractere), a partir da menor unidade. Utiliza Counting Sort como sub-rotina.

- **Bucket Sort**  
  Distribui os elementos em "baldes", ordena individualmente e concatena.

---

## 💡 Como Usar

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/algoritmos-ordenacao.git
cd algoritmos-ordenacao
```

Execute qualquer algoritmo com Python:

```bash
python selection_sort.py
```

Ou importe como módulo em outro projeto:

```python
from sorting_algorithms import selection_sort
```

---

## 📁 Estrutura do Projeto

```
algoritmos-ordenacao/
│
├── selection_sort.py
├── bubble_sort.py
├── insertion_sort.py
├── merge_sort.py
├── quick_sort.py
├── heap_sort.py
├── counting_sort.py
├── radix_sort.py
├── bucket_sort.py
└── README.md
```

---

## 🎯 Objetivo

Este repositório tem fins educacionais e serve como base para estudos sobre algoritmos de ordenação, suas complexidades e aplicações práticas.

---

## ✅ Contribuições

Sinta-se à vontade para abrir *issues*, enviar *pull requests* ou sugerir melhorias!

---

## 🧠 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).