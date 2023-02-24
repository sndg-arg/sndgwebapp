import requests


class SolrClient:
    DEFAULT_POST_HEADERS = {'Content-type': 'application/json'}

    def __init__(self, solr_url="http://localhost:8983/solr/"):
        self.solr_url = solr_url

    def search(self, q='', fq='', sort='', start=0, rows=10):
        query_params = {
            'q': q,
            'fq': fq,
            'sort': sort,
            'start': start,
            'rows': rows
        }
        response = requests.get(f'{self.solr_url}/select', params=query_params)
        return response.json()

    def suggest(self, q='', count=5):
        query_params = {
            'q': q,
            'count': count
        }
        response = requests.get(f'{self.solr_url}/spell', params=query_params)
        return response.json()

    def add_documents(self, documents):
        response = requests.post(f'{self.solr_url}/update/json/docs', json=documents,
                                 headers=SolrClient.DEFAULT_POST_HEADERS)
        return response.json()

    def delete_documents(self, query):
        data = {'delete': {'query': query}}
        response = requests.post(f'{self.solr_url}/update', json=data, headers=SolrClient.DEFAULT_POST_HEADERS)
        return response.json()

    def add_field(self, name, field_type, indexed=True, stored=True, multivalue=False, doc_values=True):
        data = {
            'add-field': {
                'name': name,
                'type': field_type,
                'indexed': indexed,
                'stored': stored,
                'multiValued': multivalue,
                'docValues': doc_values
            }
        }
        response = requests.post(f'{self.solr_url}/schema', json=data, headers=SolrClient.DEFAULT_POST_HEADERS)
        return response.json()
