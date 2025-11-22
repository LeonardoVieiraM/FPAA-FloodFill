"""
FloodFill - Algoritmo para identificar e colorir regiões conectadas em um grid 2D.

Regras e convenções:
- Grid: lista de listas de inteiros.
  - 0: terreno navegável (a ser preenchido)
  - 1: obstáculo (não navegável)
  - 2, 3, 4, ...: cores já preenchidas (devem ser preservadas)
- Coordenadas: (row, col) 0-indexadas.
- Preenchimento é ortogonal (cima, baixo, esquerda, direita).
- As funções modificam o grid in-place e também retornam o grid para conveniência.

Funções principais:
- flood_fill_region(grid, start, color) -> int
    Preenche a região conectada ao ponto start com o valor color.
    Retorna o número de células preenchidas (0 se start inválido ou não navegável).

- fill_all_regions(grid, start=None, start_color=2) -> dict
    Preenche todas as regiões navegáveis do grid começando pela célula start (se fornecida)
    ou pela primeira célula 0 encontrada. Cada região recebe uma cor incrementada
    sequencialmente a partir de start_color.
    Retorna um dicionário com metadados: {
        "regions_filled": int,
        "final_color_used": int,  # a última cor usada (ou start_color-1 se nada preenchido)
        "cells_filled": int       # total de células preenchidas
    }

Exemplo de uso:
    grid = [
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
    ]
    meta = fill_all_regions(grid)
    print(grid)
    print(meta)

from collections import deque
from typing import List, Tuple, Optional, Dict

Grid = List[List[int]]
Point = Tuple[int, int]


def in_bounds(grid: Grid, r: int, c: int) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def flood_fill_region(grid: Grid, start: Point, color: int) -> int:
    """
    Preenche a região conectada ortogonalmente ao ponto start com o valor 'color'.

    Parâmetros:
    - grid: matriz de inteiros (modificada in-place)
    - start: tupla (row, col) 0-indexada
    - color: inteiro >= 2 indicando a cor a aplicar

    Retorna:
    - número de células preenchidas (0 se start inválido ou não navegável)
    """
    if color <= 1:
        raise ValueError("color deve ser >= 2")
    if not grid:
        return 0
    r0, c0 = start
    if not in_bounds(grid, r0, c0):
        return 0
    if grid[r0][c0] != 0:
        # Não é ponto navegável (pode ser obstáculo ou já colorido)
        return 0

    rows, cols = len(grid), len(grid[0])
    q = deque()
    q.append((r0, c0))
    filled = 0
    # Marcar imediatamente para evitar múltiplas inserções na fila
    grid[r0][c0] = color
    filled += 1

    while q:
        r, c = q.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                grid[nr][nc] = color
                filled += 1
                q.append((nr, nc))
    return filled


def find_next_zero(grid: Grid, start_scan: Optional[Point] = None) -> Optional[Point]:
    """
    Encontra a próxima célula com valor 0 no grid, fazendo busca linear por linhas.
    Se start_scan for fornecido, a busca começa a partir dessa posição (inclusive).
    Retorna (row, col) ou None se não houver zeros.
    """
    if not grid:
        return None
    rows, cols = len(grid), len(grid[0])
    start_r, start_c = (0, 0) if start_scan is None else start_scan
    # Normaliza se coordenadas fora do intervalo
    if start_r < 0:
        start_r = 0
    if start_c < 0:
        start_c = 0
    for r in range(start_r, rows):
        c0 = start_c if r == start_r else 0
        for c in range(c0, cols):
            if grid[r][c] == 0:
                return (r, c)
    return None


def fill_all_regions(grid: Grid, start: Optional[Point] = None, start_color: int = 2) -> Dict[str, int]:
    """
    Localiza e preenche todas as regiões navegáveis (0) do grid, começando
    pela célula 'start' se fornecida. Cada região recebe uma cor
    incremental (start_color, start_color+1, ...).

    Retorna um dict com:
      - regions_filled: número de regiões preenchidas
      - final_color_used: último valor de cor aplicado (ou start_color-1 se nada preenchido)
      - cells_filled: total de células preenchidas
    """
    if start_color <= 1:
        raise ValueError("start_color deve ser >= 2")

    color = start_color
    regions = 0
    total_cells = 0

    # Se start fornecido e for navegável, comece por ele; caso contrário, ignore e procure
    if start is not None:
        if in_bounds(grid, start[0], start[1]) and grid[start[0]][start[1]] == 0:
            filled = flood_fill_region(grid, start, color)
            if filled > 0:
                regions += 1
                total_cells += filled
                color += 1

    # Preencha o restante das regiões encontrando zeros
    next_zero = find_next_zero(grid)
    while next_zero is not None:
        filled = flood_fill_region(grid, next_zero, color)
        if filled > 0:
            regions += 1
            total_cells += filled
            color += 1
        next_zero = find_next_zero(grid)

    final_color_used = color - 1
    return {
        "regions_filled": regions,
        "final_color_used": final_color_used,
        "cells_filled": total_cells
    }


if __name__ == "__main__":
    # Exemplo rápido de uso e demonstração
    example_grid = [
        [0, 0, 1, 0, 2],
        [0, 1, 1, 0, 2],
        [0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0],
    ]
    print("Grid inicial:")
    for row in example_grid:
        print(row)

    meta = fill_all_regions(example_grid, start=(0, 0), start_color=2)
    print("\nGrid depois do preenchimento:")
    for row in example_grid:
        print(row)

    print("\nMetadados:", meta)
