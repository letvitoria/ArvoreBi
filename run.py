#Em prática
class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

def inserir(raiz, chave):
    # Se a árvore (ou subárvore) estiver vazia, cria um novo nó
    if raiz is None:
        return No(chave)

    # Se a chave for menor, vai para a esquerda
    if chave < raiz.chave:
        raiz.esquerda = inserir(raiz.esquerda, chave)
    # Se for maior ou igual, vai para a direita
    else:
        raiz.direita = inserir(raiz.direita, chave)

    return raiz

def exibir_em_ordem(raiz):
    """Percorre a árvore em-ordem (Esquerda, Raiz, Direita).
    Em uma BST, isso sempre exibe os números em ordem crescente!"""
    if raiz:
        exibir_em_ordem(raiz.esquerda)
        print(raiz.chave, end=" ")
        exibir_em_ordem(raiz.direita)

# 1. Iniciamos a árvore vazia (sem raiz)
raiz = None

#Lista de números para inserir
numeros = [50, 30, 20, 40, 70, 60, 80]

print("Inserindo os números na árvore...")
for num in numeros:
    raiz = inserir(raiz, num)

#Exibindo o resultado
print("\nCaminhamento Em-Ordem (Elementos ordenados):")
exibir_em_ordem(raiz)
print()  