import requests # Alt + Enter
import json

key = 'Opchl4dUTt5YAAlLu0c%2BsGORkwekJdrfjhlKff2NiYhU%2FaEulm5Wk9fIJH2My7jhE9snVCr83ymkEj%2BLMj99Uw%3D%3D'
url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows=10&delngDe=20151202&prdlstCd=1001&_type=json'
print(url)
data = requests.get(url)

jo = json.loads(data.content)
print(jo['response']['body'])
