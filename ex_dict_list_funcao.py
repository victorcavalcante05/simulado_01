# Exercicio para alunos de administracao e economia
# Evento Gastronomico realizado na faculdade para arrecadar fundos para uma entidade filantrópica
#Lista dos organizadores do evento
lst_organizadores = ['bento','mariana','saulo']
# Fornecedores do evento
dict_fornecedor = {
    0: {'nome': 'Pastel Frito', 'vendas': 3000},
    1: {'nome': 'Massa da Mama', 'vendas': 5000},
    2: {'nome': 'Pizza do Tio', 'vendas': 10000},
    3: {'nome': 'Rodizio Mineiro', 'vendas': 3900},
}
# Clientes que consumiram no evento
list_cliente = ['rafael','douglas','amanda','jorge','jeffri','carol','cristian',
 'leonardo','maria','luana','vanessa','jose','maria','bento','mariana','saulo',
 'glauco','ze','maria','bola']
# Despesas do evento
locacao = 0.10 # 10% das vendas
limpeza = 700
seguranca = 800
outras_despesas = 500

# 1 - Calcular o total de vendas usando o for loop no dict
total_vendas = 0
for fornecedor in dict_fornecedor.values():
    total_vendas += fornecedor['vendas']
    vendas = fornecedor['vendas']
    nome = fornecedor['nome']
    print(f"O fornecedor é {nome} e vendeu {vendas}")
print(total_vendas)
       
# 2 - Criar um dicionario com o nome e valor
dict_professores = {
    'Professor 01': 5000,
    'Professor 02': 5000,
    'Professor 03': 5000,
    'Professor 04': 5000,
    'Professor 05': 5000
}

# 3 - Criar uma lista com os nomes dos professores  
lst_professores = list(dict_professores.keys())

# 4 - Adicionar essa lista dos professores na lista de clientes
list_cliente.extend(lst_professores)

# 5 - Calcular quantas pessoas estiveram e a media de gasto por pessoa
quantidade_pessoas = len(set(list_cliente))
media_consumidor = total_vendas / quantidade_pessoas
print(quantidade_pessoas)
print(media_consumidor)

# 6 - Encontrar quem foi o 10 consumidor e retire da lista
list_cliente.remove(list_cliente[9])

# 7 - Encontre o nome "bola" inserido incorretamente na lista e retire da lista
list_cliente.append("bola")
if "bola" in list_cliente:
    list_cliente.remove("bola")
else:
    print("Nome 'bola' retirado dessa lista.")

# 8 - Verificar se todos os organizadores estao na lista
for nome in lst_organizadores:
 if nome in list_cliente:
     print(f'{nome} está na lista de pessoas presentes no evento')
 else:
    print(f'{nome} não esta na lista de pessoas presentes no evento')
# 9 - Tira-los da lista
list(set(list_cliente) - set(lst_organizadores))
print("os organizadores desse evento foram retirados da lista.")

# 10 - fazer uma funçao que calcule o lucro liquido do evento
desp_locacao = total_vendas * locacao
total_despesa = desp_locacao + limpeza + seguranca + outras_despesas

def calc_lucro_liquido(vendas, despesas):
    lucro = vendas, despesas
    return lucro
lucro_liquido = calc_lucro_liquido(total_vendas, total_despesa)
print(lucro_liquido)
# entrada dos parametros sao as vendas e as despesas
# criar um pacote e gravar o modulo com essa funcao
# importe o pacote com a funcao
# chame a funcao
# execute o programa