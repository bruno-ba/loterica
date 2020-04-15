# loterica
 Projeto para analisar resultados de loterias, gerar relatórios e ajudar a escolher número baseados em alguns critérios.

"""
      class Concurso

      Responsável por receber por criar os tipos de concursos - simples apenas com bolas sorteadas, o que é a
      maioria das loterias, sendo possível aplicar na maioria delas. A exemplo de loterias com alguns critérios
      diferentes, como o dia da sorte, teria que especializar esta classe.

      Esta classe:
      bolas total no concurso -> qtd_bolas ex: lotofácil - 25
      bolas total que são sorteadas -> qtd_bolas  ex: lotofácil - 15
      bolas listagem da quantidade mínima de acertos - para posterior conferência-> qtd_min_acertos  ex: lotofácil ganha
      com 11, 12, 13, 14, 15 acertos

      Os resultados dos ainda são pré-carregados manualmente.
      a referência atual é o site: www.asloterias.com.br

      Cada concurso criado irá gerar um diretório-path relativo, como o nome do concurso e um arquivo csv:
      resultados_nomedoconcurso.csv, que deverá ser substituido manualmente
      """


 """
    dataclass Sorteio

    Responsável por receber as bolas sorteadas, e fazer a identificaçã:

    bolas sorteadas:
            quantidade de bolas sorteadas pares -> len
            soma das bolas sorteadas pares -> sum
            média das bolas sorteadas pares -> sum / len

            quantidade de bolas sorteadas impares -> len
            soma das bolas sorteadas impares -> sum
            média das bolas sorteadas impares -> sum / len

    bolas não sorteadas:
            quantidade de bolas não sorteadas pares -> len
            soma das bolas não sorteadas pares -> sum
            média das bolas não sorteadas pares -> sum / len

            quantidade de bolas não sorteadas impares -> len
            soma das bolas não sorteadas impares -> sum
            média das bolas não sorteadas impares -> sum / len

    propriedades zero_fill:
    são responsáveis por preencher com zeros '.' qualquer número ausente, permitindo assim, manter um tamanho fixo de
    colunas na hora de gerar os csv.

    """
