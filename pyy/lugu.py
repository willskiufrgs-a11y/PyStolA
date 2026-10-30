from tkinter import *
from tkinter import ttk
class Global:
    id_counter = 0
    radius = 30
    
    

class Node:
    def __init__(self,name: str, is_final: bool, x,y, canvas, ID,radius):
        self.name = name
        self.is_final = is_final
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = ID
        radius
        self.oval_id = canvas.create_oval( x - radius, y - radius, x + radius, y + radius, fill="lightblue", outline="black", tags=("node",ID)) 
        self.text_id = canvas.create_text( x,y,text=name,font=("Arial",10,"bold"),tags=("node",ID))

class au_toma_toes: 
    def __init__(self):
        self.alphabet: list[str] = []
        self.nodes: list[Node()] = []
        self.edges: list[Edge()] = []
        self.start = Node
        self.final: list[Node()] = []

    def node_finder(self,node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None

    def edge_finder(self,edge_id):
        for edge in self.edges:
            if edge.id == edge_id:
                return edge
        return None


class stack_toes(au_toma_toes):
    def __init__(self):
        super().__init__()
        self.edges: list[Edge_stack()] = []
        self.stack_alphabet: list[str] = []


def get_points(node1,node2,toe,Global):
    N1 = toe.node_finder(node1[1])
    N2 = toe.node_finder(node2[1])

    Hip = (((N1.x - N2.x) ** 2) + ((N1.y - N2.y) ** 2)) ** (1/2)
    a = ((N1.x - N2.x) * Global.radius) / Hip
    b = ((N1.y - N2.y) * Global.radius) / Hip

    x1 = N1.x - a
    y1 = N1.y - b

    x2 = N2.x + a
    y2 = N2.y + b
    return [x1,y1,x2,y2]

def tapeCat(from_tape: list[str]) -> str:
    return ", ".join(from_tape)

class Edge:
    def __init__(self, from_state: Node, to_state: Node,canvas, from_tape: list[char],coords,ID):
        self.from_state = from_state
        self.to_state = to_state
        self.from_tape = from_tape
        self.id = ID
        self.arrow_id = canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=3,arrow=LAST,tags=("edge",ID))
        self.text_id = canvas.create_text( (coords[0] + coords[2]) / 2,(coords[1] + coords[3]) / 2,text=tapeCat(from_tape),font=("Arial",20,"bold"),tags=("edge",ID),fill="red")

class Edge_stack(Edge):
    def __init__(self, from_state: Node, to_state: Node, from_tape: str, from_stack: str):
        super().__init__(self, from_state, to_state, from_tape)
        self.from_stack = from_stack



def kill_edge(canvas, edge, toes):
    canvas.delete(edge.arrow_id)
    canvas.delete(edge.text_id)
    toes.edges.remove(edge)

def kill_node(canvas, n: Node, toes: au_toma_toes):
    for edge in toes.edges[:]:
        if edge.from_state.id == n.id or edge.to_state.id == n.id:
            kill_edge(canvas, edge, toes)
    canvas.delete(n.oval_id)
    canvas.delete(n.text_id)
    toes.nodes.remove(n)
    


def draw_node(event,canvas,toes: au_toma_toes, Global):
    radius = Global.radius
    X = event.x
    Y = event.y
    tmp_node = Node("q" + str(len(toes.nodes)),False,X,Y,canvas,Global.id_counter,Global.radius)
    toes.nodes.append(tmp_node)
    Global.id_counter = Global.id_counter + 1
                    

def draw_edge(node_start: Node,node_end: Node,canvas, toes: au_toma_toes, Global):
    radius = Global.radius
    coords = get_points(node_start,node_end,toes,Global)
    tmp_edge = Edge(toes.node_finder(node_start[1]),toes.node_finder(node_end[1]),canvas,["a","b"],coords,Global.id_counter)
    toes.edges.append(tmp_edge)
    Global.id_counter = Global.id_counter + 1


def tag_finder(event,canvas):
    """
    Given an event and canvas of origin, return a list with node tag and node id
    """
    clicked_on = canvas.find_withtag("current")
    for item in reversed(clicked_on):
        tagg = canvas.gettags(clicked_on)
        if "tmp_edge" in tagg:
            continue
        if "edge" in tagg:
            return [tagg[0],int(tagg[1])]
        if "node" in tagg:
            return [tagg[0],int(tagg[1])]
    return None

class mouse_class:
    def __init__(self):
        self.ctx = {
            "start_x": 0,  
            "start_y": 0, 
            "is_dragging": False,
            "source_tag": ["none",0],
            "tmp_edge": None
        }

    def on_click(self,event,canvas,toes,Global):
        X = event.x
        Y = event.y
        self.ctx["start_x"] = X
        self.ctx["start_y"] = Y
        self.ctx["is_dragging"] = False
        thing = tag_finder(event,canvas)
        self.ctx["source_tag"] = thing
        #print(thing)

    def on_drag(self, event, canvas, toes): 
        if self.ctx["source_tag"]:
            X = event.x
            Y = event.y
            dx = self.ctx["start_x"] - X
            dy = self.ctx["start_y"] - Y
            dist = ((dx ** 2) + (dy ** 2)) ** (1/2)
            if (dist > 4 and self.ctx["source_tag"][0] == "node") :
                self.ctx["is_dragging"] = True
                if not self.ctx["tmp_edge"]:
                    self.ctx["tmp_edge"] = canvas.create_line(self.ctx["start_x"],self.ctx["start_y"], X,Y, arrow=LAST, fill="red", width=4,tags=("tmp_edge",))
                else:
                    canvas.coords(
                            self.ctx["tmp_edge"],
                            self.ctx["start_x"], self.ctx["start_y"],
                            X,Y
                    )

    def on_release(self,event,canvas,toes,Global):
        X = event.x
        Y = event.y
        canvas.delete(self.ctx["tmp_edge"])
        self.ctx["tmp_edge"] = None
        self.ctx["is_dragging"] = False
        canvas.update_idletasks()
        current = tag_finder(event,canvas) 
        print(current)
        if not self.ctx["source_tag"]:
            if not current:
                draw_node(event,canvas,toes,Global) 
        else:
            if self.ctx["source_tag"][0] == "node":
                if current:
                    if current[0] == "node":
                        if current[1] != self.ctx["source_tag"][1]:
                            draw_edge(self.ctx["source_tag"],current,canvas,toes,Global)


    def on_r_click(self,event,canvas,toes):
        current = tag_finder(event,canvas)
        if current:
            if current[0] == "node":
                kill_node(canvas,toes.node_finder(current[1]),toes)
            if current[0] == "edge":
                kill_edge(canvas,toes.edge_finder(current[1]),toes)







# ------------------------- MAIN()
root = Tk()
drawCanvas = Canvas(root,height=500,width=500,bd=5,relief=GROOVE)
drawCanvas.pack()

global_class = Global()
main_toe = au_toma_toes()
mouseThing = mouse_class()

drawCanvas.bind('<ButtonPress-1>',lambda event:mouseThing.on_click(event,drawCanvas,main_toe,global_class))
drawCanvas.bind('<B1-Motion>',lambda event:mouseThing.on_drag(event,drawCanvas,main_toe))
drawCanvas.bind('<ButtonRelease-1>',lambda event:mouseThing.on_release(event,drawCanvas,main_toe,global_class))
drawCanvas.bind('<Button-3>',lambda event:mouseThing.on_r_click(event,drawCanvas,main_toe))

drawCanvas.bind('<Button-2>', lambda event: print(tag_finder(event,drawCanvas)))

Framester = Frame(root, relief="sunken")
Framester.pack()
lubul = Label(Framester, text="luguseima")
lubul.pack()

#tabela_tran = 









root.mainloop()
