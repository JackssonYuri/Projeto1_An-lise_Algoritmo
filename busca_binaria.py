#busca binária
def busca_binaria(lista, item, start = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    if start <= fim: #verifico se a lista existe
        meio = (start + fim ) // 2
        # print('O índice do meio é: ', meio)
        if lista[meio] == item: #se o valor do meio for o que quero, ótimo, encontrei e retorno ele
            return meio
        #casos em que o item não é o do meio
        if item < lista[meio]: #verifico se o que eu quero é menor que o do meio, se for vou fazer a mesma busca só que pela esquerda
            return busca_binaria(lista, item, start, meio - 1)
        else:
            return busca_binaria(lista, item, meio + 1, fim)
    return None #pior caso em que não encontra o item na lista


# Obs: o meio me retorna o índice