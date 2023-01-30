from bs4 import BeautifulSoup
import mechanicalsoup as mec
from requests import get
from time import sleep



from kitano.browser import metamorproxies as proxies_,soldier_boy

headers = {'user-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
            'connection': 'keep-alive', 'upgrade-insecure-requests': '1', 
#            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6'}



def search_google(term,limit_results=20):
    term = term.replace(" ","+")
    start = 0
    proxies = None
    results = []
    for i in range(limit_results):
        url_google = f'https://www.google.com/search?q={term}&start={start}&num={limit_results-1}'
        page_google = soldier_boy.sniper_get(url_google)
        
        soup = BeautifulSoup(page_google.text, "html.parser")
        #print(soup)
        result_block = soup.find("div", attrs={"id": "center_col"}).find_all('div')
        #andando = 0
        for result in result_block:
            #print('eu toh andando, doido',andando)
            #andando = andando + 1
            #print(result)
            link = result.find("a", href=True)
            title = result.find("h3")
            description_box = result.find("div", {"style": "-webkit-line-clamp:2"})
            if link and title and description_box:
                start = start+1
            
                print(f'result number: {start}')
                res = {'title':title.text,'link':link['href'],'descript':description_box.text,'indice':start}
                results.append(res)
            
        
    return results
            
print(search_google('cosmos pdf'))