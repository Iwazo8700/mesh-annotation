import pysolr
solr_server_url = 'http://localhost:8983/solr/'
solr_collection = "mesh"
solr = pysolr.Solr(solr_server_url + solr_collection)
class solr_search():
