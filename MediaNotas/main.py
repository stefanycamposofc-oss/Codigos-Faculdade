#Código para calcular a média de 3 valores inseridos pelo usuário

N1 = float(input("Digite a Primeira nota: "))
N2 = float(input("Digite a Segunda nota: "))
N3 = float(input("Digite a Terceira nota: "))
media = (N1+N2+N3)/3

if media <= 5:
    print (f"Sua média é {media} e Você está de recuperação!")
elif media >= 6 and media <= 7:
    print (f"Sua média é {media} e sua nota está muito Baixa!")
else:
    print (f"Sua média é {media} e você está aprovado!")
