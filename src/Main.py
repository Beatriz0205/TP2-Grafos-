import sys
import networkx as nx
import matplotlib.pyplot as plt


try:
    from leituraDataset import carregar_conflitos
except Exception as e:
    print("Erro: não foi possível importar 'carregar_conflitos' de leituraDataset.py.")
    print("Verifique se o arquivo existe e contém a função esperada.")
    raise e


try:
    from coloracaoGcol import colorir_grafo, mostrar_grafo_colorido
except Exception as e:
    print("Erro: não foi possível importar 'colorir_grafo' ou 'mostrar_grafo_colorido' de coloracaoGcol.py.")
    print("Verifique se o arquivo existe e contém as funções esperadas.")
    raise e


def salvar_resultados_em_csv(coloring, caminho_saida='coloracao_resultado.csv'):
    import csv
    with open(caminho_saida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Disciplina', 'Cor'])
        for disc, cor in sorted(coloring.items()):
            writer.writerow([disc, cor])
    print(f"Resultados salvos em {caminho_saida}")


def main():
    # Import local apenas para garantir compatibilidade em alguns ambientes
    import matplotlib.pyplot as plt

    #leitura
    caminho_csv = sys.argv[1] if len(sys.argv) >= 2 else 'Dataset/grande.csv' or 'Dataset/medio.csv' or 'Dataset/pequeno.csv'
    arestas = carregar_conflitos(caminho_csv)

    # Se não conseguir ler o CSV, usa grafo de teste
    if not arestas:
        print("\nNenhum conflito foi carregado do arquivo CSV.")
        print("Verifique se o arquivo existe e está no formato correto (Disciplina1,Disciplina2).")
        return
        

    
    G = nx.Graph()
    G.add_edges_from(arestas)

    print(f"\nTotal de vértices (disciplinas): {G.number_of_nodes()}")
    print(f"Total de arestas (conflitos): {G.number_of_edges()}")

    # Mostra o grafo sem coloração
    #nx.draw(
      #  G,
      #  with_labels=True,
       # node_color="skyblue",
       # node_size=1200,
       # font_size=10
  #  )
    #plt.title("Grafo de Conflitos (sem coloração)")
    #plt.show()

    print("\nIniciando coloração do grafo...\n")

    algoritmos = ['dsatur', 'rlf', 'welsh-powell', 'random']
    resultados = {}

    for alg in algoritmos:
        try:
            coloring, num_cores, tempo = colorir_grafo(G, algoritmo=alg)
            resultados[alg] = {
                'coloring': coloring,
                'num_cores': num_cores,
                'tempo': tempo
            }
            print(f"[{alg}] → {num_cores} cores | tempo = {tempo:.4f}s")
        except Exception as e:
            print(f"Algoritmo {alg} falhou com erro: {e}")

    if not resultados:
        print("Nenhum algoritmo retornou resultado válido.")
        return

    # Escolhe o melhor resultado: menor nº de cores; se empatar, menor tempo
    melhor_nome, melhor_dados = min(resultados.items(),
                                    key=lambda kv: (kv[1]['num_cores'], kv[1]['tempo']))
    melhor_coloring = melhor_dados['coloring']

    print("\n===============================")
    print(" MELHOR RESULTADO ENCONTRADO ")
    print("===============================")
    print(f"Algoritmo: {melhor_nome}")
    print(f"Número mínimo de horários (cores): {melhor_dados['num_cores']}")
    print(f"Tempo de execução: {melhor_dados['tempo']:.4f} segundos\n")

    # Mostra o mapeamento 
    for disc, cor in sorted(melhor_coloring.items()):
        print(f"Disciplina {disc} → Horário {cor}")

    salvar_resultados_em_csv(melhor_coloring, 'coloracao_resultado.csv')

    print("\nExibindo o grafo colorido...")
    try:
        mostrar_grafo_colorido(G, melhor_coloring)
    except Exception as e:
        print(f"Erro ao desenhar grafo colorido: {e}")
        # Fallback simples usando colormap numérico
        try:
            node_color_values = [melhor_coloring.get(n, 0) for n in G.nodes()]
            pos = nx.spring_layout(G, seed=42)
            plt.figure(figsize=(8, 6))
            nx.draw_networkx(G, pos=pos, node_color=node_color_values, with_labels=True)
            plt.show()
        except Exception as e2:
            print(f"Erro no fallback de desenho: {e2}")


if __name__ == '__main__':
    main()
