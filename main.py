class automaton:
    #Estados espera lista de strings com nomes de estados
    estados = []
    # espera lista de tuplas
    # cada tupla começa com o nome do estado, seguida de duplas, cada dupla contem uma letra lida e o estado de destino;
    # ex. [["q0",[["a","q3"],["b","q2"]],["q0",[["a","q3"],["b","q2"]]]]]
    transicoes = []
    alfabeto = []
    eInicial: str 
    eFinais = []

    
def priAut(a : automaton):
    """Essa função deve receber um objeto automaton e uma palavra, retornando booleano caso a palavra seja reconhecida pelo automato"""
    
    print("Alfabeto reconhecido:")
    print(a.alfabeto)
    print("estados:")
    print(a.estados)
    print("transições:")
    print(a.transicoes)

    print("Estado inicial:")
    print(a.eInicial)
    print("Estados finais:")
    print(a.eFinais)



a1 = automaton()

a1.estados = ["q0","q1","q2"]
a1.alfabeto = ["a","b"]
a1.eInicial = "q0"
a1.eFinais = ["q3"]
a1.transicoes = [["q0",["a","q1"],["b","q0"]],["q1",["a","q1"],["b","q3"]],["q3",["a","q3"],["b","q3"]]]

priAut(a1)
