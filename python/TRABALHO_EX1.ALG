Algoritmo "Trabalho_ex1"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/10/2024
Var
// Seção de Declarações das variáveis 
numeros: vetor [1..10] de inteiro
i,soma,maior,menor: inteiro
media: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
soma:=0
maior:=0
menor:=98483

para i de 1 ate 10 faca
     escreva("Digite o ",i," numero:")
     leia(numeros[i])
     soma:= soma+ numeros[i]
     
     se numeros[i] > maior entao
        maior:= numeros[i]
     fimse
     
     se numeros[i] < menor entao
        menor:= numeros[i]
     fimse
     
     media:= soma/10
fimpara
escreval

escreval("O maior numero é: ", maior)
escreval("O menor numero é: ", menor)
escreval("A soma dos numeros é: ", soma)
escreval("A media dos numeros é: ", media)


     

Fimalgoritmo