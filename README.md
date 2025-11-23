# Flood Fill - Sistema de Mapeamento Inteligente para Robôs Autônomos

## Introdução

Em sistemas de automação e robótica, um robô autônomo precisa ser capaz de navegar em ambientes desconhecidos de forma segura. Para isso, ele deve identificar áreas livres, evitar obstáculos e reconhecer regiões conectadas onde pode se mover sem colisão. Em um terreno bidimensional representado por um grid, os espaços livres podem estar agrupados em diferentes áreas separadas por barreiras.

A identificação dessas regiões é fundamental para planejamento de rotas, economia de energia e tomada de decisão do robô. O algoritmo Flood Fill resolve esse problema ao percorrer automaticamente o grid, detectar áreas navegáveis conectadas e preenchê-las com valores distintos, permitindo que cada região seja visualmente reconhecida como um grupo independente.

## Descrição do Projeto

Este projeto implementa um sistema de mapeamento inteligente para robôs autônomos que precisam identificar e classificar regiões de um terreno previamente desconhecido.  
O terreno é representado como um grid bidimensional, onde cada célula pode ser um espaço livre ou um obstáculo.  
O sistema utiliza o **Algoritmo Flood Fill** para identificar e “colorir” automaticamente cada área navegável conectada, facilitando o planejamento do robô em missões contínuas ou ambientes dinâmicos.

---

## Objetivo

Implementar o algoritmo Flood Fill para:
- Identificar regiões conectadas de terreno navegável (valor 0).
- Pintar cada região com um valor de cor diferente (2, 3, 4...).
- Respeitar obstáculos (valor 1).
- Detectar automaticamente próximas regiões não mapeadas.
- Continuar até que todo o terreno navegável esteja preenchido.

---

## Descrição do Problema

O sistema recebe um grid **n × m**, onde cada célula pode ser:

| Valor | Significado |
|------|------------|
| **0** | Terreno livre (pode ser preenchido) |
| **1** | Obstáculo (não navegável) |
| **≥ 2** | Regiões coloridas |


Além disso, pode ser dada uma célula inicial (x, y) para começar o preenchimento.

---

## Funcionalidades do Algoritmo

1. Detectar células conectadas com valor 0.
2. Substituir todas essas células pela mesma cor (2, 3, 4...).
3. Detectar automaticamente próximas células livres.
4. Preencher a nova região com outra cor.
5. Repetir até não restarem valores 0 no grid.

---

## Regras

- Não atravessa obstáculos (`1`).
- Somente adjacência **ortogonal** (cima/baixo/esq/dir).
- Áreas já coloridas não são alteradas.
- O algoritmo não depende de recursão (usa BFS).

---

# Como Configurar e Executar

## Pré-requisitos
- Python 3.6+

Nenhuma biblioteca externa — apenas bibliotecas padrão.

## Instalação

```bash
git clone <url-do-repositorio>
cd FPAA-FloodFill
```

Certifique-se de que os arquivos estão no mesmo diretório:
- parte1_menu.py
- parte2_percurso.py
- parte3_visualizacao.py
- parte4_integração.py

---

## Execução

### Modo completo (recomendado)

```bash
python parte4_integração.py
```

### Testes individuais

Menu:

```bash
python parte1_menu.py
```

Somente algoritmo:

```bash
python parte2_percurso.py
```

---

# Como Usar

1. **Selecione ou gere um grid**
   - Opções 1–3 → exemplos
   - Opção 4 → manual
   - Opção 5 → aleatório

2. **Escolha como preencher**
   - Por coordenadas
   - Preencimento automático de todas as áreas

3. **Visualize**
   - Matriz numérica
   - Matriz colorida com cores ANSI

---

# Funcionamento do Flood Fill

## Visão geral
O algoritmo Flood Fill usa uma **fila BFS**, evitando recursão profunda.

### Fluxo geral

1. Começa em (x,y)
2. Marca a célula inicial com a cor
3. Visita vizinhos ortogonais
4. Preenche os vizinhos navegáveis
5. Quando acaba a região → encontra outra
6. Incrementa cor (2,3,4…) e repete

---

## Pseudocódigo (didático)

```
flood_fill(grid, x, y, color):
    fila ← [(x, y)]
    grid[x][y] ← color

    enquanto fila não vazia:
        célula ← pop(fila)
        para cada vizinho ortogonal:
            se dentro do grid E valor == 0:
                grid ← color
                push fila
```

---

# Exemplos de Entrada e Saída

## Exemplo 1

**Entrada:**

```
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
Start → (0,0)
```

**Saída:**

```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

---

## Exemplo 2

**Entrada:**
```
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
Start → (0,2)
```

**Saída:**
```
3 1 2 2 1
3 1 2 2 1
3 1 1 1 1
3 3 3 1 4
```

---

## Exemplo 3 — Múltiplas regiões maiores

```
0 0 0 1 0 0
0 1 0 0 0 1
0 1 1 1 0 0
1 0 0 0 1 0
0 0 1 0 0 0
0 1 0 0 1 0
```

Resultado esperado:

```
2 2 2 1 3 3
2 1 2 3 3 1
2 1 1 1 3 3
1 4 4 4 1 5
4 4 1 5 5 5
4 1 5 5 1 5
```

---

# Visualização Colorida (ANSI)

> A visualização colorida exibe o grid com cores no terminal para facilitar o entendimento.

Valores:

| Valor | Cor ANSI |
|------|---------|
| 0 | Branco |
| 1 | Cinza/Preto (obstáculo) |
| 2 | Vermelho |
| 3 | Laranja |
| 4 | Amarelo |
| ≥5 | Outras cores |

Exemplo simples visual:

```
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
```

Após preenchimento:

```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

---

# Estrutura do Projeto

```
FPAA-FloodFill/
│
├── parte1_menu.py               # menu e geração de grids
├── parte2_percurso.py           # algoritmo Flood Fill (BFS)
├── parte3_visualizacao.py       # impressão colorida e numérica
├── parte4_integração.py         # integração completa
└── README.md
```

---

# Funcionalidades Adicionais

### Geração automática de grids

- tamanhos: pequeno, médio, grande
- obstáculos: probabilidade customizada

### Validação

- tamanho das linhas
- valores válidos (0 ou 1)
- coordenada inicial válida

---

# Testes

1. Execute o programa
2. Selecione um grid de exemplo
3. Preencha automaticamente
4. Compare com os resultados deste README

---

# Notas Técnicas

- **Complexidade:** O(n × m)
- **Memória:** O(n × m) devido à fila BFS
- **Estabilidade:** implementação iterativa → não estoura stack

---

# Autores

- Pedro de Sousa Motta  
- Hitalo Silveira Porto  
- Leonardo Vieira Machado  
- Tiago Assunção de Sousa  

---

# Licença

Projeto acadêmico para a disciplina **FPAA — Fundamentos de Programação e Algoritmos Avançados**.

---

# Referências

- Flood Fill Algorithm
- BFS — Breadth-First Search
- Deque — Double-ended Queue
