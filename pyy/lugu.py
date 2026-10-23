from tkinter import *
from tkinter import ttk

class Node:
    def __init__(self,name: str, is_final: bool, x,y, canvas):
        self.name = name
        self.is_final = is_final
        self.canvas = canvas
        self.x = x
        self.y = y

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
    def __init__(self, from_state: Node, to_state: Node, from_tape: list[char], canvas):
        self.from_state = from_state
        self.to_state = to_state
        self.from_tape = from_tape
        self.arrow_id = canvas.create_line(self.from_state.x,self.from_state.y,self.to_state.x,self.to_state.y,arrow=tk.LAST)

class Edge_stack(Edge):
    def __init__(self, from_state: Node, to_state: Node, from_tape: str, from_stack: str):
        super().__init__(self, from_state, to_state, from_tape)
        self.from_stack = from_stack



def kill_node(event, canvas, n: node, toes: au_toma_toes):
    canvas.delete(n.oval_id)
    canvas.delete(n.text_id)
    toes.nodes.remove(n)


def draw_node(event,canvas,toes: au_toma_toes):
    radius = 60
    X = event.x
    Y = event.y
    tmp_node = Node("q" + str(len(toes.nodes)),False,X,Y,canvas)
    toes.nodes.append(tmp_node)
    canvas.tag_bind(tmp_node.oval_id,'<Button-3>', lambda event, n=tmp_node, canvas=canvas, toes=toes: kill_node(event, canvas, n, toes)) 
    canvas.tag_bind(tmp_node.text_id,'<Button-3>', lambda event, n=tmp_node, canvas=canvas, toes=toes: kill_node(event, canvas, n, toes)) 
                    

def draw_edge(event,canvas,node: Node, toes: au_toma_toes, start: bool):
    print(f"Clicked at: {event.x}, {event.y}")  # <-- Add this!
    radius = 60
    X = event.x
    Y = event.y
    tmp_edge = Edge()
    toes.edges.append(tmp_node)


# ------------------------- MAIN()
root = Tk()
drawCanvas = Canvas(root,height=500,width=500,bd=5,relief=GROOVE)
drawCanvas.pack()
#btn_add_node = Button(root,text="insert node",command=draw_node(drawCanvas,root.winfo_pointerx(),root.winfo_pointery(), 50))
#btn_add_node.pack()

main_toe = au_toma_toes()




drawCanvas.bind('<Button-1>',lambda event:draw_node(event,drawCanvas,main_toe))
drawCanvas.tag_bind(tmp_node.oval_id,'<Button-1>', lambda event, n=tmp_node, canvas=canvas, toes=toes: draw_edge(event, canvas, n, toes,True)) 
drawCanvas.tag_bind(tmp_node.oval_id,'<B1-Motion>', lambda event, n=tmp_node, canvas=canvas, toes=toes: kill_node(event, canvas, n, toes)) 








root.mainloop()
