Algoritmo "Trabalho_ex1"
// 
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/10/2024
Var
// Se��o de Declara��es das vari�veis 
numeros: vetor [1..10] de inteiro
i,soma,maior,menor: inteiro
media: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
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

escreval("O maior numero �: ", maior)
escreval("O menor numero �: ", menor)
escreval("A soma dos numeros �: ", soma)
escreval("A media dos numeros �: ", media)


     

Fimalgoritmo