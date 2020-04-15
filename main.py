from models import Concurso

if __name__ == '__main__':
  c = Concurso('lotofacil', 25, 15, 11)
  c.criar_relatorio('relatorio-inicial', ['numero', 'data', 'bolas_sorteadas', 'bolas_sorteadas_zero_fill'])
  c.criar_relatorio('relatorio-pares', ['numero', 'data',
                                        'bolas_sorteadas_pares_zero_fill',
                                        'bolas_sorteadas_pares_len',
                                        'bolas_sorteadas_pares_sum',
                                        'bolas_sorteadas_pares_avg',
                                        'bolas_sorteadas_impares_zero_fill',
                                        'bolas_sorteadas_impares_len',
                                        'bolas_sorteadas_impares_sum',
                                        'bolas_sorteadas_impares_avg',
                                        ])

