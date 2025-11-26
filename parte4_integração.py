from parte1_menu import executar_sistema_menu, validar_grid, obter_coordenadas_iniciais, exibir_menu_floodfill
from Parte2_FloodFill import flood_fill_region, fill_all_regions
from parte3_visualizacao import VisualizadorResultado

def converter_grid_para_inteiros(grid_str):
    """Converte grid de strings para inteiros"""
    grid_int = []
    for linha in grid_str:
        linha_int = []
        for celula in linha:
            linha_int.append(int(celula))
        grid_int.append(linha_int)
    return grid_int

def converter_grid_para_strings(grid_int):
    """Converte grid de inteiros para strings"""
    grid_str = []
    for linha in grid_int:
        linha_str = []
        for celula in linha:
            linha_str.append(str(celula))
        grid_str.append(linha_str)
    return grid_str

def executar_floodfill_interativo(grid_original):
    """Executa o Flood Fill de forma interativa com o usuário"""
    grid_trabalho = converter_grid_para_inteiros(grid_original)
    visualizador = VisualizadorResultado(grid_trabalho)
    
    while True:
        opcao = exibir_menu_floodfill()
        
        if opcao == '1':
            # Preencher região a partir de coordenadas específicas
            print("\n--- PREENCHIMENTO POR COORDENADAS ---")
            visualizador.imprimir_matriz_colorida(grid_trabalho, "Grid atual")
            
            coords = obter_coordenadas_iniciais(grid_original)
            if coords:
                x, y = coords
                try:
                    # Encontrar a próxima cor disponível
                    cores_utilizadas = set()
                    for linha in grid_trabalho:
                        for celula in linha:
                            if celula >= 2:
                                cores_utilizadas.add(celula)
                    
                    nova_cor = 2
                    while nova_cor in cores_utilizadas:
                        nova_cor += 1
                    
                    # Executar flood fill
                    celulas_preenchidas = flood_fill_region(grid_trabalho, (x, y), nova_cor)
                    
                    if celulas_preenchidas > 0:
                        print(f"Região preenchida com sucesso!")
                        print(f"Células preenchidas: {celulas_preenchidas}")
                        print(f"Cor utilizada: {nova_cor} ({visualizador.NOMES_CORES.get(nova_cor, f'Cor {nova_cor}')})")
                        
                        visualizador.imprimir_matriz_colorida(grid_trabalho, "Grid após preenchimento")
                        visualizador.exibir_resumo_cores(grid_trabalho)
                    else:
                        print("Nenhuma célula foi preenchida. Verifique as coordenadas.")
                        
                except Exception as e:
                    print(f"Erro durante o Flood Fill: {e}")
        
        elif opcao == '2':
            # Preencher automaticamente todas as regiões
            print("\n--- PREENCHIMENTO AUTOMÁTICO DE TODAS AS REGIÕES ---")
            visualizador.imprimir_matriz_colorida(grid_trabalho, "Grid antes do preenchimento automático")
            
            try:
                # Fazer uma cópia para não afetar o grid original durante a contagem
                grid_copia = converter_grid_para_inteiros(grid_original)
                resultado = fill_all_regions(grid_copia, start_color=2)
                
                # Agora aplicar no grid de trabalho
                resultado_real = fill_all_regions(grid_trabalho, start_color=2)
                
                print("Preenchimento automático concluído!")
                print(f"Regiões preenchidas: {resultado_real['regions_filled']}")
                print(f"Total de células coloridas: {resultado_real['cells_filled']}")
                print(f"Maior cor utilizada: {resultado_real['final_color_used']}")
                
                visualizador.imprimir_matriz_colorida(grid_trabalho, "Grid após preenchimento automático")
                visualizador.exibir_resumo_cores(grid_trabalho)
                
            except Exception as e:
                print(f"Erro durante o preenchimento automático: {e}")
        
        elif opcao == '3':
            # Voltar ao menu principal
            print("Voltando ao menu principal...")
            break
        
        else:
            print("Opção inválida! Escolha entre 1-3.")

def executar_sistema_completo():
    """Sistema principal integrado"""
    print("FLOOD FILL - SISTEMA COMPLETO DE COLORAÇÃO DE REGIÕES")
    
    def processar_grid_selecionado(grid):
        """Callback para processar o grid selecionado no menu"""
        if grid:
            print(f"\nGrid {len(grid)}x{len(grid[0])} selecionado com sucesso!")
            
            # Validar grid
            valido, mensagem = validar_grid(grid)
            if not valido:
                print(f"Grid inválido: {mensagem}")
                return
            
            # Exibir grid inicial
            visualizador_temp = VisualizadorResultado(converter_grid_para_inteiros(grid))
            visualizador_temp.imprimir_matriz_colorida(
                converter_grid_para_inteiros(grid), 
                "Grid selecionado"
            )
            
            # Calcular estatísticas
            celulas_livres = sum(1 for linha in grid for celula in linha if celula == '0')
            total_celulas = len(grid) * len(grid[0])
            percentual_livre = (celulas_livres / total_celulas) * 100
            
            print(f"Estatísticas do grid:")
            print(f"   • Células livres: {celulas_livres}/{total_celulas} ({percentual_livre:.1f}%)")
            print(f"   • Obstáculos: {total_celulas - celulas_livres} ({100 - percentual_livre:.1f}%)")
            
            # Executar sistema de Flood Fill interativo
            executar_floodfill_interativo(grid)
    
    # Executar o sistema de menu em loop
    executar_sistema_menu(callback_processar_grid=processar_grid_selecionado)

def main():
    """Função principal"""
    try:
        executar_sistema_completo()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\nEncerrando o Sistema de Flood Fill!")

if __name__ == "__main__":
    main()