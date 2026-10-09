from pyvis.network import Network
import os
import webbrowser

# 1. Initialize directed network
net = Network(directed=True, height="600px", width="100%")

# 2. Add states
# Use a hidden dummy node to point to the start state
net.add_node("start_dummy", shape="text", label="START", color="rgba(0,0,0,0)")
net.add_node("q0", label="q0", shape="circle", color="#97C2FC")
net.add_node("q1", label="q1", shape="circle", color="#97C2FC")
# PyVis doesn't have a 'doublecircle', so we use a thicker border and yellow color for final states
net.add_node("q3", label="q3", shape="circle", color="#FFFF00", borderWidth=4)

# 3. Add transitions
net.add_edge("start_dummy", "q0") # Arrow pointing to start state
net.add_edge("q0", "q1", label="a")
net.add_edge("q0", "q0", label="b")
net.add_edge("q1", "q3", label="b")
net.add_edge("q3", "q3", label="a, b")

net.toggle_physics(True)

# Generate the initial HTML file
file_name = "automaton.html"
net.write_html(file_name)

# 4. Define the custom UI and JavaScript logic to inject
custom_ui_and_js = """
<div style="position: absolute; top: 20px; left: 20px; z-index: 1000; background: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 8px; border: 1px solid #ccc; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); font-family: sans-serif;">
    <h3 style="margin-top: 0;">Test Word</h3>
    <input type="text" id="wordInput" placeholder="e.g., abba" style="padding: 5px;">
    <button onclick="testWord()" style="padding: 5px 10px; cursor: pointer;">Run</button>
    <p id="resultText" style="font-weight: bold; margin-bottom: 0;"></p>
</div>

<script>
function testWord() {
    const word = document.getElementById('wordInput').value;
    const resultText = document.getElementById('resultText');
    
    // Define the automaton logic here
    const transitions = {
        'q0': { 'a': 'q1', 'b': 'q0' },
        'q1': { 'a': null, 'b': 'q3' }, // null means no valid transition
        'q3': { 'a': 'q3', 'b': 'q3' }
    };
    
    let currentState = 'q0';
    const finalStates = ['q3'];

    // Process each character
    for (let char of word) {
        if (transitions[currentState] && transitions[currentState][char]) {
            currentState = transitions[currentState][char];
        } else {
            resultText.innerText = `Rejected: No transition for '${char}' in state ${currentState}`;
            resultText.style.color = "red";
            return;
        }
    }

    // Check if we ended in a final state
    if (finalStates.includes(currentState)) {
        resultText.innerText = `Accepted! Ended in ${currentState}`;
        resultText.style.color = "green";
    } else {
        resultText.innerText = `Rejected: Ended in non-final state ${currentState}`;
        resultText.style.color = "red";
    }
}
</script>
"""

# 5. Read the generated HTML, inject the code right after <body>, and overwrite
with open(file_name, "r", encoding="utf-8") as f:
    html_content = f.read()

html_content = html_content.replace("<body>", "<body>\n" + custom_ui_and_js)

with open(file_name, "w", encoding="utf-8") as f:
    f.write(html_content)

# Automatically open it in the default browser
webbrowser.open('file://' + os.path.realpath(file_name))
