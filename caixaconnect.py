import requests
import os
import datetime

loterias_caixa = {'lotofacil': 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip'}



def create_folder_results(folder_name):
    pth_folder = os.path.join('.\\', folder_name, 'results')
    if os.path.exists(pth_folder):
        print(f'ok ==> pasta {pth_folder} localizada...')
        return pth_folder
    else:
        print(f'ok ==> criando pasta local: {pth_folder}')
        os.mkdir(pth_folder)
        if os.path.exists(pth_folder):
            print(f'ok ==> pasta {pth_folder} criada...')
            return pth_folder
        else:
            print(f'error <== não foi possível criar a pasta {pth_folder}...')
            return ''


def get_results(loto_name, url):
    folder_pth = create_folder_results(loto_name)
    if folder_pth:
        file_name = 'download_'+loto_name+'.zip'
        file_dir = os.path.join(folder_pth, file_name)
        reqget = requests.get(url)
        if reqget.status_code == 200:
            print(f'ok ==> baixando resultados da lotofácil...')
            with open(file_dir, 'wb') as f:
                f.write(reqget.content)
            if os.path.exists(file_dir) and os.path.isfile(file_dir):
                print(f'ok ==> arquivo atualizado..')
            else:
                raise FileExistsError('Erro de arquivo....')
        else:
            raise ConnectionRefusedError(f'não foi possível conectar ao site:{reqget.status_code}')


if __name__ == '__main__':
    concurso =  'lotofacil'
    get_results(concurso, loterias_caixa[concurso])
