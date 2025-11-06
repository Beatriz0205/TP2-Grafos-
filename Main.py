import networkx as nx
import matplotlib.pyplot as plt

#==============================================
#antes de rodar o codigo va no terminal e intale
#pip3 install networkx matplotlib gcol
#depois pode compilar
#===============================================

G = nx.Graph() # Criar o grafo

# so para teste deve ser substituido pela leitura
conflitos = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E")
]

G.add_edges_from(conflitos)# esse adiciona todos os conflitos
#  G.add_edge(a, b) cria uma ligação por vez precisa de um for

# mostra o grafo sem esta colorido
nx.draw(
    G,
    with_labels=True,
    node_color="skyblue",  # mesma cor pra todos
    node_size=1500,
    font_size=10
)
plt.show()

#depois dele aqui deve vir as funçoes de colorir


#pode usar para mostra ele colorido, mas pesquisar melhor
# pos = gcol.coloring_layout(G, c)
# Desenhar
#nx.draw_networkx(G, pos=pos, node_color=cores, with_labels=True) acho que esta certo passo o grafo, suas posiçoes, suas cores e fala pra ele por os nomes
#plt.show()
