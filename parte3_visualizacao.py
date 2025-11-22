

import copy

NOMES_CORES = {
    0: "Branco (livre)",
    1: "Preto (obstáculo)",
    2: "Vermelho",
    3: "Laranja",
    4: "Amarelo",
}

ANSI_CORES = {
    0: "\033[97m",   # branco
    1: "\033[90m",   # cinza escuro
    2: "\033[91m",   # vermelho
    3: "\033[93m",   # amarelo
    4: "\033[93m",   # amarelo também
}
ANSI_FIM = "\033[0m"


class VisualizadorResultado:

    def __init__(self, grid_inicial):
        self.grid_inicial = copy.deepcopy(grid_inicial)

    def imprimir_matriz(self, grid, titulo=None):
        if titulo:
            print(f"\n=== {titulo} ===")
        for linha in grid:
            print(" ".join(str(c) for c in linha))
        print()

    def imprimir_matriz_colorida(self, grid, titulo=None):
        if titulo:
            print(f"\n=== {titulo} (versão colorida) ===")
        for linha in grid:
            linha_formatada = []
            for celula in linha:
                valor = int(celula)
                cor = ANSI_CORES.get(valor, "\033[0m")
                linha_formatada.append(f"{cor}{valor}{ANSI_FIM}")
            print(" ".join(linha_formatada))
        print()

    def exibir_resumo_cores(self, grid):
        usados = set()
        for linha in grid:
            for celula in linha:
                usados.add(int(celula))
        print("Cores usadas no grid:")
        for v in sorted(usados):
            nome = NOMES_CORES.get(v, f"Cor {v}")
            print(f"  {v} -> {nome}")
        print()

    def exibir_resultado_completo(self, grid_preenchido, erro=None):
        if erro:
            print(f"\n❌ Erro na execução do Flood Fill: {erro}")
            return

        print("\n🧩 Resultado do Flood Fill")

        self.imprimir_matriz(self.grid_inicial, "Grid inicial")
        self.imprimir_matriz(grid_preenchido, "Grid após preenchimento")

        self.imprimir_matriz_colorida(self.grid_inicial, "Grid inicial")
        self.imprimir_matriz_colorida(grid_preenchido, "Grid após preenchimento")

        self.exibir_resumo_cores(grid_preenchido)

        print("✅ Visualização concluída.\n")
