class VisualizadorResultado:
    def __init__(self, labirinto):
        self.labirinto = [linha[:] for linha in labirinto]

    def marcar_caminho(self, caminho):
        """Marca o caminho no labirinto com '*'"""
        if not caminho:
            return
        
        for (i, j) in caminho:
            if self.labirinto[i][j] not in ('S', 'E'):
                self.labirinto[i][j] = '*'

    def imprimir_labirinto(self):
        """Exibe o labirinto no terminal"""
        print("\n🧩 Labirinto com caminho encontrado:\n")
        for linha in self.labirinto:
            print(' '.join(linha))
        print()

    def exibir_caminho(self, caminho):
        """Mostra as coordenadas do caminho formatadas"""
        if not caminho:
            print("❌ Nenhum caminho encontrado.")
            return
        print("📍 Caminho (lista de coordenadas):")
        formatado = " → ".join([f"({i},{j})" for (i, j) in caminho])
        print(formatado)
        print()

    def exibir_resultado_completo(self, caminho, erro=None):
        """Mostra resultado final da execução"""
        if erro:
            print(f"\n❌ Erro: {erro}")
            return

        if not caminho:
            print("\n⚠️ Nenhum caminho possível entre S e E.\n")
            self.imprimir_labirinto()
            return

        self.marcar_caminho(caminho)
        self.imprimir_labirinto()
        self.exibir_caminho(caminho)
        print("✅ Caminho exibido com sucesso!\n")
