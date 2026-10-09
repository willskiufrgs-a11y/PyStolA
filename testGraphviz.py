import graphviz

dot = graphviz.Digraph(comment='Automaton')

# Define state nodes
dot.node('q0', 'q0', shape='circle')
dot.node('q1', 'q1', shape='doublecircle') # Final state

# Add transitions (arrows)
dot.edge('q0', 'q1', label='a')
dot.edge('q1', 'q1', label='b')

# Save and open image
dot.render('automaton', format='png', view=True)
