from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
doc = {
 "color": "", 
 "taxonomy": "Clothing & Accessories/Women/Ethnic Wear/Lehenga Cholis/Pink with Orange Net lehenga choli", 
 "site": "IN_amazon", 
 "currency": "INR", 
 "available_sizes": [], 
 "id": "5449836767", 
 "image_filename": "http://ecx.images-amazon.com/images/I/51kpVddAIML.jpg", 
 "style": "", 
 "fit": "", 
 "bestSellerRank": " #1,26,792 in Clothing & Accessories ( )", 
 "image_type": "look", 
 "review": [], 
 "name": "Pink with Orange Net lehenga choli", 
 "details": [
  "Pink with Orange Net lehenga choli"
 ], 
 "image_filename_all": {
  "front": [], 
  "right": [], 
  "look": [
   "http://ecx.images-amazon.com/images/I/51kpVddAIML.jpg"
  ], 
  "back": [], 
  "left": []
 }, 
 "type": "", 
 "price": 499.0, 
 "brand": "Radheshyam Enterprise", 
 "material": "", 
 "similar_items": [
  "http://www.amazon.in//Phoenix-Design-Womens-western-Phoenix1212-FreeSize_Red/dp/B01D9Q3BDE?ie=UTF8&psc=1", 
  "http://www.amazon.in//Sanjana-Georgette-Lehenga-Lehnga_SC9133_Free-Size_Green/dp/B01C8DW8HO?ie=UTF8&psc=1", 
  "http://www.amazon.in//Colors-Lifestyle-Womens-Lehenga-Aaslh2003Rjga/dp/B00XRFZX5M?ie=UTF8&psc=1", 
  "http://www.amazon.in//Shreebalaji-Enterprise-CottonSilk-Lehenga-PINKKUDDY_Pink_Free/dp/B01CNWSB76?ie=UTF8&psc=1", 
  "http://www.amazon.in//We-Can-Shop-lengha-WCS-030_Multicolor_Free/dp/B01AW51G78?ie=UTF8&psc=1", 
  "http://www.amazon.in//SAILAXMI-FASHION-Womens-Lehenga-SLF_LEH_Sangeet_01_Red_Free_Size/dp/B01DM2FTVM?ie=UTF8&psc=1"
 ], 
 "reviewStars": [], 
 "model_worn": "yes", 
 "care": "", 
 "neck": "", 
 "url": "http://www.amazon.in/Pink-Orange-Net-lehenga-choli/dp/5449836767", 
 "gender": "women", 
 "length": "", 
 "avgStars": [], 
 "image_url": "http://ecx.images-amazon.com/images/I/51kpVddAIML.jpg", 
 "sleeves": ""
}
res = es.index(index="test-indeces", id=3, body=doc)
#print(res['result'])
#print("helloWorld")

# res = es.get(index="test-index", id=1)
# #print(res['_source'])

# es.indices.refresh(index="test-index")

# #res = es.search(index="test-index", body={"query": {"match_all": {}}})
# res = es.search(index="test-index", body={"query": {"match": {"taxonomy" : "orange" }}})
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(image_filename)s %(brand)s: %(price)s" % hit["_source"])