import random
import time
import matplotlib.pyplot as plt

from ordenacao import *
from busca_binaria import *
from busca_sequencial import *
from busca_sequencial_otimizada import *
from imprime import *

def create_list(size_list):
    lista = list(range(1, size_list + 1))
    random.shuffle(lista)
    return lista

def tempo(algoritmo, lista, numero_buscas):
    tempos_busca = []
    for _ in range(numero_buscas):
        item = random.choice(lista)
        inicio = time.time()
        algoritmo(lista, item)
        fim = time.time()
        tempo_busca = fim - inicio
        tempos_busca.append(tempo_busca)
    tempo_medio = sum(tempos_busca) / len(tempos_busca)
    return tempo_medio

def plotar_grafico(tempo_busca_binaria, tempo_busca_sequencial, tempo_busca_sequencial_otimizada, size_list, numero_buscas):
    algoritmos = ['Busca Binária', 'Busca Sequencial', 'Busca Sequencial Otimizada']
    tempos = [tempo_busca_binaria, tempo_busca_sequencial, tempo_busca_sequencial_otimizada]

    plt.figure(figsize=(10, 6))
    plt.plot(algoritmos, tempos, marker='o')
    plt.xlabel('Algoritmo')
    plt.ylabel('Tempo de Busca')
    plt.title(f'Desempenho dos Algoritmos de Busca\nTamanho da Lista: {size_list} - Total de buscas: {numero_buscas}')
    plt.grid(True)
    plt.savefig('grafico.png')
    plt.show()

if __name__ == "__main__":
    size_list = 10**6 #de 10**4 a 10**7
    numero_buscas = 10**5 #de 10**2 a 10**5
    minha_lista = create_list(size_list) #cria lista com o tamanho passado
    
    imprime_lista(minha_lista)

    inicio_quicksort = time.time()
    quicksort(minha_lista)
    fim_quicksort = time.time()

    quicksort_time = fim_quicksort - inicio_quicksort
    
    imprime_lista_ordenada(minha_lista)

    print(f"Tempo para o Quicksort: {quicksort_time:.6f}")

    tempo_busca_binaria = tempo(busca_binaria, minha_lista, numero_buscas)
    tempo_busca_sequencial = tempo(busca_sequencial, minha_lista, numero_buscas)
    tempo_busca_sequencial_otimizada = tempo(busca_sequencial_otimizada, minha_lista, numero_buscas)

    print(f"Tempo para a Busca Binária: {tempo_busca_binaria:.6f} ")
    print(f"Tempo para a Busca Sequencial: {tempo_busca_sequencial:.6f} ")
    print(f"Tempo para a Busca Sequencial Otimizada: {tempo_busca_sequencial_otimizada:.6f} ")
    plotar_grafico(tempo_busca_binaria, tempo_busca_sequencial, tempo_busca_sequencial_otimizada, size_list, numero_buscas)
