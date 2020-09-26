nome = input("qual é o seu nome?")

print("prazer em te conhecer {}".format(nome))
print("vamos treinar os tipos primitivos {} ok ?".format (nome))

valor = input("digite um valor e vamos analisalo!")

print("agora com o comando isupper vamos verificar se ele está em maiuscolo")
print("se der True é por que se verifica se der False é por que nâo se verifica")
print(valor.isupper())

print("agora com o isalnum vamos verificar se è alphanumeric ou seja se contem numeros e letras")
print(valor.isalnum())

print("com o is.alpha verificamos se é alfabético ou seja se só tem letras na sua composição")
print(valor.isalpha())

print("isalpha verifica se todos os caracteres são letras")
print(valor.isalpha())

print("isdigit verifica se todos os caracteres que vc respondeu são digitos")
print(valor.isdigit())

print("isdecimal verifica se os caracteres são decimais")
print(valor.isdecimal())

print("isnumeric verifica de os caracteres são numeros")
print(valor.isnumeric())

print("Verifica se a string for um identificador válido no Python")
print(valor.isidentifier())

print("islower certifica se a letra está em minúsculo")
print(valor.islower())

print("com is printable verifica se todos os caracteres são imprimiveis ou se a string está vazia")
print(valor.isprintable())

print("com o isspace ele te diz se é um espaço ou não")
print(valor.isspace())

print("istitle te diz se a sequencia é um titlo ou não")
print(valor.istitle())


