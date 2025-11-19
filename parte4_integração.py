from parte1_menu import executar_sistema_menu, validar_labirinto
from parte2_percurso import PathFinder
from parte3_visualizacao import VisualizadorResultado

def executar_pathfinder_completo():
    print("🚀 INICIANDO PATHFINDER - RESOLVEDOR DE LABIRINTOS A*")
    
    # Parte 1: Menu e seleção do labirinto
    labirinto = executar_sistema_menu()
    
    if not labirinto:
        print("Programa encerrado.")
        return
    
    valido, mensagem = validar_labirinto(labirinto)
    if not valido:
        print(f"Erro: {mensagem}")
        return
    
    # Parte 2: Executar algoritmo A*
    print("\n🔍 Executando algoritmo A*...")
    finder = PathFinder(labirinto)
    caminho, erro = finder.executar_a_estrela()
    
    # Parte 3: Exibir resultados
    visualizador = VisualizadorResultado(labirinto)
    visualizador.exibir_resultado_completo(caminho, erro)

def main():
    try:
        executar_pathfinder_completo()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")
    finally:
        print("\nEncerrando o PathFinder!")

if __name__ == "__main__":
    main()