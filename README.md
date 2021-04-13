# PW - Pesquisa na Web

## ElasticSearch

### Adicionar ficheiro ao elastic:
```
curl -XPOST "http://localhost:9200/test/_doc/1" -H "Content-Type: application/json" -d @file1.json
```
or use the python [script](https://github.com/gomes53/pw/blob/master/esPostFile.py)

### Ver ficheiro:
```
curl -XGET "http://localhost:9200/test/_doc/1"
```
### Fazer uma pesquisa com GET no kibana:

Abrir kibana: http://localhost:5601/app/dev_tools#/console?load_from=https:/www.elastic.co/guide/en/elasticsearch/reference/current/snippets/923.console

Fazer pedido:
```
GET /_search
{
  "query": {
    "match": {
      "taxonomy" : "bags"
    }
  }
}
```
