import random  # Para gerar valores aleatórios

# Função para gerar um produto com dados aleatórios
def gerar_produto(codigo):
    nome = f"Produto {codigo}"
    
    # Gera o estoque mínimo e máximo, garantindo que o máximo seja maior que o mínimo
    estoque_minimo = random.uniform(10, 30)
    estoque_maximo = random.uniform(estoque_minimo, 100)
    estoque = random.uniform(estoque_minimo, estoque_maximo)  # O estoque atual deve estar entre o mínimo e o máximo

    # Gera valores de preço e impostos
    preco_custo = random.uniform(10, 200)  # Preço de custo
    preco_venda = preco_custo + random.uniform(10, 50)  # Preço de venda é sempre maior que o custo
    icms = random.uniform(5, 18)  # Percentual de ICMS
    ipi = random.uniform(2, 10)   # Percentual de IPI
    
    # Calcula o lucro
    lucro = preco_venda - preco_custo

    # Cria um dicionário para armazenar os dados do produto
    produto = {
        "Código": codigo,
        "Nome": nome,
        "Estoque": round(estoque, 2),
        "Estoque Mínimo": round(estoque_minimo, 2),
        "Estoque Máximo": round(estoque_maximo, 2),
        "Preço de Custo": round(preco_custo, 2),
        "Preço de Venda": round(preco_venda, 2),
        "ICMS (%)": round(icms, 2),
        "IPI (%)": round(ipi, 2),
        "Lucro": round(lucro, 2)
    }
    
    return produto  # Retorna o dicionário do produto

# Função para gerar uma lista de produtos
def gerar_lista_produtos(quantidade):
    lista = []
    for codigo in range(1, quantidade + 1):
        produto = gerar_produto(codigo)
        lista.append(produto)  # Adiciona o produto à lista
    return lista

# Função para encontrar o produto com maior e menor valor em um campo específico
def encontra_maior(produtos, campo):
    maior_produto = produtos[0]  # Assume que o primeiro produto é o maior
    for produto in produtos:
        if produto[campo] > maior_produto[campo]:
            maior_produto = produto  # Atualiza se encontrar um valor maior
    return maior_produto

def encontra_menor(produtos, campo):
    menor_produto = produtos[0]  # Assume que o primeiro produto é o menor
    for produto in produtos:
        if produto[campo] < menor_produto[campo]:
            menor_produto = produto  # Atualiza se encontrar um valor menor
    return menor_produto

# Função para encontrar o produto com o menor ICMS > 0
def encontra_menor_icms_positivo(produtos):
    menor_icms_produto = None
    for produto in produtos:
        if produto["ICMS (%)"] > 0:
            if menor_icms_produto is None or produto["ICMS (%)"] < menor_icms_produto["ICMS (%)"]:
                menor_icms_produto = produto  # Atualiza se encontrar um valor menor
    return menor_icms_produto

# Função para exibir a lista completa de produtos em formato de tabela
def exibir_tabela_produtos(produtos):
    print(f"{'Código':<6}{'Nome':<12}{'Estoque':<10}{'Preço de Custo':<15}{'Preço de Venda':<15}{'ICMS (%)':<10}{'Lucro':<10}")
    print("-" * 70)
    for produto in produtos:
        print(f"{produto['Código']:<6}{produto['Nome']:<12}{produto['Estoque']:<10}{produto['Preço de Custo']:<15}{produto['Preço de Venda']:<15}{produto['ICMS (%)']:<10}{produto['Lucro']:<10}")

# Função para exibir a tabela de maiores e menores valores
def exibir_tabela_maiores_menores(produtos):
    # Encontrando os produtos para cada critério
    maior_preco = encontra_maior(produtos, "Preço de Venda")
    menor_preco = encontra_menor(produtos, "Preço de Venda")
    
    maior_estoque = encontra_maior(produtos, "Estoque")
    menor_estoque = encontra_menor(produtos, "Estoque")
    
    maior_icms = encontra_maior(produtos, "ICMS (%)")
    menor_icms = encontra_menor_icms_positivo(produtos)
    
    maior_lucro = encontra_maior(produtos, "Lucro")
    menor_lucro = encontra_menor(produtos, "Lucro")

    # Exibindo os resultados
    print("\nResumo de Maiores e Menores Valores:")
    print(f"{'Critério':<25}{'Nome':<15}{'Valor'}")
    print("-" * 50)
    print(f"Produto de maior preço: {'':<5}{maior_preco['Nome']:<15}R$ {maior_preco['Preço de Venda']}")
    print(f"Produto de menor preço: {'':<5}{menor_preco['Nome']:<15}R$ {menor_preco['Preço de Venda']}")
    print(f"Produto com maior estoque: {'':<5}{maior_estoque['Nome']:<15}{maior_estoque['Estoque']}")
    print(f"Produto com menor estoque: {'':<5}{menor_estoque['Nome']:<15}{menor_estoque['Estoque']}")
    print(f"Produto com maior ICMS: {'':<5}{maior_icms['Nome']:<15}{maior_icms['ICMS (%)']}%")
    print(f"Produto com menor ICMS > 0: {'':<5}{menor_icms['Nome']:<15}{menor_icms['ICMS (%)']}%")
    print(f"Produto com maior lucro: {'':<5}{maior_lucro['Nome']:<15}R$ {maior_lucro['Lucro']}")
    print(f"Produto com menor lucro: {'':<5}{menor_lucro['Nome']:<15}R$ {menor_lucro['Lucro']}")

# Gera uma lista de 10 produtos e exibe as tabelas
produtos = gerar_lista_produtos(10)
print("Tabela Completa de Produtos:")
exibir_tabela_produtos(produtos)

print("\n" + "=" * 70)
exibir_tabela_maiores_menores(produtos)
