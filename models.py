import os
import csv
from dataclasses import dataclass, field, InitVar

from datetime import datetime


@dataclass
class Sorteio:
    """
    dataclass Sorteio

    Responsável por receber as bolas sorteadas, e fazer a identificação:

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

    """
    numero: int
    data: datetime
    bolas: tuple
    def sorteadas(self) -> tuple: return tuple(k if v else '.' for k, v in self.bolas)
    def sorteadas_len(self) -> int: return len([v for k, v in self.bolas if v])
    def sorteadas_sum(self) -> int: return sum(k for k, v in self.bolas if v)
    def sorteadas_avg(self) -> float: return self.sorteadas_sum() / self.sorteadas_len()
    def sorteadas_pares(self) -> tuple: return tuple(k if v else '.' for k, v in self.bolas if k % 2 == 0)
    def sorteadas_pares_len(self) -> int: return len([v for k, v in self.bolas if v if k % 2 == 0])
    def sorteadas_pares_sum(self) -> int: return sum(k for k, v in self.bolas if v if k % 2 == 0)
    def sorteadas_pares_avg(self) -> float: return self.sorteadas_pares_sum() / self.sorteadas_pares_len()
    def sorteadas_impares(self) -> tuple: return tuple(k if v else '.' for k, v in self.bolas if k % 2 != 0)
    def sorteadas_impares_len(self) -> int: return len([v for k, v in self.bolas if v if k % 2 != 0])
    def sorteadas_impares_sum(self) -> int: return sum(k for k, v in self.bolas if v if k % 2 != 0)
    def sorteadas_impares_avg(self) -> float: return self.sorteadas_impares_sum() / self.sorteadas_impares_len()
    def nao_sorteadas(self) -> tuple: return tuple(k if not v else '.' for k, v in self.bolas)
    def nao_sorteadas_len(self) -> int: return len([v for k, v in self.bolas if not v])
    def nao_sorteadas_sum(self) -> int: return sum(k for k, v in self.bolas if not v)
    def nao_sorteadas_avg(self) -> float: return self.nao_sorteadas_sum() / self.nao_sorteadas_len()
    def nao_sorteadas_pares(self) -> tuple: return tuple(k if not v else '.' for k, v in self.bolas if k % 2 == 0)
    def nao_sorteadas_pares_len(self) -> int: return len([v for k, v in self.bolas if not v if k % 2 == 0])
    def nao_sorteadas_pares_sum(self) -> int: return sum(k for k, v in self.bolas if not v if k % 2 == 0)
    def nao_sorteadas_pares_avg(self) -> float: return self.nao_sorteadas_pares_sum() / self.nao_sorteadas_pares_len()
    def nao_sorteadas_impares(self) -> tuple: return tuple(k if not v else '.' for k, v in self.bolas if k % 2 != 0)
    def nao_sorteadas_impares_len(self) -> int: return len([v for k, v in self.bolas if not v if k % 2 != 0])
    def nao_sorteadas_impares_sum(self) -> int: return sum(k for k, v in self.bolas if not v if k % 2 != 0)
    def nao_sorteadas_impares_avg(self) -> float: return self.nao_sorteadas_impares_sum() / self.nao_sorteadas_impares_len()


class Concurso:
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

    @staticmethod
    def exp_filter_sorteio_by_dates(dt_in: datetime, dt_out: datetime):
        return lambda s: dt_in <= s.data < dt_out

    def _create_init_file(self) -> tuple:
        """
        método interno para verificar ou criar os diretórios e arquivos resultados csv.

        """
        pth_folder = os.path.join('.\\', self.nome)
        file_nome = 'resultados' + '_' + self.nome + '.csv'
        pth_file = os.path.join(pth_folder, file_nome)

        if os.path.exists(pth_file):
            print(f'\nok -> file: {os.path.basename(pth_file)}, found.')

        else:
            os.makedirs(pth_folder)
            file = open(pth_file, mode='w', encoding='utf-8', newline='')
            file.close()
            print(f'\nok -> file: {os.path.basename(pth_file)}, created.')

        return pth_folder, pth_file

    def _load_sorteios(self) -> list:
        """
        Carrega os sorteios, fazendo a limpeza das linhas iniciais não relevantes.
        """
        rows = []
        sorteios = []

        if os.path.exists(self._pth_file):
            with open(self._pth_file, encoding='utf-8', mode='r', newline='') as csv_file:
                csv_len = self._qtd_sorteadas + 2
                csv_rd = csv.reader(csv_file)
                csv_rd = (list(filter(None, x)) for x in csv_rd)  # limpa os campos vazios
                csv_rd = (x for x in csv_rd if len(x) == csv_len)  # colunas válidas -> num + dt + qtd_sorteadas
                header = next(csv_rd, 'empty')  # clear header

                if header == 'empty':
                    print(f'warning <- file: {os.path.basename(self._pth_file)}, empty.')

                else:
                    print(f'ok -> file: {os.path.basename(self._pth_file)}, filled.')
                    for r in csv_rd:
                        rows.append(r)

            if 0 < len(rows):
                range_balls = range(1, self._qtd_bolas + 1)

                for r in rows:
                    draw_balls = tuple(int(b) for b in r[2:])
                    sorteio_num = int(r[0])
                    sorteio_dt = datetime.strptime(r[1], '%d/%m/%Y')
                    sorteio_balls_hit = tuple((ball, True)
                                              if ball in draw_balls
                                              else (ball, False) for ball in range_balls)
                    sorteios.append(Sorteio(sorteio_num, sorteio_dt, sorteio_balls_hit))
                    sorteios.sort(key=lambda x: x.numero)

        return sorteios

    def __init__(self, nome: str, qtd_bolas: int, qtd_sorteadas: int, qtd_min_acertos: tuple):
        self._nome = ''
        self._qtd_bolas = 0
        self._qtd_sorteadas = 0
        self._qtd_min_acertos = 0
        self._sorteios = None

        self.nome = nome
        self.qtd_bolas = qtd_bolas
        self.qtd_sorteadas = qtd_sorteadas
        self.qtd_min_acertos = qtd_min_acertos

        self._pth_folder, self._pth_file = self._create_init_file()
        self._sorteios = self._load_sorteios()

    def criar_relatorio(self, nome_relatorio: str,
                        propriedades_sorteio: list,
                        exp_filter=None,
                        insert_row_header=True) -> None:
        """
        Permite gerar relatórios com qualquer propriedade da classe Sorteio

        """

        def insert_header(header: list, elements: list) -> None:
            if insert_row_header:
                header += elements

        if len(self.sorteios) == 0:
            print(f'error <- file: {self._pth_file}, empty')

        else:
            file_nome = nome_relatorio + ' ' + self._nome + '.csv'
            pth_file = os.path.join(self._pth_folder, file_nome)

            if not exp_filter:
                lst_sorteios = self._sorteios

            else:
                sorteios_filter = exp_filter
                lst_sorteios = [s for s in self._sorteios if sorteios_filter(s)]

            try:
                with open(pth_file, encoding='utf-8', mode='w', newline='') as csv_file:
                    csv_wr = csv.writer(csv_file)

                    for s in lst_sorteios:
                        sorteio_row = []
                        header_row = []

                        for prop_sorteio in propriedades_sorteio:
                            if prop_sorteio == 'numero':
                                sorteio_row += [s.numero]
                                insert_header(header_row, ['num'])

                            elif prop_sorteio == 'data':
                                sorteio_row += [f'{s.data: %d/%m/%y}']
                                insert_header(header_row, ['data'])

                            elif prop_sorteio == 'sorteadas':
                                sorteio_row += s.sorteadas()
                                insert_header(header_row, [f'{b+1}' for b in range(len(s.bolas))])

                            elif prop_sorteio == 'sorteadas_len':
                                sorteio_row += [s.sorteadas_len()]
                                insert_header(header_row, ['qtd'])

                            elif prop_sorteio == 'sorteadas_sum':
                                sorteio_row += [s.sorteadas_sum()]
                                insert_header(header_row, ['soma'])

                            elif prop_sorteio == 'sorteadas_avg':
                                sorteio_row += [f'{s.sorteadas_avg(): .2f}']
                                insert_header(header_row, ['media'])

                            elif prop_sorteio == 'sorteadas_pares':
                                sorteio_row += s.sorteadas_pares()
                                insert_header(header_row, [f'{b+1}' for b in range(len(s.bolas)) if (b+1) % 2 == 0])

                            elif prop_sorteio == 'sorteadas_pares_len':
                                sorteio_row += [s.sorteadas_pares_len()]
                                insert_header(header_row, ['qtd'])

                            elif prop_sorteio == 'sorteadas_pares_sum':
                                sorteio_row += [s.sorteadas_pares_sum()]
                                insert_header(header_row, ['soma'])

                            elif prop_sorteio == 'sorteadas_pares_avg':
                                sorteio_row += [f'{s.sorteadas_pares_avg(): .2f}']
                                insert_header(header_row, ['media'])

                            elif prop_sorteio == 'sorteadas_impares':
                                sorteio_row += s.sorteadas_impares()
                                insert_header(header_row, [f'{b+1}' for b in range(len(s.bolas)) if (b+1) % 2 != 0])

                            elif prop_sorteio == 'sorteadas_impares_len':
                                sorteio_row += [s.sorteadas_impares_len()]
                                insert_header(header_row, ['qtd'])

                            elif prop_sorteio == 'sorteadas_impares_sum':
                                sorteio_row += [s.sorteadas_impares_sum()]
                                insert_header(header_row, ['soma'])

                            elif prop_sorteio == 'sorteadas_impares_avg':
                                sorteio_row += [f'{s.sorteadas_impares_avg(): .2f}']
                                insert_header(header_row, ['media'])

                            elif prop_sorteio == 'nao_sorteadas':
                                sorteio_row += s.nao_sorteadas()
                                insert_header(header_row, [f'{b+1}' for b in range(len(s.bolas))])

                            elif prop_sorteio == 'nao_sorteadas_len':
                                sorteio_row += [s.nao_sorteadas_len()]
                                insert_header(header_row, ['qtd'])

                            elif prop_sorteio == 'nao_sorteadas_sum':
                                sorteio_row += [s.nao_sorteadas_sum()]
                                insert_header(header_row, ['soma'])

                            elif prop_sorteio == 'nao_sorteadas_avg':
                                sorteio_row += [f'{s.nao_sorteadas_avg(): .2f}']
                                insert_header(header_row, ['media'])

                            elif prop_sorteio == 'nao_sorteadas_pares':
                                sorteio_row += s.nao_sorteadas_pares()
                                insert_header(header_row, [f'{b+1}' for b in range(len(s.bolas)) if (b+1) % 2 == 0])

                            elif prop_sorteio == 'nao_sorteadas_pares_len':
                                sorteio_row += [s.nao_sorteadas_pares_len()]
                                insert_header(header_row, ['qtd'])

                            elif prop_sorteio == 'nao_sorteadas_pares_sum':
                                sorteio_row += [s.nao_sorteadas_pares_sum()]
                                insert_header(header_row, ['soma'])

                            elif prop_sorteio == 'nao_sorteadas_pares_avg':
                                sorteio_row += [f'{s.nao_sorteadas_pares_avg(): .2f}']
                                insert_header(header_row, ['media'])

                            elif prop_sorteio == 'nao_sorteadas_impares':
                                sorteio_row += s.nao_sorteadas_impares()
                                insert_header(header_row, [f'{b+1}' for b in range(len(s.bolas)) if (b+1) % 2 != 0])

                            elif prop_sorteio == 'nao_sorteadas_impares_len':
                                sorteio_row += [s.nao_sorteadas_impares_len()]
                                insert_header(header_row, ['qtd'])

                            elif prop_sorteio == 'nao_sorteadas_impares_sum':
                                sorteio_row += [s.nao_sorteadas_impares_sum()]
                                insert_header(header_row, ['soma'])

                            elif prop_sorteio == 'nao_sorteadas_impares_avg':
                                sorteio_row += [f'{s.nao_sorteadas_impares_avg(): .2f}']
                                insert_header(header_row, ['media'])

                            else:
                                sorteio_row += [f'error {prop_sorteio}']
                                insert_header(header_row, ['error!'])

                        if insert_row_header:
                            csv_wr.writerow(header_row)
                            insert_row_header = False

                        csv_wr.writerow(sorteio_row)

            except PermissionError:
                print(f'error <- file: {os.path.basename(pth_file)}, open.')

            else:
                print(f'ok -> file: {os.path.basename(pth_file)}, created.')

    @property
    def sorteios(self):
        return self._sorteios

    @sorteios.setter
    def sorteios(self, value: list) -> None:
        self._sorteios = value

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        self._nome = value

    @property
    def qtd_bolas(self) -> int:
        return self._qtd_bolas

    @qtd_bolas.setter
    def qtd_bolas(self, value: int) -> None:
        self._qtd_bolas = value

    @property
    def qtd_sorteadas(self) -> int:
        return self._qtd_sorteadas

    @qtd_sorteadas.setter
    def qtd_sorteadas(self, value: int) -> None:
        self._qtd_sorteadas = value

    @property
    def qtd_min_acertos(self) -> int:
        return self._qtd_min_acertos

    @qtd_min_acertos.setter
    def qtd_min_acertos(self, value: tuple) -> None:
        self._qtd_min_acertos = value
