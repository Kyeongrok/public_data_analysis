import requests # Alt + Enter
import json

def call_api(key, num_of_rows, date, prd_cd):
    url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={num_of_rows}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
    print(url)
    data = requests.get(url)

    jo = json.loads(data.content)
    print(jo)
    items = jo['response']['body']['items']
    print(items)

    # item = items['item']
    # return item

if __name__ == '__main__':
    key = 'Opchl4dUTt5YAAlLu0c%2BsGORkwekJdrfjhlKff2NiYhU%2FaEulm5Wk9fIJH2My7jhE9snVCr83ymkEj%2BLMj99Uw%3D%3D'
    date = '20200105'
    prd_cd = '1202'

    r = call_api(key, 200, date, prd_cd)
    # print(len(r))

