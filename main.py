from models import Concurso
from datetime import datetime as dt


def rel_sorteadas(concurso: Concurso, nome: str, filter_exp=None):

    lst_sorteios_props = [
        'numero',
        'data',
        'sorteadas',
        'sorteadas_len',
        'sorteadas_sum',
        'sorteadas_avg',
    ]
    concurso.criar_relatorio(
        nome,
        lst_sorteios_props,
        filter_exp
    )


def rel_sorteadas_pares(concurso: Concurso, nome: str, filter_exp=None):

    lst_sorteios_props = [
        'numero',
        'data',
        'sorteadas_pares',
        'sorteadas_pares_len',
        'sorteadas_pares_sum',
        'sorteadas_pares_avg',
    ]
    concurso.criar_relatorio(
        nome,
        lst_sorteios_props,
        filter_exp
    )


def rel_sorteadas_impares(concurso: Concurso, nome: str, filter_exp=None):

    lst_sorteios_props = [
        'numero',
        'data',
        'sorteadas_impares',
        'sorteadas_impares_len',
        'sorteadas_impares_sum',
        'sorteadas_impares_avg',
    ]
    concurso.criar_relatorio(
        nome,
        lst_sorteios_props,
        filter_exp
    )


def rel_nao_sorteadas(concurso: Concurso, nome: str, filter_exp=None):

    lst_sorteios_props = [
        'numero',
        'data',
        'nao_sorteadas',
        'nao_sorteadas_len',
        'nao_sorteadas_sum',
        'nao_sorteadas_avg',
    ]
    concurso.criar_relatorio(
        nome,
        lst_sorteios_props,
        filter_exp
    )


def rel_nao_sorteadas_pares(concurso: Concurso, nome: str, filter_exp=None):

    lst_sorteios_props = [
        'numero',
        'data',
        'nao_sorteadas_pares',
        'nao_sorteadas_pares_len',
        'nao_sorteadas_pares_sum',
        'nao_sorteadas_pares_avg',
    ]
    concurso.criar_relatorio(
        nome,
        lst_sorteios_props,
        filter_exp
    )


def rel_nao_sorteadas_impares(concurso: Concurso, nome: str, filter_exp=None):

    lst_sorteios_props = [
        'numero',
        'data',
        'nao_sorteadas_impares',
        'nao_sorteadas_impares_len',
        'nao_sorteadas_impares_sum',
        'nao_sorteadas_impares_avg',
    ]
    concurso.criar_relatorio(
        nome,
        lst_sorteios_props,
        filter_exp
    )


if __name__ == '__main__':

    c = Concurso('lotofacil', 25, 15, 11)

    dt_in = dt(2020, 1, 1)
    dt_out = dt.now()

    rel_sorteadas(c, 'rel sorteadas')
    rel_sorteadas(c, 'rel 2020 sorteadas', Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))
    rel_sorteadas_pares(c, 'rel sorteadas-pares')
    rel_sorteadas_pares(c, 'rel 2020 sorteadas-pares', Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))
    rel_sorteadas_impares(c, 'rel sorteadas-impares')
    rel_sorteadas_impares(c, 'rel 2020 sorteadas-impares', Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))
    rel_nao_sorteadas(c, 'rel nao-sorteadas')
    rel_nao_sorteadas(c, 'rel 2020 nao-sorteadas', Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))
    rel_nao_sorteadas_pares(c, 'rel nao-sorteadas-pares')
    rel_nao_sorteadas_pares(c, 'rel 2020 nao-sorteadas-pares', Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))
    rel_nao_sorteadas_impares(c, 'rel nao-sorteadas-impares')
    rel_nao_sorteadas_impares(c, 'rel 2020 nao-sorteadas-impares', Concurso.exp_filter_sorteio_by_dates(dt_in, dt_out))

