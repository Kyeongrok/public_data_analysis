import requests # Alt + Enter
import json
import pandas as pd

def call_api(key, num_of_rows, date, prd_cd):
    url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={num_of_rows}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
    print(url)
    data = requests.get(url)

    jo = json.loads(data.content)
    total_cnt = jo['response']['body']['totalCount']
    print('total_cnt:', total_cnt)
    items = jo['response']['body']['items']
    if items == '':
        return []
    return items['item']

if __name__ == '__main__':
    key = 'Opchl4dUTt5YAAlLu0c%2BsGORkwekJdrfjhlKff2NiYhU%2FaEulm5Wk9fIJH2My7jhE9snVCr83ymkEj%2BLMj99Uw%3D%3D'
    prd_cd = '1202'

    rct = pd.date_range(start='20210101', end='20210427')
    dt_list = rct.strftime("%Y%m%d").to_list()

    for date in dt_list:
        r = call_api(key, 30000, date, prd_cd)
        with open(f'./1202/1202_{date}.json', 'w+') as f:
            f.write(json.dumps(r))

