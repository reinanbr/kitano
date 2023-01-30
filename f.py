from bs4 import BeautifulSoup
import mechanicalsoup as mec
from requests import get
from time import sleep



#from getpdf.google.user_agents import get_useragent



def _req(term, results, lang, start, proxies):
    resp = br.get("https://www.google.com/search")
    #     headers=headers,
    #     params=dict(
    #         q=term,
    #         num=results + 2,  # Prevents multiple requests
    #         hl=lang,
    #         start=start,
    #     ),
    #     proxies=proxies,
    # )
    resp.raise_for_status()
    return resp


class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"


def search(term, num_results=10, lang="en", proxy=None, advanced=False, sleep_interval=0,start=0):
    escaped_term = term.replace(" ", "+")

    # Proxy
    # proxies = None
    # if proxy:
    #     if proxy.startswith("https"):
    #         proxies = {"https": proxy}
    #     else:
    #         proxies = {"http": proxy}
    prox = proxies_.api_proxy()[0]
    print(prox)
    proxi = f'https://{prox["Ip"]}:{prox["Port"]}'
    proxies = {'https':proxi}

    # Fetch
    start = start
    while start < num_results:
        # Send request
        try:
            resp = _req(escaped_term, num_results - start, lang, start, proxies)

            # Parse
            soup = BeautifulSoup(resp.text, "html.parser")
            result_block = soup.find_all("div", attrs={"class": "g"})
            for result in result_block:
                # Find link, title, description
                link = result.find("a", href=True)
                title = result.find("h3")
                description_box = result.find("div", {"style": "-webkit-line-clamp:2"})
                if description_box:
                    description = description_box.find("span")
                    if link and title and description:
                        start += 1
                        if advanced:
                            return SearchResult(link["href"], title.text, description.text)
                        else:
                            return link["href"]
            sleep(sleep_interval)
        except Exception as e:
            print(start)
            print('oh shits. lats go again Error:',e)
            return search(term=term, num_results=num_results, lang=lang, proxy=proxy, advanced=advanced, sleep_interval=sleep_interval,start=start)

print(search('cosmos filetype:pdf'))