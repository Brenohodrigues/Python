def calcular_porcentagem(parte, total):
    """Calcula a porcentagem de uma parte em relação ao total."""
    if total == 0:
        return 0
    return (parte / total) * 100

municipios = []
municipio_max_eleitores = None
municipio_max_vts_branco = None
municipio_max_vts_nulos = None
municipio_max_vts_validos = None


max_eleitores = -1
max_vts_branco = -1
max_vts_nulos = -1
max_vts_validos = -1


for i in range(2):
    print(f"\nCadastro do Município {i + 1}:")
    nome = input("Nome do município: ")
    vts_branco = int(input("Número de votos em branco: "))
    vts_nulos = int(input("Número de votos nulos: "))
    vts_validos = int(input("Número de votos válidos: "))
    eleitores = vts_validos + vts_nulos + vts_branco 

    municipio = {
        'nome': nome,
        'eleitores': eleitores,
        'vts_branco': vts_branco,
        'vts_nulos': vts_nulos,
        'vts_validos': vts_validos
    }
    municipios.append(municipio)

    if eleitores > max_eleitores:
        max_eleitores = eleitores
        municipio_max_eleitores = municipio

    if vts_branco > max_vts_branco:
        max_vts_branco = vts_branco
        municipio_max_vts_branco = municipio

    if vts_nulos > max_vts_nulos:
        max_vts_nulos = vts_nulos
        municipio_max_vts_nulos = municipio

    if vts_validos > max_vts_validos:
        max_vts_validos = vts_validos
        municipio_max_vts_validos = municipio

print("\n Resultado Municípios:")
for municipio in municipios:
    nome = municipio['nome']
    eleitores = municipio['eleitores']
    vts_branco = municipio['vts_branco']
    vts_nulos = municipio['vts_nulos']
    vts_validos = municipio['vts_validos']
    
    porcentagem_branco = calcular_porcentagem(vts_branco, eleitores)
    porcentagem_nulo = calcular_porcentagem(vts_nulos, eleitores)
    porcentagem_valido = calcular_porcentagem(vts_validos, eleitores)
    
    print(f"\nMunicípio: {nome}")
    print(f"Totais\t\tQuantidade\tPorcentagem")
    print(f"Eleitores\t{eleitores}\t\t100%")
    print(f"vts em branco\t{vts_branco}\t\t{porcentagem_branco:.2f}%")
    print(f"vts nulos\t{vts_nulos}\t\t{porcentagem_nulo:.2f}%")
    print(f"vts válidos\t{vts_validos}\t\t{porcentagem_valido:.2f}%")

print("\nResumo:")
if municipio_max_eleitores:
    print(f"Município com mais eleitores\t{municipio_max_eleitores['nome']}\t{municipio_max_eleitores['eleitores']}\t{calcular_porcentagem(municipio_max_eleitores['eleitores'], municipio_max_eleitores['eleitores']):.2f}%")

if municipio_max_vts_branco:
    print(f"Município com mais vts em branco\t{municipio_max_vts_branco['nome']}\t{municipio_max_vts_branco['vts_branco']}\t{calcular_porcentagem(municipio_max_vts_branco['vts_branco'], municipio_max_vts_branco['eleitores']):.2f}%")

if municipio_max_vts_nulos:
    print(f"Município com mais vts nulos\t{municipio_max_vts_nulos['nome']}\t{municipio_max_vts_nulos['vts_nulos']}\t{calcular_porcentagem(municipio_max_vts_nulos['vts_nulos'], municipio_max_vts_nulos['eleitores']):.2f}%")

if municipio_max_vts_validos:
    print(f"Município com mais vts válidos\t{municipio_max_vts_validos['nome']}\t{municipio_max_vts_validos['vts_validos']}\t{calcular_porcentagem(municipio_max_vts_validos['vts_validos'], municipio_max_vts_validos['eleitores']):.2f}%")