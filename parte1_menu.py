import random

def exibir_menu_principal():
    print("\n=== FLOOD FILL - COLORAÇÃO DE REGIÕES ===")
    print("1. Usar Grid Exemplo 1")
    print("2. Usar Grid Exemplo 2") 
    print("3. Usar Grid Exemplo 3")
    print("4. Criar Meu Próprio Grid")
    print("5. Gerar Grid Aleatório")
    print("6. Sair")
    return input("Escolha uma opção (1-6): ")

def exibir_menu_floodfill():
    print("\n=== OPÇÕES FLOOD FILL ===")
    print("1. Preencher região a partir de coordenadas específicas")
    print("2. Preencher automaticamente todas as regiões")
    print("3. Voltar ao menu principal")
    return input("Escolha uma opção (1-3): ")

def exibir_menu_geracao_automatica():
    print("\n=== GERAR GRID ALEATÓRIO ===")
    print("1. Grid Pequeno (5x5)")
    print("2. Grid Médio (8x8)")
    print("3. Grid Grande (12x12)")
    print("4. Grid Personalizado (definir dimensões)")
    print("5. Voltar")
    return input("Escolha uma opção (1-5): ")

def exibir_menu_probabilidade():
    print("\n=== PROBABILIDADE DE OBSTÁCULOS ===")
    print("1. Baixa (20% obstáculos) - Muitas áreas livres")
    print("2. Média (35% obstáculos) - Balanceado")
    print("3. Alta (50% obstáculos) - Muitos obstáculos")
    print("4. Personalizada (definir porcentagem)")
    print("5. Voltar")
    return input("Escolha uma opção (1-5): ")

def carregar_grid_exemplo(numero):
    exemplos = {
        1: [
            ['0', '0', '1', '0', '0'],
            ['0', '1', '1', '0', '0'],
            ['0', '0', '1', '1', '1'],
            ['1', '1', '0', '0', '0']
        ],
        2: [
            ['0', '1', '0', '0', '1'],
            ['0', '1', '0', '0', '1'],
            ['0', '1', '1', '1', '1'],
            ['0', '0', '0', '1', '0']
        ],
        3: [
            ['0', '0', '0', '1', '0', '0'],
            ['0', '1', '0', '0', '0', '1'],
            ['0', '1', '1', '1', '0', '0'],
            ['1', '0', '0', '0', '1', '0']
        ]
    }
    return exemplos.get(numero)

def criar_grid_personalizado():
    print("\n=== CRIAR GRID PERSONALIZADO ===")
    print("Instruções:")
    print("- Use '0' para áreas livres (navegável)") 
    print("- Use '1' para obstáculos (não navegável)")
    print("- Separe os valores por espaços")
    print("- Todas as linhas devem ter o mesmo número de colunas")
    print("\nDigite seu grid (linha por linha, digite 'fim' para terminar):")
    
    grid = []
    while True:
        linha = input().strip()
        if linha.lower() == 'fim':
            break
        if linha:
            grid.append(linha.split())
    
    return grid

def gerar_grid_aleatorio():
    """Gera grids aleatórios com diferentes configurações"""
    while True:
        opcao = exibir_menu_geracao_automatica()
        
        if opcao == '1':
            return _gerar_grid_com_probabilidade(5, 5, 0.2)  # 20% obstáculos
        
        elif opcao == '2':
            return _gerar_grid_com_probabilidade(8, 8, 0.35)  # 35% obstáculos
        
        elif opcao == '3':
            return _gerar_grid_com_probabilidade(12, 12, 0.5)  # 50% obstáculos
        
        elif opcao == '4':
            return _gerar_grid_personalizado()
        
        elif opcao == '5':
            return None
        else:
            print("Opção inválida! Escolha entre 1-5.")

def _gerar_grid_personalizado():
    """Gera grid com dimensões e probabilidade personalizadas"""
    try:
        print("\n=== DIMENSÕES PERSONALIZADAS ===")
        linhas = int(input("Número de linhas: "))
        colunas = int(input("Número de colunas: "))
        
        if linhas <= 0 or colunas <= 0:
            print("Dimensões devem ser maiores que zero!")
            return None
        
        # Menu de probabilidade
        prob_opcao = exibir_menu_probabilidade()
        probabilidade = 0.35  # padrão
        
        if prob_opcao == '1':
            probabilidade = 0.2
        elif prob_opcao == '2':
            probabilidade = 0.35
        elif prob_opcao == '3':
            probabilidade = 0.5
        elif prob_opcao == '4':
            try:
                percentual = float(input("Digite a porcentagem de obstáculos (0-100): "))
                probabilidade = percentual / 100.0
                if not 0 <= probabilidade <= 1:
                    print("Porcentagem deve estar entre 0 e 100!")
                    return None
            except ValueError:
                print("Digite um número válido!")
                return None
        elif prob_opcao == '5':
            return None
        else:
            print("Opção inválida!")
            return None
        
        grid = _gerar_grid_com_probabilidade(linhas, colunas, probabilidade)
        print(f"Grid {linhas}x{colunas} gerado com {probabilidade*100:.0f}% de obstáculos")
        return grid
        
    except ValueError:
        print("Digite números válidos!")
        return None

def _gerar_grid_com_probabilidade(linhas: int, colunas: int, prob_obstaculo: float) -> list:
    """Gera um grid aleatório com a probabilidade especificada de obstáculos"""
    grid = []
    
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            # Gera número aleatório entre 0 e 1
            if random.random() < prob_obstaculo:
                linha.append('1')  # Obstáculo
            else:
                linha.append('0')  # Área livre
        grid.append(linha)
    
    # Garantir que há pelo menos algumas células livres
    celulas_livres = sum(1 for linha in grid for celula in linha if celula == '0')
    if celulas_livres == 0:
        # Se não há células livres, criar algumas
        for _ in range(min(3, linhas * colunas)):
            x = random.randint(0, linhas - 1)
            y = random.randint(0, colunas - 1)
            grid[x][y] = '0'
    
    return grid

def validar_grid(grid):
    """Valida se o grid é válido para Flood Fill"""
    if not grid or not grid[0]:
        return False, "Grid vazio"
    
    num_colunas = len(grid[0])
    
    # Verificar se todas as linhas têm o mesmo número de colunas
    for i, linha in enumerate(grid):
        if len(linha) != num_colunas:
            return False, f"Linha {i} tem número diferente de colunas"
    
    # Verificar se existem apenas caracteres válidos
    caracteres_validos = {'0', '1'}
    
    for i, linha in enumerate(grid):
        for j, celula in enumerate(linha):
            if celula not in caracteres_validos:
                return False, f"Caractere inválido '{celula}' na posição ({i},{j}). Use apenas '0' e '1'"
    
    return True, "Grid válido"

def obter_coordenadas_iniciais(grid):
    """Obtém coordenadas iniciais para o Flood Fill do usuário"""
    print("\n Digite as coordenadas iniciais para Flood Fill:")
    try:
        x = int(input("Coordenada X (linha, 0-indexed): "))
        y = int(input("Coordenada Y (coluna, 0-indexed): "))
        
        # Validar coordenadas
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            print(f" Coordenadas fora dos limites! Grid: {len(grid)}x{len(grid[0])}")
            return None
        
        if grid[x][y] == '1':
            print(" Coordenada inicial é um obstáculo! Escolha uma posição com valor '0'")
            return None
            
        return (x, y)
    except ValueError:
        print(" Por favor, digite números válidos!")
        return None

def executar_sistema_menu(callback_processar_grid=None):
    """Sistema principal de menu para seleção de grid
    
    Args:
        callback_processar_grid: Função opcional que será chamada com o grid selecionado.
                                 Se None, retorna o grid. Se fornecida, processa o grid e continua o loop.
    """
    while True:
        opcao = exibir_menu_principal()
        
        if opcao in ['1', '2', '3']:
            grid = carregar_grid_exemplo(int(opcao))
            print(f"\nGrid Exemplo {opcao} carregado!")
            if callback_processar_grid:
                callback_processar_grid(grid)
            else:
                return grid
            
        elif opcao == '4':
            grid = criar_grid_personalizado()
            valido, mensagem = validar_grid(grid)
            
            if valido:
                print("\n✓ Grid válido! Carregado com sucesso.")
                if callback_processar_grid:
                    callback_processar_grid(grid)
                else:
                    return grid
            else:
                print(f"\n✗ Erro: {mensagem}")
                print("Por favor, tente novamente.")
                # Continua no loop para tentar novamente
                
        elif opcao == '5':
            grid = gerar_grid_aleatorio()
            if grid:
                print(f"\n Grid aleatório {len(grid)}x{len(grid[0])} gerado com sucesso!")
                if callback_processar_grid:
                    callback_processar_grid(grid)
                else:
                    return grid
            # Se grid é None, usuário voltou, então continua no loop
            
        elif opcao == '6':
            print("\nSaindo do programa...")
            if callback_processar_grid:
                break  # Sai do loop
            else:
                return None
        else:
            print("\nOpção inválida! Escolha entre 1-6.")

# Teste independente da Parte 1
if __name__ == "__main__":
    print("=== TESTE DA PARTE 1 - SISTEMA DE MENU ===")
    
    def processar_grid(grid):
        """Função para processar o grid selecionado"""
        print(f"\nGrid selecionado ({len(grid)}x{len(grid[0])}):")
        for linha in grid:
            print(' '.join(linha))
        
        # Estatísticas do grid
        celulas_livres = sum(1 for linha in grid for celula in linha if celula == '0')
        total_celulas = len(grid) * len(grid[0])
        percentual_livre = (celulas_livres / total_celulas) * 100
        print(f"\n Estatísticas: {celulas_livres}/{total_celulas} células livres ({percentual_livre:.1f}%)")
        print("\n" + "="*50)
    
    # Executa o menu em loop até que o usuário escolha sair
    executar_sistema_menu(callback_processar_grid=processar_grid)
    print("Programa encerrado.")