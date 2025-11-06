import pandas as pd

def carregar_conflitos(caminho_do_arquivo_csv):
    
    try:
        
        df = pd.read_csv(caminho_do_arquivo_csv)
        
        lista_de_arestas = []
        
        # Itera por cada linha do arquivo lido
        for index, linha in df.iterrows():
            d1 = linha['Disciplina1']
            d2 = linha['Disciplina2']
            
            # Adiciona a tupla na lista
            lista_de_arestas.append((d1, d2))
            
        print(f"Arquivo {caminho_do_arquivo_csv} lido com sucesso.")
        print(f"Total de {len(lista_de_arestas)} conflitos (arestas) encontrados.")
        
        return lista_de_arestas
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo_csv}' não foi encontrado.")
        return [] # Retorna uma lista vazia em caso de erro
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return []
    
    


#main temporario
if __name__ == "__main__":
    
   
    NOME_ARQUIVO_CSV = 'grande.csv' 
    
    print(f"--- Iniciando teste da Parte 1 (Leitura Dataset) ---")
    
    arestas_do_grafo = carregar_conflitos(NOME_ARQUIVO_CSV)
    
    if arestas_do_grafo:
        print(f"\n--- Teste BEM-SUCEDIDO para '{NOME_ARQUIVO_CSV}' ---")
        print(f"Total de {len(arestas_do_grafo)} conflitos (arestas) encontrados.")
        print("\nAs 5 primeiras arestas carregadas:")
        print(arestas_do_grafo[:5])
        print("\nAs 5 ultimas arestas carregadas:")
        print(arestas_do_grafo[-5:])
    else:
        print(f"\n--- Teste FALHOU para '{NOME_ARQUIVO_CSV}' ---")
        print("A lista de arestas esta vazia")
