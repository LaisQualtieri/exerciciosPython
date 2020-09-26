v= float(input("Qual o valor do produto desejado que receberá o desconto:R$"))
d= v * 5 / 100
vt= v - d
print("o valor do produto é R$ {:.2f}\no desconto de 5% é R$ {:.2f}\nou seja o valor a ser pago é de R${:.2f}".format(v, d, vt))
