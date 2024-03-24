# o script é dedicado à demanda
import json
import csv

path_json = '../data_raw/dados_empresaA.json'
path_csv = "../data_raw/dados_empresaB.csv"


def leitura_json(path_json) -> dict:
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json


def leitura_csv(path_csv) -> dict:
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        dados_csv = list(map(lambda x: x, spamreader))
    return dados_csv


def leitura_dados(path, file_type) -> dict:
    if file_type == 'csv':
        return leitura_csv(path)
    elif file_type == 'json':
        return leitura_json(path)


def get_columns(dados):
    return list(dados[-1].keys())  # ponto de atenção.


def rename_columns(dados, key_mapping):
    return [{key_mapping.get(old_key): value for old_key, value
             in old_dict.items()} for old_dict in dados]


def size_data(dados):
    return len(dados)


def join(dados_A, dados_B):
    combined_list = []
    combined_list.extend(dados_A)
    combined_list.extend(dados_B)
    return combined_list


def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)


def transformando_dados_tabela(dados, nome_colunas):
    dados_combinados_tabela = [nome_colunas]  # primeira linha é o header

    for row in dados:
        linha = []
        for coluna in nome_colunas:
            linha.append(row.get(coluna, "Indisponível"))
        dados_combinados_tabela.append(linha)

    return dados_combinados_tabela


# Iniciando a leitura
dados_json = leitura_dados(path_json, 'json')
tamanho_dados_json = size_data(dados_json)

print(f'Nome colunas dados json: {get_columns(dados_json)}')
print(f'Tamanho do dados json: {tamanho_dados_json}')

dados_csv = leitura_dados(path_csv, 'csv')
tamanho_dados_csv = size_data(dados_csv)

print(f'Nome colunas dados csv: {get_columns(dados_csv)}')
print(f'Tamanho do dados csv: {tamanho_dados_csv}')

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}


# Transformacao de dados - etapas da regra de negócio
dados_csv = rename_columns(dados_csv, key_mapping)

print(f'Nome colunas dados csv: {get_columns(dados_csv)}')

# União dos dados
dados_fusao = join(dados_json, dados_csv)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)

print(f'Nome das colunas da Fusao: {nome_colunas_fusao}')
print(f'Tamanho dados fusao: {tamanho_dados_fusao}')

# Salvando dados - etapa feita e escolhida pela equipe de engenharia de dados.
# Note que as funções anteriores jã nao funcionam pois jã não temos uma lista
# de dicts , mas sim de listas.
dados_fusao_tabela = transformando_dados_tabela(
    dados_fusao, nome_colunas_fusao)


path_dados_combinados = '../data_processed/dados_combinados.csv'
salvando_dados(dados_fusao_tabela, path_dados_combinados)

print(path_dados_combinados)
