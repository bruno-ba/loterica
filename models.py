import os
import csv
from dataclasses import dataclass, field, InitVar

from datetime import datetime

@dataclass
class Sorteio:
    ''' dataclass sorteio '''
    numero: int
    data: datetime
    bolas: InitVar[tuple]
    bolas_sorteadas: tuple = field(init=False)
    bolas_sorteadas_pares: tuple = field(init=False)
    bolas_sorteadas_pares_len: int = field(init=False)
    bolas_sorteadas_pares_sum: int = field(init=False)
    bolas_sorteadas_pares_avg: float = field(init=False)
    bolas_sorteadas_pares_zero_fill: tuple = field(init=False)
    bolas_sorteadas_impares: tuple = field(init=False)
    bolas_sorteadas_impares_len: int = field(init=False)
    bolas_sorteadas_impares_sum: int = field(init=False)
    bolas_sorteadas_impares_avg: float = field(init=False)
    bolas_sorteadas_impares_zero_fill: tuple = field(init=False)
    bolas_nao_sorteadas: tuple = field(init=False)
    bolas_nao_sorteadas_pares: tuple = field(init=False)
    bolas_nao_sorteadas_pares_len: int = field(init=False)
    bolas_nao_sorteadas_pares_sum: int = field(init=False)
    bolas_nao_sorteadas_pares_avg: float = field(init=False)
    bolas_nao_sorteadas_pares_zero_fill: tuple = field(init=False)
    bolas_nao_sorteadas_impares: tuple = field(init=False)
    bolas_nao_sorteadas_impares_len: int = field(init=False)
    bolas_nao_sorteadas_impares_sum: int = field(init=False)
    bolas_nao_sorteadas_impares_avg: float = field(init=False)
    bolas_nao_sorteadas_impares_zero_fill: tuple = field(init=False)
    bolas_sorteadas_zero_fill: tuple = field(init=False)
    bolas_nao_sorteadas_zero_fill: tuple = field(init=False)

    def __post_init__(self, bolas):
        self.bolas_sorteadas = tuple(k for k, v in bolas if v)
        self.bolas_sorteadas_pares = tuple(k for k, v in bolas if v if k % 2 == 0)
        self.bolas_sorteadas_pares_len = len(self.bolas_sorteadas_pares)
        self.bolas_sorteadas_pares_sum = sum(self.bolas_sorteadas_pares)
        self.bolas_sorteadas_pares_avg = self.bolas_sorteadas_pares_sum/self.bolas_sorteadas_pares_len
        self.bolas_sorteadas_pares_zero_fill = tuple(k if v else '.' for k, v in bolas if k % 2 == 0)
        self.bolas_sorteadas_impares = tuple(k for k, v in bolas if v if k % 2 != 0)
        self.bolas_sorteadas_impares_len = len(self.bolas_sorteadas_impares)
        self.bolas_sorteadas_impares_sum = sum(self.bolas_sorteadas_impares)
        self.bolas_sorteadas_impares_avg = self.bolas_sorteadas_impares_sum/self.bolas_sorteadas_impares_len
        self.bolas_sorteadas_impares_zero_fill = tuple(k if v else '.' for k, v in bolas if k % 2 != 0)
        self.bolas_nao_sorteadas = tuple(k for k, v in bolas if (not v))
        self.bolas_nao_sorteadas_pares = tuple(k for k, v in bolas if (not v) if k % 2 == 0)
        self.bolas_nao_sorteadas_pares_len = len(self.bolas_nao_sorteadas_pares)
        self.bolas_nao_sorteadas_pares_sum = sum(self.bolas_nao_sorteadas_pares)
        self.bolas_nao_sorteadas_pares_avg = self.bolas_nao_sorteadas_pares_sum/self.bolas_nao_sorteadas_pares_len
        self.bolas_nao_sorteadas_pares_zero_fill = tuple(k if (not v) else '.' for k, v in bolas if k % 2 == 0)
        self.bolas_nao_sorteadas_impares = tuple(k for k, v in bolas if (not v) if k % 2 != 0)
        self.bolas_nao_sorteadas_impares_len = len(self.bolas_nao_sorteadas_impares)
        self.bolas_nao_sorteadas_impares_sum = sum(self.bolas_nao_sorteadas_impares)
        self.bolas_nao_sorteadas_impares_avg = self.bolas_nao_sorteadas_impares_sum/self.bolas_nao_sorteadas_impares_len
        self.bolas_nao_sorteadas_impares_zero_fill = tuple(k if (not v) else '.' for k, v in bolas if k % 2 != 0)
        self.bolas_sorteadas_zero_fill = tuple(('P' if k % 2 == 0 else 'I') if v else '.' for k, v in bolas)
        self.bolas_nao_sorteadas_zero_fill = tuple(('P' if k % 2 == 0 else 'I') if (not v) else '.' for k, v in bolas)


class Concurso:
    def _create_init_file(self) -> tuple:
        pth_folder = os.path.join('.\\', self.nome)
        file_nome = 'resultados' + '_' + self.nome + '.csv'
        pth_file = os.path.join(pth_folder, file_nome)

        if os.path.exists(pth_file):
            print(f'\nok -> file: {os.path.basenome(pth_file)}, found.')

        else:
            os.makedirs(pth_folder)
            file = open(pth_file, mode='w', encoding='utf-8', newline='')
            file.close()
            print(f'\nok -> file: {os.path.basenome(pth_file)}, created.')

        return pth_folder, pth_file

    def _load_sorteios(self) -> list:
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
                    print(f'warning <- file: {os.path.basenome(self._pth_file)}, empty.')

                else:
                    print(f'ok -> file: {os.path.basenome(self._pth_file)}, filled.')
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

    def __init__(self, nome: str, qtd_bolas: int, qtd_sorteadas: int, qtd_min_acertos: int):
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

    def criar_relatorio(self, nome_relatorio: str, propriedades_sorteio: list) -> None:
        if len(self.sorteios) == 0:
            print(f'error <- file: {self._pth_file}, empty')
        else:
            file_nome = nome_relatorio + '_' + self._nome + '.csv'
            pth_file = os.path.join(self._pth_folder, file_nome)
            try:
                with open(pth_file, encoding='utf-8', mode='w', newline='') as csv_file:
                    csv_wr = csv.writer(csv_file)

                    for s in self.sorteios:
                        sorteio_row = []

                        for a in propriedades_sorteio:
                            if a == 'numero':
                                sorteio_row.append(s.numero)

                            elif a == 'data':
                                sorteio_row.append(f'{s.data: %x}')

                            elif a == 'bolas':
                                sorteio_row += [*s.bolas]

                            elif a == 'bolas_sorteadas':
                                sorteio_row += [*s.bolas_sorteadas]

                            elif a == 'bolas_sorteadas_pares':
                                sorteio_row += [*s.bolas_sorteadas_pares]

                            elif a == 'bolas_sorteadas_pares_len':
                                sorteio_row.append(s.bolas_sorteadas_pares_len)

                            elif a == 'bolas_sorteadas_pares_sum':
                                sorteio_row.append(s.bolas_sorteadas_pares_sum)

                            elif a == 'bolas_sorteadas_pares_avg':
                                sorteio_row.append(f'{s.bolas_sorteadas_pares_avg: .2f}')

                            elif a == 'bolas_sorteadas_pares_zero_fill':
                                sorteio_row = sorteio_row + [*s.bolas_sorteadas_pares_zero_fill]

                            elif a == 'bolas_sorteadas_impares':
                                sorteio_row += [*s.bolas_sorteadas_impares]

                            elif a == 'bolas_sorteadas_impares_len':
                                sorteio_row.append(s.bolas_sorteadas_impares_len)

                            elif a == 'bolas_sorteadas_impares_sum':
                                sorteio_row.append(s.bolas_sorteadas_impares_sum)

                            elif a == 'bolas_sorteadas_impares_avg':
                                sorteio_row.append(f'{s.bolas_sorteadas_impares_avg: .2f}')

                            elif a == 'bolas_sorteadas_impares_zero_fill':
                                sorteio_row += [*s.bolas_sorteadas_impares_zero_fill]

                            elif a == 'bolas_nao_sorteadas':
                                sorteio_row += [*s.bolas_nao_sorteadas]

                            elif a == 'bolas_nao_sorteadas_pares':
                                sorteio_row += [*s.bolas_nao_sorteadas_pares]

                            elif a == 'bolas_nao_sorteadas_pares_len':
                                sorteio_row.append(s.bolas_nao_sorteadas_pares_len)

                            elif a == 'bolas_nao_sorteadas_pares_sum':
                                sorteio_row.append(s.bolas_nao_sorteadas_pares_sum)

                            elif a == 'bolas_nao_sorteadas_pares_avg':
                                sorteio_row.append(f'{s.bolas_nao_sorteadas_pares_avg: .2f}')

                            elif a == 'bolas_nao_sorteadas_pares_zero_fill':
                                sorteio_row += [*s.bolas_nao_sorteadas_pares_zero_fill]

                            elif a == 'bolas_nao_sorteadas_impares':
                                sorteio_row += [*s.bolas_nao_sorteadas_impares]

                            elif a == 'bolas_nao_sorteadas_impares_len':
                                sorteio_row.append(s.bolas_nao_sorteadas_impares_len)

                            elif a == 'bolas_nao_sorteadas_impares_sum':
                                sorteio_row.append(s.bolas_nao_sorteadas_impares_sum)

                            elif a == 'bolas_nao_sorteadas_impares_avg':
                                sorteio_row.append(f"{s.bolas_nao_sorteadas_impares_avg: .2f}")

                            elif a == 'bolas_nao_sorteadas_impares_zero_fill':
                                sorteio_row += [*s.bolas_nao_sorteadas_impares_zero_fill]

                            elif a == 'bolas_sorteadas_zero_fill':
                                sorteio_row += [*s.bolas_sorteadas_zero_fill]

                            elif a == 'bolas_nao_sorteadas_zero_fill':
                                sorteio_row += [*s.bolas_nao_sorteadas_zero_fill]

                            else:
                                sorteio_row.append('error <- s.prop')

                        csv_wr.writerow(sorteio_row)

            except PermissionError:
                print(f'error <- file: {os.path.basenome(pth_file)}, open.')

            else:
                print(f'ok -> file: {os.path.basenome(pth_file)}, created.')

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
    def qtd_min_acertos(self, value: int) -> None:
        self._qtd_min_acertos = value
