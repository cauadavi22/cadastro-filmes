# Lista para armazena os filmes
titulo = []
genero = []
ano = []
notas = []

# Função para cadastrar um filme
def cadastrar_filme():
    try:
        titulo_filme = str(input("Digite o título do filme: "))
        genero_filme = str(input("Digite o gênero do filme: "))
        ano_filme = int(input("Digite o ano do filme: "))
        nota_filme = float(input("Digite a nota do filme: "))

        # Adicionar filme
        titulo.append(titulo_filme)
        genero.append(genero_filme)
        ano.append(ano_filme)
        notas.append(nota_filme)
        print(f"Filme '{titulo_filme}' cadastrado com sucesso!")
    except ValueError:
        print("Erro: Por favor, insira um valor válido para o ano e a nota.")

# classificação do filme
def classificar_filme(nota):
    if nota >= 8:
        return "Bom"
    elif 5 <= nota < 8:
        return "Regular"
    else:
        return "Ruim"

# lista de classificação de filmes
def listar_filmes():
    filme_busca = input("Digite o nome do filme que deseja buscar: ")
    encontrado = False
    for i in range(len(titulo)):
        if filme_busca.lower() == titulo[i].lower():  # Comparando em minúsculas para não ter problema com maiúsculas
            classificacao = classificar_filme(notas[i])
            print(f"\nTitulo: {titulo[i]} - Gênero: {genero[i]} - Ano de Lançamento: {ano[i]} - Nota: {notas[i]} - Classificação: {classificacao}")
            encontrado = True
            break
    if not encontrado:
        print("Filme não encontrado.")

# busca por classificação
def buscar_por_classificacao():
    try:
        classificacao_desejada = input("Digite a classificação que deseja buscar (Bom, Regular, Ruim): ").strip().capitalize()

        # validação da classficação inserida
        if classificacao_desejada not in ["Bom", "Regular", "Ruim"]:
            print("Classificação inválida. Tente novamente.")
            return

        filmes_filtrados = list(filter(lambda i: classificar_filme(notas[i]) == classificacao_desejada, range(len(titulo))))

        if filmes_filtrados:
            print(f"\nFilmes classificados como '{classificacao_desejada}':")
            for i in filmes_filtrados:
                print(f"{titulo[i]} - {genero[i]} - {ano[i]} - Nota: {notas[i]}")
        else:
            print(f"Nenhum filme encontrado com a classificação '{classificacao_desejada}'.")
    except Exception as e:
        print(f"Erro ao buscar filmes: {e}")

#remover filme
def remover_filme():
    filme_remover = input("Digite o nome do filme que deseja remover: ")
    for i in range(len(titulo)):
        if filme_remover.lower() == titulo[i].lower():  # Comparando em minúsculas para não ter problema com maiúsculas
            titulo.pop(i)
            genero.pop(i)
            ano.pop(i)
            notas.pop(i)
            print(f"Filme '{filme_remover}' removido com sucesso!")
            return
    print("Filme não encontrado para remoção.")

#exibir estatísticas
def exibir_estatisticas():
    if not titulo:  
        print("Nenhum filme cadastrado.")
        return
    
    # Total de filmes
    total_filmes = len(titulo)
    
    # Média das notas
    media_notas = sum(notas) / total_filmes
    
    # Filme com a maior nota
    maior_nota = max(notas)
    indice_maior_nota = notas.index(maior_nota)
    filme_maior_nota = titulo[indice_maior_nota]
    
    # Filme com a menor nota
    menor_nota = min(notas)
    indice_menor_nota = notas.index(menor_nota)
    filme_menor_nota = titulo[indice_menor_nota]
    
    # Gênero mais repetido
    from collections import Counter
    contagem_generos = Counter(genero)
    genero_mais_comum = contagem_generos.most_common(1)[0][0]

    # Exibindo as estatísticas
    print("\n--- Estatísticas dos Filmes ---")
    print(f"Total de filmes cadastrados: {total_filmes}")
    print(f"Média das notas: {media_notas:.2f}")
    print(f"Filme com a maior nota: {filme_maior_nota} ({maior_nota})")
    print(f"Filme com a menor nota: {filme_menor_nota} ({menor_nota})")
    print(f"Gênero mais comum: {genero_mais_comum}")

# Menu principal
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar filme")
        print("2. Listar filmes")
        print("3. Remover filme")
        print("4. Exibir estatísticas")
        print("5. Buscar filmes por classificação")
        print("6. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            cadastrar_filme()
        elif opcao == '2':
            listar_filmes()
        elif opcao == '3':
            remover_filme()
        elif opcao == '4':
            exibir_estatisticas()
        elif opcao == '5':
            buscar_por_classificacao()
        elif opcao == '6':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Chamada da função do menu
menu()
