from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
doc = {"foos" : [{
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
},
{
 "color": "", 
 "taxonomy": "Computers & Accessories/Accessories & Peripherals/Laptop Accessories/Bags & Sleeves/Laptop Briefcases/Case Logic 15.4\" Slimline Case NCR - 15 Black Caselogic", 
 "site": "IN_amazon", 
 "currency": "INR", 
 "available_sizes": [], 
 "id": "B000EPFG5U", 
 "image_filename": "http://ecx.images-amazon.com/images/I/41tEnK%2Be1fL.jpg", 
 "style": "", 
 "fit": "", 
 "bestSellerRank": "", 
 "image_type": "look", 
 "review": [
  "Good bag.", 
  "Could not make out color while ordering. It is more green than expected;", 
  "Inside pouch re not useful for credit card,business card keeping... :-(", 
  "Great buy. Am very happy. Thank you!"
 ], 
 "name": "Case Logic 15.4\" Slimline Case NCR - 15 Black Caselogic", 
 "details": [
  "holds all the netbooks upto 15.4 inches", 
  "Slimline Case features Padded", 
  " ergonomically designed shoulder strap", 
  "reinforced carrying handle for exceptional comfort"
 ], 
 "image_filename_all": {
  "front": [], 
  "right": [], 
  "look": [
   "http://ecx.images-amazon.com/images/I/41tEnK%2Be1fL.jpg"
  ], 
  "back": [], 
  "left": []
 }, 
 "type": "", 
 "price": 1500.0, 
 "brand": "Case Logic", 
 "material": "Thick foam padding and durable material", 
 "similar_items": [], 
 "reviewStars": [
  "3.0 out of 5 stars", 
  "4.0 out of 5 stars"
 ], 
 "model_worn": "yes", 
 "care": "", 
 "neck": "", 
 "url": "http://www.amazon.in/Case-Logic-15-4-Slimline-NCR/dp/B000EPFG5U", 
 "gender": "all", 
 "length": "", 
 "avgStars": [], 
 "image_url": "http://ecx.images-amazon.com/images/I/41tEnK%2Be1fL.jpg", 
 "sleeves": ""
}]}
res = es.index(index="test-index", id=1, body=doc)
#print(res['result'])
#print("helloWorld")

res = es.get(index="test-index", id=1)
#print(res['_source'])

es.indices.refresh(index="test-index")

#res = es.search(index="test-index", body={"query": {"match_all": {}}})
res = es.search(index="test-index", body={"query": {"match": {"foos" : {"taxonomy" : "orange"} }}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(image_filename)s %(brand)s: %(price)s" % hit["_source"])