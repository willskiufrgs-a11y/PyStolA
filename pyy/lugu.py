from tkinter import *
from tkinter import ttk

class stack_toes(au_toma_toes):
    def __init__(self):
        super().__init__()
        self.edges: list[Edge_stack()] = []
        self.stack_alphabet: list[str] = []

class au_toma_toes: 
    def __init__(self):
        self.alphabet: list[str] = []
        self.nodes: list[Node()] = []
        self.edges: list[Edge()] = []
        self.inital = Node()
        self.final: list[Node()] = []

class Node:
    def __init__(self,name: str, is_final: bool):
        self.name = name
        self.is_final = is_final

class Edge:
    def __init__(self, from_state: Node, to_state: Node, from_tape: str):
        self.from_state = from_state: Node()
        self.to_state = to_state
        self.from_tape = from_tape

class Edge_stack(Edge):
    def __init__(self, from_state: Node, to_state: Node, from_tape: str, from_stack: str):
        super().__init__(self, from_state: Node, to_state: Node, from_tape: str)
        self.from_stack = from_stack









root = Tk()
drawCanvas = Canvas(root)
drawCanvas.pack()









root.mainloop()
