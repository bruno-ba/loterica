from models import Concurso
from datetime import datetime as dt

if __name__ == '__main__':
    c = Concurso('lotofacil', 25, 15, 11)

    dt_in = dt(2020, 1, 1)
    dt_out = dt(2020, 4, 18)

    lst_sorteios_props = ['numero',
                          'data',
                          'bolas_sorteadas_zero_fill'
                          ]

    c.criar_relatorio('relatorio-inicial_2020',
                      lst_sorteios_props,
                      Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))

    lst_sorteios_par_impar = ['numero',
                              'data',
                              'bolas_sorteadas_pares_zero_fill',
                              'bolas_sorteadas_pares_len',
                              'bolas_sorteadas_pares_sum',
                              'bolas_sorteadas_pares_avg',
                              'bolas_sorteadas_impares_zero_fill',
                              'bolas_sorteadas_impares_len',
                              'bolas_sorteadas_impares_sum',
                              'bolas_sorteadas_impares_avg',
                              ]

    c.criar_relatorio('relatorio-inicial_pares_impares_2020',
                      lst_sorteios_par_impar,
                      Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))