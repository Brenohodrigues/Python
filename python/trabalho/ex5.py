
total=0



for i in range(2): 
    print("\n")     
    nome=input("informe o nome do produto:")
    quantidade=int(input("Informe a quantidade adquirida:"))
    preco=float(input("Informe o preço únitario do produto:"))
    total=(quantidade * preco)
    if quantidade <=5:
        desconto=total*(2/100)
    elif quantidade > 5 and quantidade <=10:
        desconto=total*(3/100)
    elif quantidade >10:
        desconto=total*(5/100)
    totalpg=(total-desconto)
    print("\n") 

    print(f"produto: {nome}")
    print(f"O valor total é de: R$ {total:.2f}")
    print(f"O valor do desconto é de: R${desconto:.2f}")
    print(f"O total a pagar com o desconto atribuido é de: R${totalpg:.2f}")

#ctrl+shift+l= mudança em todos os lugares que tiver o mesmo nome 

#ctrl+f= para pesquisar oque quer no arquivo

