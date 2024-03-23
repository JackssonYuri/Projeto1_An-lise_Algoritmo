#Ordenação feita pelo quicksort
def quicksort(lista, inicio=0, fim=None):  #passei algumas declarações como padrão, meu fim é None caso não passe
    if fim is None:  #nesse caso se for pelo padrão, ele vai ser o último elemento da lista
        fim = len(lista)-1  
    if inicio < fim:
        p = partition(lista, inicio, fim) #essa minha outra função vai cortar a lista nos elementos menores e maiores que meu pivô, pois ela retorna o índice do meu pivô
        quicksort(lista, inicio, p-1) #lista dos menores que meu pivô, lembrando que p é meu índice do pivô
        quicksort(lista, p+1, fim) #lista dos maiores que meu pivô

def partition(lista, inicio, fim):
    pivot = lista[fim] #declarei na outra função o fim como o último elemento e vou usar ele como pivô
    i = inicio #meu primeiro elemento da lista, índice 0 na outra função
    for j in range(inicio, fim): #faço um for em toda a minha lista, o range não pega meu pivô(vai até o anterior dele)
        if lista[j] <= pivot:  #se o elemento atual da lista for menor ou = meu pivô
            lista[j], lista[i] = lista[i], lista[j] #dessa forma eu movo todos os elementos menores ou = ao meu pivô para a esquerda, formando uma lista dos menores que ele
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i] #troco meu pivô com o elemento no indice i da lista, isso faz com que meu pivô vá pra posição certa dele
    return i #retorna meu índice do pivô, isso me ajuda a criar duas listas: uma dos que são menores que o pivô e outra dos que são maiores que ele, dessa forma eu chamo meu quick sort novamente para ordena-los mas em listas menores

#o quicksort é um algoritmo de ordenação em que:
# 1 - escolho meu pivô, no caso escolhi o último elemento da lista
# 2 - eu crio uma lista dos elementos menores que meu pivô e outra lista dos maiores que meu pivô
# 3 - após fazer essa partição de 2 sub listas da minha lista dada, eu chamo o quicksort novamente
#     dessa forma eu tenho menos elementos para lidar e vejo tudo novamente
#     último elemtno da lista, crio novamente 2 sublistas e etc... 