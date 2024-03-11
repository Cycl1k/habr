import requests
import asyncio
import aiohttp
import json
import time
from sql import sqlQuery, sqlUpdate

#url = 'https://habr.com/ru/hubs/'

async def fetch_page(session, url, idList): 
    
    async with session.get(url) as response:
        response = requests.get(url)
        response = response.text.split('TE__=')
        response = response[1].split(',"wysiwyg"')
        response = response[0] + '}'
        response = json.loads(response)
        #await scraping()
        
        js = {}
        jsonData = response['articlesList']['articlesList']
        for id in jsonData:
            if jsonData[id]['id'] in idList:
                print('Это запись уже есть в базе')
            else:
                js.update({
                    'post_id'       : jsonData[id]['id'],
                    'title'         : jsonData[id]['titleHtml'],
                    'post_date'     : jsonData[id]['timePublished'],
                    'post_url'      : 'https://habr.com/ru/articles/' + str(jsonData[id]['id']),
                    'author_name'   : jsonData[id]['author']['fullname'],
                    'author_url'    : 'https://habr.com/ru/users/' + str(jsonData[id]['author']['alias'])
                })
                sqlUpdate(js)
                print(js)
    


async def main():
    

    urls = 'https://habr.com/ru/hubs/'
    start_time = time.time()

    while True:
        circle_time = time.time()
        hub = sqlQuery('SELECT hubs_url FROM hubs')
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            idList = sqlQuery('SELECT post_id FROM posts')
            idStr = str(idList).replace('[','').replace(']','').replace('(','').replace(')','').replace(',,',',')

            for x in hub:
                url = urls + str(x[0]) + '/articles/'
                tasks.append(fetch_page(session, url, idStr)) 

            htmls = await asyncio.gather(*tasks)

        end_time = time.time()

        print(f"Time taken: {end_time - start_time} seconds")
        print(f"Time circle: {end_time - circle_time} seconds")
        print('5s Start!!!')
        await asyncio.sleep(600)

if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())

    loop.run_forever()