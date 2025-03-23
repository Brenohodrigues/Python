idade = 0
diasv = 0
resposta = 0
decadas = 0.0
nome = ""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
diasv = idade * 365

resposta = int(input("Quer saber quantas décadas viveu? sim(1) nao(2): "))

if resposta == 1:
    decadas = idade / 10
    print(f"{nome}, você já viveu {diasv} dias de vida. Equivalente a {decadas:.1f} décadas.")
else:
    print(f"{nome}, você já viveu {diasv} dias de vida.")