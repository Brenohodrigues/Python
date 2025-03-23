import tkinter as tk  # Importa a biblioteca tkinter para criar a interface gráfica

# Inclui letras minúsculas, maiúsculas e o espaço no array abc
abc = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '  # Letras e espaço
]

# Correspondente de caracteres no array cod
cod = [
    '!', '@', '#', "'", '$', '%', '&', '(', ')', '+', '=', '§', '_', '-', '£', '¢', '¬', '.', ';', ':', '/',
    '?', 'º', '^', '~', ']', '}', '[', '{', '<', '>', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '`', '"', '*', ',', '\\', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'  # Caracteres que correspondem às letras
]

# Função de criptografia
def crip():
    novaLista = []  # Cria uma lista para armazenar os caracteres criptografados
    shift = int(rotacao.get())  # Obtém a chave de rotação
    frase = entrada.get()  # Obtém a entrada do usuário

    for letra in frase:  # Itera por cada letra na frase de entrada
        if letra in abc:  # Verifica se a letra está no conjunto de caracteres definidos
            indice = (abc.index(letra) + shift) % len(abc)  # Calcula o novo índice
            novaLista.append(cod[indice])  # Substitui a letra pela correspondente no array cod

    novaFrase = ''.join(novaLista)  # Concatena a lista em uma string
    abrir_janela_criptografada(novaFrase)  # Abre a nova janela com o texto criptografado

# Função para abrir a janela de criptografia
def abrir_janela_criptografada(novaFrase):
    janela.withdraw()  # Oculta a janela principal
    nova_janela = tk.Toplevel()  # Cria uma nova janela
    nova_janela.title("Texto Criptografado")  # Define o título da nova janela
    nova_janela.geometry("400x300")  # Define o tamanho da nova janela
    nova_janela.config(bg="#303038")  # Aplica tema escuro

    # Exibe o texto criptografado com fonte maior e cor destacada
    texto_label = tk.Label(nova_janela, text=novaFrase, font=("Arial", 16, "bold"), fg="#fdffff", bg="#303038")
    texto_label.pack(pady=30)

    # Label para "Rotação"
    label_rotacao = tk.Label(nova_janela, text="Rotação:", font=("Arial", 12), bg="#303038", fg="#fdffff")
    label_rotacao.pack(pady=5)

    # Entrada para chave de descriptografia
    chave_decifrar = tk.Entry(nova_janela, font=("Arial", 12), justify='center', bg="white", fg="black")
    chave_decifrar.pack(pady=10)
    chave_decifrar.insert(0, "Rotação")  # Placeholder para o campo de rotação

    # Botão para descriptografar
    botao_descriptografar = tk.Button(nova_janela, text="Descriptografar", 
                                       command=lambda: descriptografar(nova_janela, chave_decifrar.get(), novaFrase),
                                       font=("Arial", 12, "bold"), activebackground="#555555", bg='#107db2', fg='white')
    botao_descriptografar.pack(pady=10)

# Função de descriptografia
def descriptografar(nova_janela, chave, frase):
    try:
        shift = int(chave)  # Obtém a chave de rotação
        novaLista = []  # Cria uma lista para armazenar os caracteres descriptografados

        for letra in frase:  # Itera por cada letra na frase de entrada
            if letra in cod:  # Verifica se a letra está no conjunto de caracteres codificados
                indice = (cod.index(letra) - shift) % len(cod)  # Calcula o novo índice para a descriptografia
                novaLista.append(abc[indice])  # Adiciona a nova letra à lista

        novaFrase = ''.join(novaLista)  # Conecta a lista em uma string
        resultado_label = tk.Label(nova_janela, text=novaFrase, font=("Arial", 14), fg="#fdffff", bg="#303038")  # Cria um rótulo para o resultado
        resultado_label.pack(pady=20)  # Adiciona o rótulo à janela

    except ValueError:
        # Se a chave não for um número, exibe uma mensagem de erro
        erro_label = tk.Label(nova_janela, text="Rotação inválida!", font=("Arial", 12), fg="red", bg="#303038")
        erro_label.pack(pady=10)

# Configuração da janela principal
janela = tk.Tk()  # Cria a janela principal
janela.title("APS - Criptografia")  # Define o título da janela
janela.geometry("400x300")  # Define um tamanho padrão para a janela principal
janela.config(bg="#303038")  # Aplica tema escuro

# Título
titulo = tk.Label(janela, text="Cifra de César", font=("Arial", 15, "bold"), bg="#4a4c4e", fg="#fdffff")
titulo.pack(pady=10)

# Label para "Frase"
label_frase = tk.Label(janela, text="Frase:", font=("Arial", 12), bg="#303038", fg="#fdffff")
label_frase.pack(pady=5)

# Entrada de texto
entrada = tk.Entry(janela, width=50, font=("Arial", 14), bg="white", fg="black")  # Cria um campo de entrada
entrada.pack(pady=10)  # Adiciona o campo à janela com espaçamento vertical

# Label para "Rotação"
label_rotacao = tk.Label(janela, text="Rotação:", font=("Arial", 12), bg="#303038", fg="#fdffff")
label_rotacao.pack(pady=5)

# Entrada de rotação
rotacao = tk.Entry(janela, width=10, font=("Arial", 14), bg="white", fg="black")  # Cria um campo para entrada de rotação
rotacao.pack(pady=10)  # Adiciona o campo à janela com espaçamento vertical

# Botão para criptografar
botao_criptografar = tk.Button(janela, text="Criptografar", command=crip, font=("Arial", 12, "bold"), activebackground="#555555", bg='#107db2', fg='white')
botao_criptografar.pack(pady=5)  # Adiciona o botão à janela

# Iniciar a aplicação
janela.mainloop()  # Inicia o loop principal da aplicação
