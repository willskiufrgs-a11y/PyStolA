from tkinter import *
from tkinter import ttk
import math
class Global:
    id_counter = 0
    radius = 30
    
    
    

class Node:
    def __init__(self,name: str, is_final: bool, x,y, canvas, ID,radius,toes):
        self.name = name
        self.is_final = is_final
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = ID
        self.radius = radius
        self.oval_id = canvas.create_oval( x - radius, y - radius, x + radius, y + radius, fill="lightblue", outline="black", tags=("node",ID)) 
        self.text_id = canvas.create_text( x,y,text=name,font=("Arial",10,"bold"),tags=("node",ID))
        self.start_arrow_id = None
        self.end_oval_id = None
        self.toes = toes

    def toggle_start(self):
        if not self.toes.start:
            self.start_arrow_id = self.canvas.create_line(self.x - 1.3 * self.radius, self.y - 1.3 * self.radius,self.x + self.radius * math.cos(3*math.pi/4),self.y - self.radius * math.sin(3*math.pi/4),width=5,arrow=LAST,tags=("start_edge",self.id))
            self.toes.start = self
        else:
            if self.toes.start == self:
                self.canvas.delete(self.start_arrow_id)
                self.start_arrow_id = None
                self.toes.start = None

    def toggle_end(self):
        if not self in self.toes.final:
            self.end_oval_id = self.canvas.create_oval( self.x - self.radius + 5, self.y - self.radius + 5, self.x + self.radius - 5, self.y + self.radius - 5,width=5,  outline="black", tags=("end_oval", self.id)) 
            self.toes.final.append(self)
        else:
            self.canvas.delete(self.end_oval_id)
            self.toes.final.remove(self)
            self.end_oval_id = None
    



class au_toma_toes: 
    def __init__(self):
        self.alphabet: list[str] = []
        self.nodes: list[Node()] = []
        self.edges: list[Edge()] = []
        self.start = None
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
    
    def set_starting_node(self,node):
        self.start = node
    def unset_starting_node(self):
        self.start = None

    def set_ending_node(self,node):
        self.final = node
    def unset_ending_node(self):
        self.final = None

class stack_toes(au_toma_toes):
    def __init__(self):
        super().__init__()
        self.edges: list[Edge_stack()] = []
        self.stack_alphabet: list[str] = []


def get_points(node1,node2,toe,Global):
    ret = []
    if node1 != node2:
        N1 = toe.node_finder(node1[1])
        N2 = toe.node_finder(node2[1])

        Hip = (((N1.x - N2.x) ** 2) + ((N1.y - N2.y) ** 2)) ** (1/2)
        a = ((N1.x - N2.x) * Global.radius) / Hip
        b = ((N1.y - N2.y) * Global.radius) / Hip

        x1 = N1.x - a
        y1 = N1.y - b

        x2 = N2.x + a
        y2 = N2.y + b
        ret.append(x1)
        ret.append(y1)
        ret.append(x2)
        ret.append(y2)
    else: 
        angle_1 = math.pi * 0.3   # angulo que localiza o ponto tangente do nodo (como ponteiro em relogio)
        radius2 = Global.radius * 1.5
        number_subpoints = 25
        hip = (Global.radius ** 2 + radius2 ** 2) ** (1/2)
        N = toe.node_finder(node1[1])
        centerX = N.x + math.cos(angle_1) * hip # coords of smaller circle
        centerY = N.y - math.sin(angle_1) * hip # coords of smaller circle

        # coordenada do primeiro ponto tangeente ao Nodo
        xi1 = N.x + math.cos(angle_1) * Global.radius
        yi1 = N.y - math.sin(angle_1) * Global.radius
        ret.append(xi1)
        ret.append(yi1)

        slices = (2 * math.pi - 2 * angle_1) / number_subpoints
        for i in range(0,number_subpoints,1): 
            xtemp = centerX + math.cos(i*slices) * radius2
            ytemp = centerY - math.sin(i*slices) * radius2
            ret.append(xtemp)
            ret.append(ytemp)

        # coordenada do ultimo ponto tangeente ao Nodo
        xf1 = N.x + math.cos((2) * angle_1) * Global.radius
        yf1 = N.y - math.sin((2) * angle_1) * Global.radius
        ret.append(xf1)
        ret.append(yf1)
    print(ret)
    return ret

def tapeCat(from_tape: list[str]) -> str:
    return ", ".join(from_tape)

def tapeParse(unparsed: str) -> list[str]:
    tmpList = []
    for character in unparsed.replace(" ","").replace(",",""):
        if not character in tmpList:
            tmpList.append(character)
    return tmpList

class Edge:
    def __init__(self, from_state: Node, to_state: Node,canvas, from_tape: list[char],coords,ID):
        self.from_state = from_state
        self.to_state = to_state
        self.from_tape = from_tape
        self.id = ID
        self.coords = coords
        self.arrow_id = canvas.create_line(coords,width=3,arrow=LAST,tags=("edge",ID))
        #self.arrow_id = canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=3,arrow=LAST,tags=("edge",ID))
        self.text_id = canvas.create_text((coords[0] + coords[2]) / 2,(coords[1] + coords[3]) / 2,text=tapeCat(from_tape),font=("Arial",20,"bold"),tags=("edge",ID),fill="red")
        

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
    if n.start_arrow_id:
        canvas.delete(n.start_arrow_id)
        toes.start = None
    if n.end_oval_id:
        canvas.delete(n.end_oval_id)
        toes.final.remove(n)
    
    toes.nodes.remove(n)
    


def draw_node(event,canvas,toes: au_toma_toes, Global):
    radius = Global.radius
    X = event.x
    Y = event.y
    tmp_node = Node("q" + str(len(toes.nodes)),False,X,Y,canvas,Global.id_counter,Global.radius,toes)
    toes.nodes.append(tmp_node)
    Global.id_counter = Global.id_counter + 1
                    

def draw_edge(node_start: Node,node_end: Node,canvas, toes: au_toma_toes, Global):
    radius = Global.radius
    coords = get_points(node_start,node_end,toes,Global)
    tmp_edge = Edge(toes.node_finder(node_start[1]),toes.node_finder(node_end[1]),canvas,[""],coords,Global.id_counter)
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
    def __init__(self,canvas,toes,Global,selected):
        self.selected = selected
        self.Global = Global
        self.canvas = canvas
        self.toes = toes
        self.ctx = {
            "start_x": 0,  
            "start_y": 0, 
            "is_dragging": False,
            "source_tag": ["none",0],
            "tmp_edge": None
        }

    def del_tmp_edge(self):
        self.canvas.delete(self.ctx["tmp_edge"])
        self.ctx["tmp_edge"] = None
        self.canvas.update_idletasks()

    def on_click(self,event):
        X = event.x
        Y = event.y
        self.ctx["start_x"] = X
        self.ctx["start_y"] = Y
        self.ctx["is_dragging"] = False
        thing = tag_finder(event,self.canvas)
        self.ctx["source_tag"] = thing
        #print(thing)

    def on_drag(self, event): 
        if self.ctx["source_tag"]:
            X = event.x
            Y = event.y
            dx = self.ctx["start_x"] - X
            dy = self.ctx["start_y"] - Y
            dist = ((dx ** 2) + (dy ** 2)) ** (1/2)
            if (dist > 24 and self.ctx["source_tag"][0] == "node") :
                self.ctx["is_dragging"] = True
                if not self.ctx["tmp_edge"]:
                    self.ctx["tmp_edge"] = self.canvas.create_line(self.ctx["start_x"],self.ctx["start_y"], X,Y, arrow=LAST, fill="red", width=4,tags=("tmp_edge",))
                else:
                    self.canvas.coords(
                            self.ctx["tmp_edge"],
                            self.ctx["start_x"], self.ctx["start_y"],
                            X,Y
                    )

    def on_release(self,event):
        X = event.x
        Y = event.y
        self.del_tmp_edge()
        current = tag_finder(event,self.canvas) 
        print(current)
        if not self.ctx["source_tag"]:
            if not current:
                self.selected.delete_selected()
                draw_node(event,self.canvas,self.toes,self.Global) 
            else:    # Toggles initial node if releasing with no source node
                self.selected.delete_selected()
                self.toes.node_finder(current[1]).toggle_start()
        else:
            if self.ctx["source_tag"][0] == "node":
                if current:
                    if current[0] == "node":
                        if current[1] != self.ctx["source_tag"][1]:
                            self.selected.delete_selected()
                            draw_edge(self.ctx["source_tag"],current,self.canvas,self.toes,self.Global)
                        elif self.ctx["is_dragging"]:
     #----------------->    # Draw edge to itself!
                            self.selected.delete_selected()
                            draw_edge(self.ctx["source_tag"],current,self.canvas,self.toes,self.Global)


                            self.selected.delete_selected()
                            self.selected.tagV = current
                            self.selected.draw_node()
            elif self.ctx["source_tag"][0] == "edge":
                if current:
                    if current[0] == "edge":
                        if current[1] == self.ctx["source_tag"][1]:
                           self.selected.delete_selected()
                           self.selected.tagV = current
                           self.selected.draw_edge()

        self.ctx["is_dragging"] = False


    def on_r_click(self,event):
        current = tag_finder(event,self.canvas)
        if current:
            if current[0] == "node":
                kill_node(self.canvas,self.toes.node_finder(current[1]),self.toes)
            if current[0] == "edge":
                kill_edge(self.canvas,self.toes.edge_finder(current[1]),self.toes)

class Selected:
    def __init__(self, canvas, Global, toes,start_button,end_button,edge_field,edge_button):
        self.tagV = None
        self.canvas = canvas
        self.Global = Global
        self.toes = toes
        self.Radius = Global.radius + 5
        self.oval_id = None
        self.arrow_id = None
        self.start_button = start_button
        self.end_button = end_button
        self.edge_field = edge_field
        self.edge_button = edge_button

    def draw_node(self):
        self.oval_id = self.canvas.create_oval(self.toes.node_finder(self.tagV[1]).x - self.Radius,self.toes.node_finder(self.tagV[1]).y - self.Radius,self.toes.node_finder(self.tagV[1]).x + self.Radius,self.toes.node_finder(self.tagV[1]).y + self.Radius,outline="orange", tags=("selected_node"),width=5)
        self.start_button.config(state=NORMAL)
        self.end_button.config(state=NORMAL)
        

    def draw_edge(self):
        self.edge_field.config(state="normal")
        self.edge_button.config(state="normal")
        self.arrow_id = self.canvas.create_line(self.toes.edge_finder(self.tagV[1]).coords[0],self.toes.edge_finder(self.tagV[1]).coords[1],self.toes.edge_finder(self.tagV[1]).coords[2],self.toes.edge_finder(self.tagV[1]).coords[3],width=5,arrow=LAST,tags=("selected_edge"),fill="orange")
        self.edge_field.delete(0,END)
      # for index, character in enumerate(self.toes.edge_finder(self.tagV[1]).from_tape):
      #     self.edge_field.insert(index,character)
        self.edge_field.insert(0,tapeCat(self.toes.edge_finder(self.tagV[1]).from_tape))                                      

    def get_edge(self):
        string = self.edge_field.get()
        string_list = tapeParse(string)
        selectedEdge = self.toes.edge_finder(self.tagV[1])
        selectedEdge.from_tape = string_list 
        print(self.toes.edge_finder(self.tagV[1]).from_tape)
        self.edge_field.delete(0,END)
        self.edge_field.insert(0,tapeCat(string_list))
        self.canvas.itemconfig(selectedEdge.text_id,text=tapeCat(string_list))
        

    
    def delete_selected(self):
        if self.oval_id:
            self.canvas.delete(self.oval_id)
            self.oval_id = None
            self.tagV = None
            self.start_button.config(state=DISABLED)
            self.start_button.deselect()
            self.end_button.config(state=DISABLED)
            self.end_button.deselect()
            self.edge_field.delete(0,END)
        if self.arrow_id:
            self.canvas.delete(self.arrow_id)
            self.arrow_id = None
            self.tagV = None
            self.edge_field.delete(0,END)
            self.edge_field.config(state="disabled")
            self.edge_button.config(state="disabled")
        

            dsf






# ------------------------- MAIN()
root = Tk()
#drawCanvas = Canvas(root,height=500,width=500,bd=5,relief=GROOVE)
drawCanvas = Canvas(root,height=450,width=450,relief=GROOVE,bd=4, bg="white")
drawCanvas.pack(fill=BOTH,expand=True,padx=10,pady=(10,5))



# --------------------------- Frame & Options

botton_frame = Frame(root, relief="groove", bd=5)
botton_frame.pack()

node_frame = Frame(botton_frame, relief="groove",bd=5) 
edge_frame = Frame(botton_frame, relief="groove",bd=5)
node_frame.pack(side="left", padx=10)
edge_frame.pack(side="right", padx=10)

edge_label = Label(edge_frame,text="Transições",font=("Arial",19,"bold"))
node_label = Label(node_frame,text="Estados",font=("Arial",19,"bold"))
edge_label.pack()
node_label.pack()

#   lubul = Button(botton_frame, text="Testar Palavra!",font=("Arial",14,"bold"), relief=RAISED, bd=3,bg="lightyellow" )
#   lubul.pack()

edge_button = Button(edge_frame,state="disabled", text="Modificar Seta",font=("Arial",14,"bold"), relief=RAISED, bd=3,bg="lightyellow",command=lambda: selected_class.get_edge())
edge_button.pack()

edge_entry = Entry(edge_frame,font=("arial",14,"bold"),state="disabled")
edge_entry.pack()


button_is_start = Checkbutton(node_frame, text="Estado Inicial?",font=("arial",14,"bold"), relief=RAISED, bd=3,bg="lightyellow",state=DISABLED, command=lambda: selected_class.toes.node_finder(selected_class.tagV[1]).toggle_start())
button_is_end = Checkbutton(node_frame, text="Estado Terminal?",font=("arial",14,"bold"), relief=RAISED, bd=3,bg="lightyellow",state=DISABLED, command=lambda: selected_class.toes.node_finder(selected_class.tagV[1]).toggle_end())

button_is_start.pack()
button_is_end.pack()




# -------- Classes init



global_class = Global()
main_toe = au_toma_toes()
selected_class = Selected(drawCanvas,global_class,main_toe,button_is_start,button_is_end,edge_entry,edge_button)                                        
mouseThing = mouse_class(drawCanvas,main_toe,global_class,selected_class)



# ----------------- Binds

drawCanvas.bind('<ButtonPress-1>',lambda event:mouseThing.on_click(event))
drawCanvas.bind('<B1-Motion>',lambda event:mouseThing.on_drag(event))
drawCanvas.bind('<ButtonRelease-1>',lambda event:mouseThing.on_release(event))
drawCanvas.bind('<Button-3>',lambda event:mouseThing.on_r_click(event))

drawCanvas.bind('<Button-2>', lambda event: print(tag_finder(event,drawCanvas)))











root.mainloop()
