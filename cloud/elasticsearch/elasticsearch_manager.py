import elasticsearch
from settings import ELASTIC_PASSWORD, ELASTIC_CLOUD_ID, ES_INDEX


class ElasticSearch:
    def __init__(self):
        self.es_instance = elasticsearch.Elasticsearch(
            basic_auth=('elastic', ELASTIC_PASSWORD), cloud_id=ELASTIC_CLOUD_ID
        )

    def get_aggregated_data(self, field, size):
        query_params = {
            "aggs": {
                "count_is": {
                    "terms": {
                        "field": field,
                        "size": size
                    }
                }
            }
        }
        response = self.es_instance.search(index=ES_INDEX, body=query_params)
        return response.get('aggregations').get('count_is').get('buckets')

    def get_top_animals(self, top_size):
        return self.get_aggregated_data("animals.animal_type.keyword", top_size)

    def get_top_streets(self, top_size):
        return self.get_aggregated_data("animals.street_address.keyword", top_size)

