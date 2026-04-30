"""
=============================================================================
CENTRO UNIVERSITÁRIO DE ENSINO SUPERIOR DO AMAZONAS – CIESA
CURSO DE BACHARELADO EM CIÊNCIA DA COMPUTAÇÃO
RELATÓRIO TÉCNICO – PROJETO INTEGRADOR | ÁLGEBRA LINEAR – 2026/1
=============================================================================

Projeto: Transformação Única com Reset
         Aplicação individual de transformação com opção de reinício.

Equipe:  Yara Vaz, Samia Albuquerque, David Neves, Matheus Rodrigues
Prof.:   Francisco de Assis Souza de Oliveira
Data:    14/04/2026

=============================================================================
O QUE SÃO TRANSFORMAÇÕES LINEARES?
=============================================================================

Uma transformação linear é uma operação que move, rotaciona, espelha ou
redimensiona um ponto (ou vetor) no espaço — sem quebrar a estrutura do espaço.

Na prática, trabalhamos com vetores 2D: pontos do tipo (x, y) no plano.
Uma transformação linear é representada por uma MATRIZ 2x2:

    | a  b |   | x |   =   | a*x + b*y |
    | c  d | × | y |       | c*x + d*y |

Cada tipo de transformação tem sua própria matriz. Exemplos:

  ROTAÇÃO de 90°:          ESCALA (dobrar):       REFLEXÃO no eixo X:
  |  0  -1 |               | 2  0 |               |  1   0 |
  |  1   0 |               | 0  2 |               |  0  -1 |

=============================================================================
EXEMPLOS REAIS DE USO (pra entender onde isso aparece)
=============================================================================

  🎮 JOGOS:
     Quando um personagem gira ou uma câmera rotaciona, o engine aplica
     uma matriz de rotação em todos os pontos do modelo 3D.
     Ex: girar o jogador 45° para a direita = multiplicar cada vértice
     pela matriz de rotação de 45°.

  🖼 EDITORES DE IMAGEM (Photoshop, GIMP):
     Ao espelhar ou redimensionar uma imagem, cada pixel (x, y) é
     multiplicado por uma matriz de reflexão ou escala.

  🤖 ROBÓTICA:
     Um braço robótico calcula onde mover cada junta usando matrizes de
     transformação para converter coordenadas locais em globais.

  📱 INTERFACES (CSS, Android, iOS):
     A propriedade transform: rotate(45deg) no CSS é literalmente
     uma matriz de rotação aplicada ao elemento HTML.

=============================================================================
COMO USAR ESTE PROGRAMA
=============================================================================

  1. Execute o programa: python transformacao_unica.py
  2. Digite as coordenadas do vetor inicial (ex: x=3, y=4)
  3. Escolha uma transformação:
       - Rotação: gira o vetor em torno da origem pelo ângulo escolhido
       - Escala: estica ou encolhe o vetor nos eixos x e/ou y
       - Reflexão: espelha o vetor em relação a um eixo
  4. O programa mostra a matriz usada e o cálculo passo a passo
  5. Só é possível aplicar UMA transformação por vez
  6. Use "Resetar" para voltar ao vetor original e fazer nova transformação

  Exemplo de execução:
     Vetor inicial: (3, 4)
     Rotação de 90°:
       x' = 0 × 3 + (-1) × 4 = -4
       y' = 1 × 3 +   0  × 4 =  3
     Resultado: (-4, 3)  ← o ponto girou 90° no plano!

=============================================================================
"""

import math  # Importa a biblioteca matemática para usar seno, cosseno e conversão de graus


# Classe principal que representa o objeto de transformação única com reset
class TransformacaoUnica:

    def __init__(self, vetor_inicial):
        # Construtor da classe — executado automaticamente ao criar o objeto
        # vetor_inicial é uma tupla (x, y) representando um ponto no plano 2D
        self.vetor_inicial = vetor_inicial        # Guarda o vetor original para uso no reset
        self.vetor_atual = list(vetor_inicial)    # Cópia do vetor que será transformada
        self.transformado = False                 # Controle: impede mais de uma transformação sem reset

    def aplicar_transformacao(self, matriz, nome):
        # Método que aplica uma transformação linear ao vetor atual
        # Recebe: matriz (2x2) e nome da transformação (para exibição)

        if self.transformado:
            # Bloqueia nova transformação se já houver uma aplicada — regra do "Única"
            print("\n⚠ Já foi aplicada uma transformação. Faça o reset antes de continuar.")
            return self.vetor_atual

        # Extrai as coordenadas do vetor atual
        x, y = self.vetor_atual

        # Extrai as linhas da matriz 2x2
        a, b = matriz[0]  # Primeira linha da matriz
        c, d = matriz[1]  # Segunda linha da matriz

        # Multiplicação matriz 2x2 × vetor [x, y]:
        # | a  b |   | x |   =   | a*x + b*y |
        # | c  d | × | y |       | c*x + d*y |
        novo_x = a * x + b * y  # Nova coordenada x após transformação
        novo_y = c * x + d * y  # Nova coordenada y após transformação

        # Exibe os detalhes do cálculo passo a passo
        print(f"\n--- Cálculo da Transformação: {nome} ---")
        print(f"Matriz de transformação:")
        print(f"  | {a:6.3f}  {b:6.3f} |")
        print(f"  | {c:6.3f}  {d:6.3f} |")
        print(f"\nVetor original: ({x}, {y})")
        print(f"\nCálculo:")
        print(f"  x' = {a:.3f} × {x} + {b:.3f} × {y} = {novo_x:.4f}")
        print(f"  y' = {c:.3f} × {x} + {d:.3f} × {y} = {novo_y:.4f}")

        # Atualiza o vetor atual com os valores transformados (arredondados em 4 casas)
        self.vetor_atual = [round(novo_x, 4), round(novo_y, 4)]

        # Marca que a transformação foi aplicada — bloqueia novas até o reset
        self.transformado = True

        print(f"\nVetor transformado: ({self.vetor_atual[0]}, {self.vetor_atual[1]})")
        return self.vetor_atual

    def resetar(self):
        # Restaura o vetor ao estado inicial e libera nova transformação
        self.vetor_atual = list(self.vetor_inicial)  # Volta ao vetor original
        self.transformado = False                     # Libera o bloqueio de transformação
        print(f"\nReset realizado. Vetor voltou ao estado inicial: {self.vetor_inicial}")
        return self.vetor_atual


# --- Funções que geram as matrizes de transformação ---

def matriz_rotacao(graus):
    # Gera a matriz de rotação para um ângulo dado em graus
    # Converte graus para radianos (necessário para math.sin e math.cos)
    rad = math.radians(graus)
    # Matriz de rotação padrão:
    # | cos(θ)  -sin(θ) |
    # | sin(θ)   cos(θ) |
    return [
        [math.cos(rad), -math.sin(rad)],
        [math.sin(rad),  math.cos(rad)]
    ]

def matriz_escala(sx, sy):
    # Gera a matriz de escala com fatores sx (horizontal) e sy (vertical)
    # Matriz diagonal — só afeta cada eixo individualmente:
    # | sx   0 |
    # |  0  sy |
    return [
        [sx, 0],
        [0, sy]
    ]

def matriz_reflexao(eixo):
    # Gera a matriz de reflexão de acordo com o eixo escolhido
    if eixo == "x":
        # Reflexão no eixo X: inverte apenas a coordenada y
        # | 1   0 |
        # | 0  -1 |
        return [[1, 0], [0, -1]]
    elif eixo == "y":
        # Reflexão no eixo Y: inverte apenas a coordenada x
        # | -1  0 |
        # |  0  1 |
        return [[-1, 0], [0, 1]]
    else:
        # Reflexão na origem: inverte ambas as coordenadas
        # | -1   0 |
        # |  0  -1 |
        return [[-1, 0], [0, -1]]


# --- Programa principal ---

if __name__ == "__main__":
    # Bloco principal — só executa quando o arquivo é rodado diretamente
    print("=== Transformação Única com Reset ===")
    print("Informe o vetor inicial (ponto no plano 2D):")

    # Lê as coordenadas iniciais do usuário
    x = float(input("  x: "))
    y = float(input("  y: "))

    # Cria o objeto de transformação com o vetor fornecido
    t = TransformacaoUnica((x, y))

    # Loop principal — mantém o programa rodando até o usuário sair
    while True:
        print("\n" + "="*40)
        print(f"Vetor atual: {t.vetor_atual}")
        # Informa se já existe uma transformação aplicada (exige reset antes de nova)
        print(f"Transformação aplicada: {'Sim (faça reset para nova transformação)' if t.transformado else 'Não'}")
        print("\nEscolha uma transformação:")
        print("1 - Rotação")
        print("2 - Escala")
        print("3 - Reflexão")
        print("4 - Resetar (volta ao vetor inicial)")
        print("5 - Sair")

        opcao = input("\nOpção: ")

        if opcao == "1":
            # Rotação: pede o ângulo e gera a matriz de rotação correspondente
            graus = float(input("Ângulo de rotação (em graus): "))
            matriz = matriz_rotacao(graus)
            t.aplicar_transformacao(matriz, f"Rotação de {graus}°")

        elif opcao == "2":
            # Escala: pede os fatores de escala para x e y separadamente
            sx = float(input("Fator de escala em x: "))
            sy = float(input("Fator de escala em y: "))
            matriz = matriz_escala(sx, sy)
            t.aplicar_transformacao(matriz, f"Escala ({sx}, {sy})")

        elif opcao == "3":
            # Reflexão: pede o eixo (x, y ou origem)
            print("Reflexão em qual eixo?")
            print("  x - Reflexão no eixo X")
            print("  y - Reflexão no eixo Y")
            print("  o - Reflexão na origem")
            eixo = input("Eixo: ").lower()
            if eixo in ["x", "y", "o"]:
                matriz = matriz_reflexao(eixo)
                t.aplicar_transformacao(matriz, f"Reflexão no eixo {eixo.upper()}")
            else:
                print("Eixo inválido.")

        elif opcao == "4":
            # Reset: restaura o vetor inicial e libera nova transformação
            t.resetar()

        elif opcao == "5":
            # Encerra o programa normalmente
            print("Encerrando...")
            break

        else:
            # Entrada inválida — solicita nova opção
            print("Opção inválida.")
