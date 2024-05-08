def verificar_forca_senha(senha):


  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."
  
  # TODO Verificando se a senha contém letras maiúsculas, minúsculas, números e caracteres especiais
    
  for char in senha:
    if char.isupper():
      tem_letra_maiuscula = True
    elif char.islower():
      tem_letra_minuscula = True
    elif char.isdigit():
      tem_numero = True
    else:
      tem_caractere_especial = True

  # TODO: Verificar o comprimento mínimo e critérios de validação
  
  if not tem_letra_maiuscula or not tem_letra_minuscula or not tem_numero or not tem_caractere_especial:
    return "Sua senha nao atende aos requisitos de seguranca."
  else:
    return "Sua senha atende aos requisitos de seguranca. Parabens!"
  

  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."



# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)