# Lista para armazenar os itens
itens = []

# Solicite os itens ao usuário

for i in range(3):
    entrada = input()
    itens.append(entrada)


# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")