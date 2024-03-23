#Busca sequencial
def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if(lista[i] == item):
            # print(f"\nO número {item} foi encontrado na posição {i}.")
            return i
    return False

#a busca sequencial analisa o meu elemento atual com seu posterior, assim ela ai percorrendo a lista até achar o que quero
#o pior caso é quando o elemento está no final da lista e tem que percorrer ela toda