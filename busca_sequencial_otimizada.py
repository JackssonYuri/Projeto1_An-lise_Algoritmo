# #Busca sequencial Otimizada(Linear)
def busca_sequencial_otimizada(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i  # Retorna o índice se o elemento for encontrado
    return None  # Retorna None se o elemento não estiver na lista