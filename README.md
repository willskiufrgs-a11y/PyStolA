# PyStolA


-> Today (28/10/2026) [madrugada]:

Adicionando a opção de deletar edges, juntamente com as edges conectadas a um nodo caso esse seja removido.

* CONFUSÃO: o output do thing_finder é algo do tipo ['node', id], mas as vezes isso se confunde com node_obj de modo que estava guardando a lista ao invez do node_obj em toes.

* Caso queira fazer diferenciações de tags entre node e node_text, basta modificar as tags...

--------------------------------------------------------------------------------------------------

-> Today (22/10/2026):

The thing started gaining shape, will keep the classes to both hold the info about automanton networks, nodes and edges, but also their canvas drawing methods, this way, say, a node instance hold the canvas_tag id of its circle and text, so that it is easy to manipulate it later while using canvas instead of widgets...

* Next steps are to do similar work to edges
* then work on functions such as move, delete, rename and such
* A frame holding the (toggle) buttons (buttons to toggle insert node mode, insert edge, remove, move, etc.)
* a region that holds the automaton network information, such as its characters, number of nodes, etc.
* later stuff that tests if a word is recognized by automaton....

** Need to add license!

--------------------------------------------------------------------------------------------------
-> Today (21/10/2026) made some guud first steps in object-orienting the things in python, mainly in the newly created "lugu.py"
--------------------------------------------------------------------------------------------------

Simple automaton simulator project

* Sobre o venv:

    1. Criando um diretório venv:
        python3 -m venv .venv
    2. Ativando:
        source .venv/bin/activate
    3. então pode instalar livrarias com pip..
    4. deactivate encerra a sessão venv
    
* Teve uma mãozinha pra fazer rodar a GUI
    Teve que abrir um display server...


* O script mais promissor até então é o "testCombinehtml.py"
    Já sendo capaz de gerar o automato em uma pagina html e ser capaz de testar palavras..


--------------------------------------------------------------------------------------------------




