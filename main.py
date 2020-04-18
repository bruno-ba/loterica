from models import Concurso
from datetime import datetime as dt

if __name__ == '__main__':
    c = Concurso('lotofacil', 25, 15, 11)

    dt_in = dt(2020, 1, 1)
    dt_out = dt(2020, 4, 18)

    lst_sorteios_props = ['numero',
                          'data',
                          'bolas_sorteadas_zero_fill']

    c.criar_relatorio('relatorio-inicial_2020',
                      lst_sorteios_props,
                      Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))
