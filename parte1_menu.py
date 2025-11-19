def exibir_menu():
    print("\n=== PATHFINDER - RESOLVEDOR DE LABIRINTOS ===")
    print("1. Usar Labirinto Exemplo 1")
    print("2. Usar Labirinto Exemplo 2") 
    print("3. Usar Labirinto Exemplo 3")
    print("4. Criar Meu Próprio Labirinto")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ")

def carregar_labirinto_exemplo(numero):
    exemplos = {
        1: [
            ['S', '0', '1', '0', '0'],
            ['0', '0', '1', '0', '1'],
            ['1', '0', '1', '0', '0'],
            ['1', '0', '0', 'E', '1']
        ],
        2: [
            ['S', '0', '0', '0', '1'],
            ['1', '0', '1', '0', '0'],
            ['0', '0', '1', '1', '0'],
            ['0', '1', '0', 'E', '0']
        ],
        3: [
            ['0', 'S', '0', '1', '0'],
            ['0', '1', '0', '0', '0'],
            ['0', '0', '1', 'E', '0'],
            ['1', '0', '0', '0', '1']
        ]
    }
    return exemplos.get(numero)

def criar_labirinto_personalizado():
    print("\n=== CRIAR LABIRINTO PERSONALIZADO ===")
    print("Instruções:")
    print("- Use 'S' para ponto inicial")
    print("- Use 'E' para ponto final") 
    print("- Use '0' para caminhos livres")
    print("- Use '1' para obstáculos")
    print("- Separe os valores por espaços")
    print("- Todas as linhas devem ter o mesmo número de colunas")
    print("\nDigite seu labirinto (linha por linha, digite 'fim' para terminar):")
    
    labirinto = []
    while True:
        linha = input().strip()
        if linha.lower() == 'fim':
            break
        if linha:
            labirinto.append(linha.split())
    
    return labirinto

def validar_labirinto(labirinto):
    if not labirinto or not labirinto[0]:
        return False, "Labirinto vazio"
    
    num_colunas = len(labirinto[0])
    
    # Verificar se todas as linhas têm o mesmo número de colunas
    for i, linha in enumerate(labirinto):
        if len(linha) != num_colunas:
            return False, f"Linha {i} tem número diferente de colunas"
    
    # Verificar se existe caracteres válidos
    caracteres_validos = {'S', 'E', '0', '1'}
    count_S = 0
    count_E = 0
    
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula not in caracteres_validos:
                return False, f"Caractere inválido '{celula}' na posição ({i},{j})"
            if celula == 'S':
                count_S += 1
            if celula == 'E':
                count_E += 1
    
    # Verificar se tem exatamente um S e um E
    if count_S == 0:
        return False, "Ponto inicial 'S' não encontrado"
    if count_S > 1:
        return False, "Múltiplos pontos iniciais 'S' encontrados"
    if count_E == 0:
        return False, "Ponto final 'E' não encontrado"
    if count_E > 1:
        return False, "Múltiplos pontos finais 'E' encontrados"
    
    return True, "Labirinto válido"

def executar_sistema_menu():
    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            labirinto = carregar_labirinto_exemplo(1)
            print("\nLabirinto Exemplo 1 carregado!")
            return labirinto
            
        elif opcao == '2':
            labirinto = carregar_labirinto_exemplo(2)
            print("\nLabirinto Exemplo 2 carregado!")
            return labirinto
            
        elif opcao == '3':
            labirinto = carregar_labirinto_exemplo(3)
            print("\nLabirinto Exemplo 3 carregado!")
            return labirinto
            
        elif opcao == '4':
            labirinto = criar_labirinto_personalizado()
            valido, mensagem = validar_labirinto(labirinto)
            
            if valido:
                print("\n✓ Labirinto válido! Carregado com sucesso.")
                return labirinto
            else:
                print(f"\n✗ Erro: {mensagem}")
                print("Por favor, tente novamente.")
                
        elif opcao == '5':
            print("Saindo do programa...")
            return None
        else:
            print("Opção inválida! Escolha entre 1-5.")

# Teste independente da Parte 1
if __name__ == "__main__":
    print("=== TESTE DA PARTE 1 - SISTEMA DE MENU ===")
    labirinto_selecionado = executar_sistema_menu()
    
    if labirinto_selecionado:
        print("\nLabirinto selecionado:")
        for linha in labirinto_selecionado:
            print(' '.join(linha))
    else:
        print("Nenhum labirinto selecionado.")