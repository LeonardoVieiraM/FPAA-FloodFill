import heapq
from typing import List, Tuple, Optional


class PathFinder:
    """Implementa o algoritmo A* para encontrar caminho entre 'S' e 'E'.

    Contrato:
    - __init__(labirinto: List[List[str]])
    - executar_a_estrela() -> (caminho: List[Tuple[int,int]] | None, erro: Optional[str])

    Retornos:
    - (caminho, None) quando caminho encontrado (inclui S e E)
    - ([], None) quando nenhum caminho possível
    - (None, mensagem) quando entrada inválida
    """

    def __init__(self, labirinto: List[List[str]]):
        self.lab = labirinto
        self.n = len(labirinto)
        self.m = len(labirinto[0]) if self.n > 0 else 0

    def executar_a_estrela(self) -> Tuple[Optional[List[Tuple[int, int]]], Optional[str]]:
        # checagens básicas
        if not self.lab or self.n == 0 or self.m == 0:
            return None, "Labirinto inválido ou vazio"

        start = None
        goal = None
        for i in range(self.n):
            for j in range(self.m):
                if self.lab[i][j] == 'S':
                    start = (i, j)
                elif self.lab[i][j] == 'E':
                    goal = (i, j)

        if start is None:
            return None, "Ponto inicial 'S' não encontrado"
        if goal is None:
            return None, "Ponto final 'E' não encontrado"

        def h(a: Tuple[int, int], b: Tuple[int, int]) -> int:
            # heurística Manhattan
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        open_set = []  # heap of (f_score, g_score, node, parent)
        heapq.heappush(open_set, (h(start, goal), 0, start, None))

        came_from = {}  # node -> parent
        g_score = {start: 0}
        closed = set()

        while open_set:
            f, g, current, parent = heapq.heappop(open_set)

            if current in closed:
                continue

            came_from[current] = parent

            if current == goal:
                # reconstruir caminho
                path = []
                node = current
                while node is not None:
                    path.append(node)
                    node = came_from.get(node)
                path.reverse()
                return path, None

            closed.add(current)

            for dx, dy in neighbors:
                ni, nj = current[0] + dx, current[1] + dy
                if not (0 <= ni < self.n and 0 <= nj < self.m):
                    continue
                cell = self.lab[ni][nj]
                if cell == '1':
                    continue  # obstáculo

                neighbor = (ni, nj)
                tentative_g = g + 1

                if neighbor in g_score and tentative_g >= g_score[neighbor]:
                    continue

                g_score[neighbor] = tentative_g
                f_score = tentative_g + h(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, current))

        # sem caminho
        return [], None


if __name__ == '__main__':
    # teste rápido
    lab = [
        ['S', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]
    pf = PathFinder(lab)
    caminho, erro = pf.executar_a_estrela()
    print('caminho:', caminho)
    print('erro:', erro)
