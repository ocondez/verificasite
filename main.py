from http.client import HTTPConnection
from urllib.parse import urlparse
import pandas as pd

def site_is_online(url, timeout=2):

    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error

lista = pd.read_excel('lista.xlsx')

for i in range(len(lista.index)):
    print(round((i/len(lista.index)*100), 2), '% ', lista.iat[i, 0])
    try:
        if site_is_online(lista.iat[i, 0]) == True:
            lista.iat[i, 1] = "Sim"
        else:
            lista.iat[i, 1] = "Não"
    except:
        lista.iat[i, 1] = "Não"

lista.to_excel('listaverificada.xlsx', index=False)