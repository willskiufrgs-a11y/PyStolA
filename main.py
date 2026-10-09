from tkinter import *
from tkinter import ttk

root = Tk()
drawCanvas = Canvas(root)
drawCanvas.pack()

class automaton:
    #Estados espera lista de estados, onde cada estado é um trio ordenado com [str nome, int coord x, int coord y]
    estados = []
    # espera lista de tuplas
    # cada tupla começa com o nome do estado, seguida de duplas, cada dupla contem uma letra lida e o estado de destino;
    # ex. [["q0",[["a","q3"],["b","q2"]],["q0",[["a","q3"],["b","q2"]]]]]
    transicoes = []
    alfabeto = []
    eInicial: str 
    eFinais = []

    
def printAut(a : automaton):
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


def initAut(a : automaton):



def drawAut(a : automaton, canvas):
    return canvas.create_oval(249,234,40,34)

def create_circle(x, y, r, canvas): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1)

a1 = automaton()

a1.estados = ["q0","q1","q2"]
a1.alfabeto = ["a","b"]
a1.eInicial = "q0"
a1.eFinais = ["q3"]
a1.transicoes = [["q0",["a","q1"],["b","q0"]],["q1",["a","q1"],["b","q3"]],["q3",["a","q3"],["b","q3"]]]

#drawAut(a1,drawCanvas)
create_circle(100,100,300,drawCanvas)
printAut(a1)

print(type(drawCanvas))

root.mainloop()

