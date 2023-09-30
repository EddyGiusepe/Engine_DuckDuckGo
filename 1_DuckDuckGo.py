"""
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

DuckDuckGo
==========
Aqui estudamos este Engine de busca.
"""
import requests
from bs4 import BeautifulSoup


class DuckDuckGoSearch:
    def __init__(self):
        """Inicializa a classe DuckDuckGoSearch. Esta classe é usada 
           para realizar pesquisas no DuckDuckGo usando Python.
        """
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
                       }

    def search_duckduckgo(self, query: str):
        """
        Realiza uma pesquisa no DuckDuckGo com base na consulta fornecida.

        Args:
            query (str): A consulta de pesquisa.

        Exemplo:
            search = DuckDuckGoSearch()
            search.search_duckduckgo("Quanto está o dólar hoje?")
        """

        url = f'https://duckduckgo.com/html/?q={query}'
        
        try:
            # Enviar uma solicitação HTTP GET para a URL do DuckDuckGo com os cabeçalhos definidos:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                # Analisar a página HTML com BeautifulSoup:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Encontrar todos os links dos resultados (estão dentro de tags <a> com a classe "result__url")
                results = soup.find_all('a', class_='result__url', limit=3)
                
                if results: # Verifica se a lista de resultados não está vazia.
                    print("Resultados da pesquisa:")
                    for result in results:
                        print(result['href'])
                else:
                    print("Nenhum resultado encontrado.")
            else:
                print("A pesquisa não retornou resultados.")

        except Exception as e:
            print("Ocorreu um erro ao realizar a pesquisa:", str(e))


# Exemplo de uso:
if __name__ == "__main__":
    while True:
        duckduckgo = DuckDuckGoSearch()
        query = input("\033[033mDigite a sua query: \033[m")
        duckduckgo.search_duckduckgo(query)
        if not query:
            break
    