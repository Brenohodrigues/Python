numero=int(input("Digite um número:"))
print("Os números inferiores são:")
for i in range (numero - 50,numero+1):
    print(i, end=" ")
print("\n")

print("Os números superiores são:")
for i in range(numero,numero+51):
    print(i, end=" ")