from tkinter import *
from tkinter import ttk

class Node:
    def __init__(self,name: str, is_final: bool, x,y, canvas):
        self.name = name
        self.is_final = is_final
        self.canvas = canvas

        radius = 30
        self.oval_id = canvas.create_oval( x - radius, y - radius, x + radius, y + radius, fill="lightblue", outline="black") 
        self.text_id = canvas.create_text( x,y,text=name,font=("Arial",10,"bold"))

class au_toma_toes: 
    def __init__(self):
        self.alphabet: list[str] = []
        self.nodes: list[Node()] = []
        self.edges: list[Edge()] = []
        self.start = Node
        self.final: list[Node()] = []

class stack_toes(au_toma_toes):
    def __init__(self):
        super().__init__()
        self.edges: list[Edge_stack()] = []
        self.stack_alphabet: list[str] = []


class Edge:
    def __init__(self, from_state: Node, to_state: Node, from_tape: str):
        self.from_state = from_state
        self.to_state = to_state
        self.from_tape = from_tape

class Edge_stack(Edge):
    def __init__(self, from_state: Node, to_state: Node, from_tape: str, from_stack: str):
        super().__init__(self, from_state, to_state, from_tape)
        self.from_stack = from_stack




def draw_node(event,canvas,toes: au_toma_toes):
    print(f"Clicked at: {event.x}, {event.y}")  # <-- Add this!
    radius = 60
    X = event.x
    Y = event.y
    toes.nodes.append(Node("q" + str(len(toes.nodes)),False,X,Y,canvas))


# ------------------------- MAIN()
root = Tk()
drawCanvas = Canvas(root,height=500,width=500,bd=5,relief=GROOVE)
drawCanvas.pack()
#btn_add_node = Button(root,text="insert node",command=draw_node(drawCanvas,root.winfo_pointerx(),root.winfo_pointery(), 50))
#btn_add_node.pack()

main_toe = au_toma_toes()




drawCanvas.bind('<Button-1>',lambda event:draw_node(event,drawCanvas,main_toe))








root.mainloop()
