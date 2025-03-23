from tkinter import *  # Importa todos os componentes do módulo Tkinter.
root = Tk()  # Cria a janela principal da aplicação.
root.geometry("400x300")  # Define o tamanho da janela para 400x300 pixels.
root.resizable(0, 0)  # Desabilita a redimensionamento da janela.
root.config(bg="#303038")  # Define a cor de fundo da janela.
root.title("Cifra de Vigenère")  # Define o título da janela.

def cifra_vigenere(texto, chave):  # Define a função para cifrar o texto usando a cifra de Vigenère.
    resultado = ""  # Inicializa uma string vazia para armazenar o resultado.
    chave = chave.upper()  # Converte a chave para letras maiúsculas.
    texto = texto.upper()  # Converte o texto para letras maiúsculas.
    tamanho_chave = len(chave)  # Obtém o tamanho da chave.
    for i in range(len(texto)):  # Itera sobre cada caractere do texto.
        char = texto[i]  # Obtém o caractere atual.
        if char.isalpha():  # Verifica se o caractere é uma letra.
            deslocamento = ord(chave[i % tamanho_chave]) - ord('A')  # Calcula o deslocamento baseado na chave.
            novo_char = chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))  # Calcula o novo caractere cifrado.
            resultado += novo_char  # Adiciona o novo caractere ao resultado.
        else:
            resultado += char  # Adiciona caracteres não alfabéticos sem cifrar.
    return resultado  # Retorna o texto cifrado.

def decifra_vigenere(texto, chave):  # Define a função para decifrar o texto usando a cifra de Vigenère.
    resultado = ""  # Inicializa uma string vazia para armazenar o resultado.
    chave = chave.upper()  # Converte a chave para letras maiúsculas.
    texto = texto.upper()  # Converte o texto para letras maiúsculas.
    tamanho_chave = len(chave)  # Obtém o tamanho da chave.
    for i in range(len(texto)):  # Itera sobre cada caractere do texto.
        char = texto[i]  # Obtém o caractere atual.
        if char.isalpha():  # Verifica se o caractere é uma letra.
            deslocamento = ord(chave[i % tamanho_chave]) - ord('A')  # Calcula o deslocamento baseado na chave.
            novo_char = chr((ord(char) - ord('A') - deslocamento) % 26 + ord('A'))  # Calcula o novo caractere decifrado.
            resultado += novo_char  # Adiciona o novo caractere ao resultado.
        else:
            resultado += char  # Adiciona caracteres não alfabéticos sem decifrar.
    return resultado  # Retorna o texto decifrado.

def cifrar():  # Define a função que será chamada ao clicar no botão de cifrar.
    texto = frase.get()  # Obtém o texto da entrada.
    chave = chaves.get()  # Obtém a chave da entrada.
    texto_cifrado = cifra_vigenere(texto, chave)  # Cifra o texto usando a chave.
    resultado1.set(texto_cifrado)  # Atualiza a variável de resultado com o texto cifrado.

def decifrar():  # Define a função que será chamada ao clicar no botão de decifrar.
    texto = frase.get()  # Obtém o texto da entrada.
    chave = chaves.get()  # Obtém a chave da entrada.
    texto_decifrado = decifra_vigenere(texto, chave)  # Decifra o texto usando a chave.
    resultado1.set(texto_decifrado)  # Atualiza a variável de resultado com o texto decifrado.

def limpar():  # Define a função que será chamada ao clicar no botão de limpar.
    frase_entrada.delete(0, END)  # Limpa a entrada de texto.
    chaves_entrada.delete(0, END)  # Limpa a entrada da chave.

# Criação do título da aplicação.
titulo = Label(text="Cifra de Vigenère", 
               font=("Arial", "15", "bold"), bg="#4a4c4e", fg="#fdffff")
titulo.place(relx=0.3, rely=0.05)  # Posiciona o título na janela.

# Criação do rótulo para o campo "Frase".
texto_sub1 = Label(text="Frase:", 
                   font=("Arial", "12", "bold"), bg="#4a4c4e", fg="#000000")
texto_sub1.place(relx=0.15, rely=0.25)  # Posiciona o rótulo na janela.

# Criação do rótulo para o campo "Chave".
texto_sub2 = Label(text="Chave:", 
                   font=("Arial", "12", "bold"), bg="#4a4c4e", fg="#000000")
texto_sub2.place(relx=0.15, rely=0.4)  # Posiciona o rótulo na janela.

# Criação da entrada de texto para a frase.
frase = StringVar()  # Cria uma variável para armazenar o texto.
frase_entrada = Entry(textvariable=frase, 
                      font=("Arial", "12", "bold"), 
                      bg="white", fg="black", justify='center')
frase_entrada.place(relx=0.3, rely=0.25, relwidth=0.65)  # Posiciona a entrada na janela.

# Criação da entrada de texto para a chave.
chaves = StringVar()  # Cria uma variável para armazenar a chave.
chaves_entrada = Entry(textvariable=chaves, 
                       font=("Arial", "12", "bold"), 
                       bg="white", fg="black", justify='center')
chaves_entrada.place(relx=0.3, rely=0.4, relwidth=0.65)  # Posiciona a entrada na janela.

# Criação do botão para cifrar o texto.
but_cifrar = Button(text="Cifrar", bd=2, bg='#107db2', fg='white', 
                    font=('verdana', 12, 'bold'), command=cifrar)
but_cifrar.place(relx=0.05, rely=0.55, relwidth=0.25, relheight=0.1)  # Posiciona o botão na janela.

# Criação do botão para decifrar o texto.
but_decifrar = Button(text="Decifrar", bd=2, bg='#107db2', fg='white', 
                      font=('verdana', 12, 'bold'), command=decifrar)
but_decifrar.place(relx=0.35, rely=0.55, relwidth=0.25, relheight=0.1)  # Posiciona o botão na janela.

# Criação do botão para limpar os campos.
but_limpar = Button(text="Limpar", bd=2, bg='#107db2', fg='white', 
                    font=('verdana', 12, 'bold'), command=limpar)
but_limpar.place(relx=0.65, rely=0.55, relwidth=0.25, relheight=0.1)  # Posiciona o botão na janela.

# Criação do rótulo para exibir o resultado.
resultado1 = StringVar()  # Cria uma variável para armazenar o resultado.
resultado_texto = Label(textvariable=resultado1, 
                         font=("Arial", 12, "bold"), bg="#cfe2f3")
resultado_texto.place(relx=0.2, rely=0.75, relwidth=0.7, relheight=0.15)  # Posiciona o rótulo na janela.

root.mainloop()  # Inicia o loop principal da aplicação, permitindo interação com a interface.
