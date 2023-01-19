import requests


def coletar_dados(concurso):
    ret = requests.get(
        f'https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/{concurso}', verify=False).json()
    return ret

dados = coletar_dados(2717)

print(f"Dezenas sorteadas: {dados['listaDezenas']}")
print(
    f"Quantidade de ganhadores: {dados['listaRateioPremio'][0]['numeroDeGanhadores']}")

