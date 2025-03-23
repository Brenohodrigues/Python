nome = ""
idade = 0
mes = 0
dias = 0
total = 0 

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
mes = int(input("Digite o mes que vc esta: "))
dias = int(input("Digite o dia que vc esta: "))

total = (idade*365) + (mes*30) + (dias)

print(f"Você ja viveu por {total} dias.")