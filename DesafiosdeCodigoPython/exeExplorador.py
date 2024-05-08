# Desafio: A Aventura do Explorador

# Entrada
while True:
    try:
        quantidade_passos = int(input())
        if quantidade_passos >= 0:
            break
        else:
            print("Por favor, digite um número inteiro positivo ou zero.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")
else:
    for i in range(1, quantidade_passos + 1):
        if i == 1:
            print(f"Explorador: {i} passo")
        else:
            print(f"Explorador: {i} passos")