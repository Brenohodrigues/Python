import tkinter as tk  # Importa a biblioteca tkinter para criar a interface gráfica - NO CASO A JANELA.

# Inclui letras minúsculas, maiúsculas e o espaço no array abc
abc = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '  # Letras e espaço
]

# Correspondente de caracteres no array cod
cod = [
    '!', '@', '#', "'", '$', '%', '&', '(', ')', '+', '=', '§', '_', '-', '£', '¢', '¬', '.', ';', ':', '/',
    '?', 'º', '^', '~', ']', '}', '[', '{', '<', '>', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '`', '"', '*', ',', '\\', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'  # Caracteres que correspondem às letras
]

chave = 5  # Define a chave de rotação para a criptografia

# Função para abrir a janela de criptografia com o mesmo tamanho da janela original
def abrir_janela_criptografada(novaFrase):
    # Oculta a janela principal
    janela.withdraw()

    # Cria uma nova janela
    nova_janela = tk.Toplevel()
    nova_janela.title("Texto Criptografado")

    # Aplicando o tema escuro na nova janela
    

    # Obtém o tamanho da janela principal para replicar na segunda janela
    largura = janela.winfo_width()
    altura = janela.winfo_height()

    # Define o mesmo tamanho da janela principal na nova janela
    nova_janela.geometry(f"{largura}x{altura}")

    # Exibe o texto criptografado com fonte maior e cor destacada
    texto_label = tk.Label(nova_janela, text=novaFrase, font=("Arial", 16), fg="#000000", bg="#303038")
    texto_label.pack(pady=30)

    # Botão para descriptografar com cores customizadas
    botao_descriptografar = tk.Button(nova_janela, text="Descriptografar", command=lambda: descriptografar(nova_janela),
                                       font=("Arial", 12), activebackground="#555555")
    botao_descriptografar.pack(pady=10)

# Função de descriptografia
def descriptografar(nova_janela):
    novaLista = []  # Cria uma lista para armazenar os caracteres descriptografados
    shift = chave  # Usa a chave de rotação
    frase = entrada.get()  # Obtém a entrada do usuário (que agora está criptografada)
    
    for letra in frase:  # Itera por cada letra na frase de entrada
        if letra in cod:  # Verifica se a letra está no conjunto de caracteres codificados
            indice = (cod.index(letra) - shift) % len(cod)  # Calcula o novo índice para a descriptografia
            novaLetra = abc[indice] if indice < len(abc) else ' '  # Ajusta o índice para garantir que está dentro dos limites de abc
            novaLista.append(novaLetra)  # Adiciona a nova letra à lista

    novaFrase = ''.join(novaLista)  # Conecta a lista em uma string
    entrada.delete(0, tk.END)  # Limpa o campo de entrada
    entrada.insert(0, novaFrase)  # Insere a string descriptografada no campo de entrada

    nova_janela.destroy()  # Fecha a janela criptografada
    janela.deiconify()  # Reexibe a janela principal

# Função de criptografia
def crip():
    novaLista = []  # Cria uma lista para armazenar os caracteres criptografados
    shift = chave  # Usa a chave de rotação
    frase = entrada.get()  # Obtém a entrada do usuário
    for letra in frase:  # Itera por cada letra na frase de entrada
        if letra in abc:  # Verifica se a letra está no conjunto de caracteres definidos
            indice = (abc.index(letra) + shift) % len(abc)  # Calcula o novo índice
            novaLetra = cod[indice]  # Substitui a letra pela correspondente no array cod
            novaLista.append(novaLetra)  # Adiciona a nova letra à lista
    novaFrase = ''.join(novaLista)  # Concatena a lista em uma string
    entrada.delete(0, tk.END)  # Limpa o campo de entrada
    entrada.insert(0, novaFrase)  # Insere o texto criptografado no campo de entrada
    abrir_janela_criptografada(novaFrase)  # Abre a nova janela com o texto criptografado

# Configuração da janela principal
janela = tk.Tk()  # Cria a janela principal
janela.title("APS - Criptografia")  # Define o título da janela
janela.geometry("400x200")  # Define um tamanho padrão para a janela principal

# Aplicando tema escuro


# Entrada de texto
entrada = tk.Entry(janela, width=50, font=("Arial", 14))  # Cria um campo de entrada escuro
entrada.pack(pady=10)  # Adiciona o campo à janela com espaçamento vertical

# Botão para criptografar com tema escuro
botao_criptografar = tk.Button(janela, text="Criptografar", command=crip, font=("Arial", 12), activebackground="#555555")
botao_criptografar.pack(pady=5)

# Iniciar a aplicação
janela.mainloop()  # Inicia o loop principal da aplicação
