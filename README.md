# Flood Fill - Sistema de Mapeamento Inteligente para Robôs Autônomos

## Introdução

Em sistemas de automação e robótica, um robô autônomo precisa ser capaz de navegar em ambientes desconhecidos de forma segura. Para isso, ele deve identificar áreas livres, evitar obstáculos e reconhecer regiões conectadas onde pode se mover sem colisão. Em um terreno bidimensional representado por um grid, os espaços livres podem estar agrupados em diferentes áreas separadas por barreiras.

A identificação dessas regiões é fundamental para planejamento de rotas, economia de energia e tomada de decisão do robô. O algoritmo Flood Fill resolve esse problema ao percorrer automaticamente o grid, detectar áreas navegáveis conectadas e preenchê-las com valores distintos, permitindo que cada região seja visualmente reconhecida como um grupo independente.

## Descrição do Projeto

Este projeto implementa um sistema de mapeamento inteligente para robôs autônomos que precisam identificar e classificar regiões de um terreno previamente desconhecido. O terreno é representado como um grid bidimensional, onde cada célula pode ser um espaço livre ou um obstáculo. O sistema utiliza o **Algoritmo Flood Fill** para identificar e "colorir" automaticamente cada área navegável conectada, facilitando o planejamento do robô em missões contínuas ou ambientes dinâmicos.

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

## Funcionamento detalhado do Flood Fill

Imagine que você está explorando um mapa quadriculado, onde alguns quadrados estão livres para caminhar e outros são paredes intransponíveis. O algoritmo Flood Fill funciona como um explorador sistemático que vai marcando todas as áreas conectadas com a mesma cor, uma região de cada vez.

1. **Preparação do terreno**: O algoritmo recebe um grid onde cada célula pode ser um espaço navegável (representado pelo valor 0) ou um obstáculo (representado pelo valor 1). Esses obstáculos são como paredes que não podem ser atravessadas.

2. **Escolha do ponto de partida**: O processo começa quando você fornece uma coordenada inicial (x, y) no grid. Essa célula deve ser um espaço navegável, ou seja, deve conter o valor 0. Se for um obstáculo, o algoritmo não pode começar ali.

3. **Atribuição da primeira cor**: A primeira região descoberta será marcada com o valor 2. Pense nisso como pintar essa área inteira com a cor vermelha. As próximas regiões receberão os valores 3, 4, 5 e assim por diante, cada uma com sua própria "cor" numérica.

4. **Criação da lista de trabalho**: A célula inicial é colocada em uma lista especial que funciona como uma fila de espera. Essa lista guarda todas as células que precisam ser processadas. É como fazer uma lista de lugares que você ainda precisa visitar.

5. **Processamento da fila**: O algoritmo pega a primeira célula da lista e começa a trabalhar nela. Ele verifica os quatro vizinhos diretos dessa célula: acima, abaixo, à esquerda e à direita. Esses são os únicos vizinhos considerados, não as diagonais.

6. **Verificação de células navegáveis**: Para cada vizinho encontrado, o algoritmo verifica duas coisas importantes: primeiro, se a célula está dentro dos limites do grid (não está fora das bordas), e segundo, se ela contém o valor 0, indicando que é um espaço livre e navegável.

7. **Preenchimento e expansão**: Quando encontra uma célula vizinha que é navegável (valor 0), o algoritmo faz duas coisas: marca essa célula com a cor atual (por exemplo, 2) e adiciona ela na lista de trabalho para que seus próprios vizinhos sejam verificados depois. É como se você estivesse pintando um cômodo e, ao pintar uma parede, descobrisse que há uma porta para outro cômodo conectado.

8. **Continuação do preenchimento**: O processo continua pegando células da lista, verificando seus vizinhos, preenchendo as navegáveis e adicionando-as à lista. Isso se repete até que a lista fique vazia, o que significa que toda a região conectada foi descoberta e pintada com a mesma cor.

9. **Busca automática por novas regiões**: Após terminar de preencher uma região completa, o algoritmo não para. Ele percorre o grid linha por linha, da esquerda para a direita, procurando a primeira célula que ainda contém o valor 0. Quando encontra, sabe que há uma nova região desconectada esperando para ser explorada.

10. **Incremento da cor e repetição**: Ao encontrar uma nova região, o algoritmo incrementa o valor da cor. Se a primeira região foi marcada com 2, a próxima será marcada com 3, depois 4, 5 e assim por diante. O processo de preenchimento se repete para essa nova região, começando do passo 4.

11. **Finalização**: O algoritmo continua esse ciclo de encontrar regiões, preenchê-las e procurar a próxima, até que não existam mais células com valor 0 no grid. Quando isso acontece, significa que todas as áreas navegáveis foram identificadas e cada região desconectada recebeu sua própria cor única.

12. **Resultado final**: Ao final do processo, o grid estará completamente mapeado. Cada região navegável terá sua própria cor numérica, os obstáculos permanecerão inalterados (valor 1), e você poderá visualizar claramente quantas áreas distintas existem e quais células pertencem a cada região.

A segmentação do terreno em regiões distintas é extremamente útil para o planejamento de rotas do robô. Com cada área claramente identificada, o sistema pode calcular caminhos dentro de uma mesma região, decidir qual região explorar primeiro, e até mesmo determinar se é possível chegar de um ponto a outro (se ambos estão na mesma região colorida). Isso torna a navegação mais eficiente e segura, permitindo que o robô tome decisões inteligentes sobre onde e como se mover no ambiente.

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

**Entrada:**

```
0 0 0 1 0 0
0 1 0 0 0 1
0 1 1 1 0 0
1 0 0 0 1 0
0 0 1 0 0 0
0 1 0 0 1 0
```

**Resultado esperado:**

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

## Geração automática de grids

- tamanhos: pequeno, médio, grande
- obstáculos: probabilidade customizada

## Validação

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
