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
    
    


