# Transformação Única com Reset

Aplicação individual de transformação linear com opção de reinício, desenvolvida em Python como projeto integrador da disciplina de Álgebra Linear.

---

## Tecnologias utilizadas

- Python 3.x
- Biblioteca `math` (nativa do Python)
- Overleaf (documentação acadêmica)
- HTML, CSS e JavaScript (frontend visual — bônus)

---

## Como rodar o projeto

Clone o repositório:

```bash
git clone https://github.com/nevext/tranform-reset-python.git
```

Rode o programa:

```bash
python transformacao_unica.py
```

Nenhuma instalação de dependências necessária — o projeto usa apenas a biblioteca padrão do Python.

---

## Estrutura do projeto

```
tranform-reset-python/
├── code/
│   └── transformacao_unica.py   → código principal com a lógica e as transformações
├── doc/
│   └── frontend/
│       ├── index.html           → interface visual do projeto
│       ├── style.css            → estilização
│       └── script.js            → lógica de integração visual
└── README.md                    → documentação
```

---

## O que o programa faz

O projeto aplica **transformações lineares** em um vetor 2D (ponto no plano) usando multiplicação de matriz 2×2. A regra principal é: só é permitida **uma transformação por vez** — após aplicar, o usuário deve resetar para fazer outra.

### Transformações disponíveis

| Transformação | O que faz | Matriz usada |
|---|---|---|
| Rotação | Gira o vetor em torno da origem | `[[cos θ, -sin θ], [sin θ, cos θ]]` |
| Escala | Estica ou encolhe o vetor | `[[sx, 0], [0, sy]]` |
| Reflexão X | Espelha em relação ao eixo X | `[[1, 0], [0, -1]]` |
| Reflexão Y | Espelha em relação ao eixo Y | `[[-1, 0], [0, 1]]` |
| Reflexão Origem | Espelha em relação à origem | `[[-1, 0], [0, -1]]` |

### Versão final esperada

- Usuário informa um vetor inicial `(x, y)`
- Escolhe uma das três transformações (rotação, escala ou reflexão)
- O programa exibe a matriz usada e o cálculo passo a passo:
  - `x' = a×x + b×y`
  - `y' = c×x + d×y`
- Após aplicar, novas transformações ficam bloqueadas até o reset
- O reset restaura o vetor ao estado original
- O frontend visual exibe o vetor antes (azul) e depois (verde) no plano cartesiano

---

## Onde isso é usado no mundo real

- **Jogos**: motores de jogo aplicam matrizes de rotação em cada vértice de um modelo 3D para girar personagens e câmeras
- **Editores de imagem** (Photoshop, GIMP): espelhar ou redimensionar uma imagem aplica uma matriz de reflexão ou escala em cada pixel
- **Robótica**: braços robóticos usam matrizes de transformação para converter coordenadas locais em globais
- **Interfaces** (CSS, Android, iOS): `transform: rotate(45deg)` no CSS é literalmente uma matriz de rotação aplicada ao elemento

---

## Divisão de tarefas

Todos os integrantes são responsáveis por:
- Entender e saber explicar o código completo
- Saber executar o programa localmente
- Dominar a teoria por trás das transformações lineares
- Saber onde e como esse conceito é aplicado no mundo real

| Integrante | Responsabilidade principal |
|---|---|
| David Neves | Estrutura do repositório, código principal, frontend (bônus) e README |
| Samia Albuquerque | Estrutura inicial do código, lógica da classe `TransformacaoUnica` |
| Yara da Silva Vaz | Documentação no Overleaf e apoio na implementação das transformações |

> O frontend em HTML/CSS/JS é um bônus visual — não faz parte da entrega obrigatória, mas demonstra as transformações de forma interativa no navegador.

---

## Integrantes

- David Neves
- Samia Albuquerque
- Yara da Silva Vaz

**Professor:** Francisco de Assis Souza de Oliveira  
**Disciplina:** Álgebra Linear — CIESA 2026/1