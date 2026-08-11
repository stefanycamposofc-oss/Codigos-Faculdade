soma = 0
numero = -1

print("Digite os números que quer somar. Digite 0 para encerrar.")

while numero != 0:
    numero = int(input("Digite um número: "))
    soma = soma + numero

print(f"A soma total de todos os números digitados é: {soma}")
