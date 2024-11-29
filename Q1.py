import os

def listar_arquivos_recursivo(dir):
    try:
        for item in os.listdir(dir):
            caminho_completo = os.path.join(dir, item)

            if os.path.isdir(caminho_completo):
                print(f"Diretório: {caminho_completo}")
                listar_arquivos_recursivo(caminho_completo)
    except OSError as e:
        print(f"Error accessing {dir}: {e}")

listar_arquivos_recursivo("/Users/maria/OneDrive/Documentos") 