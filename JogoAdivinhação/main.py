import random

numero_secreto = random.randint(1, 100)
tentativa = 0
max_tentativas = 10

while tentativa < max_tentativas:
    numero_digitado = int(input("Digite um número de 1 a 100: "))
    tentativa += 1

    if numero_digitado == numero_secreto:
        print(f"Você acertou o número em {tentativa} tentativa(s)!!!")
        break
    elif numero_digitado > numero_secreto:
        print("O número secreto é menor!")
    else:
        print("O número secreto é maior!")

    print(f"Tentativa {tentativa} de {max_tentativas}")

    if tentativa == max_tentativas:
        print(f"Você esgotou suas tentativas! O número secreto era {numero_secreto}.")
