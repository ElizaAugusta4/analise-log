import time
from collections import defaultdict

def monitorar_arquivo_log(caminho_arquivo_log):
    with open(caminho_arquivo_log, 'r', encoding='utf-8') as arquivo:
        arquivo.seek(0, 2) 
        while True:
            linha = arquivo.readline()
            if not linha:
                time.sleep(0.1)  
                continue
            yield linha

def analisar_logs(caminho_arquivo_log, padrao_analise):
    contador_ocorrencias = defaultdict(int)
    linhas_encontradas = []
    with open(caminho_arquivo_log, 'r') as arquivo:
        for linha in arquivo:
            if padrao_analise in linha:
                contador_ocorrencias[padrao_analise] += 1
                linhas_encontradas.append(linha.strip())

    print(f"Total de ocorrências de '{padrao_analise}': {contador_ocorrencias[padrao_analise]}")
    if contador_ocorrencias[padrao_analise] > 0:
        resposta = input("Deseja visualizar todas as linhas encontradas? (s/n): ")
        if resposta.lower() == 's':
            for linha_encontrada in linhas_encontradas:
                print(f"Linha: {linha_encontrada}")

def gerar_relatorio(contador_ocorrencias):
    print("------ Relatório de Análise de Logs ------")
    for padrao, contador in contador_ocorrencias.items():
        print(f"Padrão: {padrao} - Ocorrências: {contador}")
    print("-----------------------------------------")

caminho_do_arquivo = input("Insira o caminho do arquivo log: ")
padrao_analise = input("Insira o tipo de status que deseja contar: ")

analisar_logs(caminho_do_arquivo, padrao_analise)
