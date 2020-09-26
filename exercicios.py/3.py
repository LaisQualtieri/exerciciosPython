#formato antigo, talvez por não ser um código bonito
#print("hora da calculadora, primeiro soma")
#n1=int(input("digite um número:"))
#n2=int(input("digite outro número:"))
#soma=n1+n2
#print("a soma entre", n1,"e", n2,"é" soma)

print("hora da calculadora, primeiro soma")

n1=int(input("digite um número:"))
n2=int(input("digite outro número:"))
soma=n1+n2
print("a soma vale",soma)


#formato atual e mais atualizado por motivos óbvios
print("agora subtração")

n1=int(input("digite um número:"))
n2=int(input("digite outro número:"))
subtração=n1-n2
print("a subtração entre {} e {} é {}".format(n1, n2, subtração))

print("agora multiplicação")

n1=int(input("digite um número:"))
n2=int(input("digite outro número:"))
multiplicação=n1*n2
print("a multiplicação entre {} e {} é {}".format(n1, n2, multiplicação))

print("agora divisão")

n1=int(input("digite um número:"))
n2=int(input("digite outro número:"))
divisão=n1/n2
print("a divisão entre {} e {} é {}".format(n1, n2, divisão))

print("potência")
n1=int(input("digite a base:"))
n2=int(input("digite o expoente:"))
potência= n1**n2
print("a potência de {} ao {} é {}".format(n1, n2, potência))

#ou

print("potência")
n1=int(input("digite a base:"))
n2=int(input("digite o expoente:"))
print("o resultado é:", pow(n1, n2))















print("parabéns pelo exercicio concluido :)")
