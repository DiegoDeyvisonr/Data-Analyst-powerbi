# Ler a entrada do usuário
capacidade_atual, aumento_percentual = map(int, input().split())

def calcular_nova_capacidade(capacidade_atual, aumento_percentual):
    novo_aumento = capacidade_atual * (aumento_percentual / 100)
    nova_capacidade = capacidade_atual + novo_aumento
    return nova_capacidade


# Calcular a nova capacidade
nova_capacidade = calcular_nova_capacidade(capacidade_atual, aumento_percentual)

# Imprimir a nova capacidade
print(int(nova_capacidade))
