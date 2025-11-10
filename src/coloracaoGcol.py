import time
import gcol
import networkx as nx
import matplotlib.pyplot as plt


def colorir_grafo(G, algoritmo='dsatur'):
   
    #Aplica coloração de grafo usando a biblioteca GCol.
   
    inicio = time.perf_counter()
    resultado = {}

    try:
        if hasattr(gcol, "node_coloring"):
            resultado = gcol.node_coloring(G)

        elif hasattr(gcol, "coloring"):
            resultado = gcol.coloring(G)

        elif hasattr(gcol, "colour_graph"):
            resultado = gcol.colour_graph(G)

        else:
            raise RuntimeError(
                "Versão do GCol não possui nenhuma função de coloração reconhecida."
            )

    except Exception as e:
        raise RuntimeError(f"Falha ao aplicar algoritmo '{algoritmo}': {e}")

    tempo = time.perf_counter() - inicio
    num_cores = len(set(resultado.values()))

    return resultado, num_cores, tempo


def mostrar_grafo_colorido(G, coloracao):
    
    #Desenha o grafo com base na coloração obtida
    
    try:
        node_colors = gcol.get_node_colors(G, coloracao)
    except Exception:
        node_colors = list(coloracao.values())

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(
        G,
        pos=pos,
        node_color=node_colors,
        with_labels=True,
        node_size=1500,
        font_size=10,
        font_color="black"
    )
    plt.title("Grafo Colorido (Horários das Disciplinas)")
    plt.axis("off")
    plt.show()
