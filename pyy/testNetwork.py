from pyvis.network import Network

# Initialize directed network
net = Network(directed=True, height="600px", width="100%")

# Add automaton states
net.add_node("q0", label="q0", color="#97C2FC")
net.add_node("q1", label="q1", color="#97C2FC")
net.add_node("q3", label="q3 (Final)", color="#FFFF00", shape="doubleCircle")

# Add transition arrows
net.add_edge("q0", "q1", label="a")
net.add_edge("q0", "q0", label="b")
net.add_edge("q1", "q3", label="b")
net.add_edge("q3", "q3", label="a, b")

# Enable physics configuration for easy node dragging
net.toggle_physics(True)

# Generate and view in browser
net.show("automaton.html", notebook=False)
