import os

#manipular json
try: 
    import json
except:
    os.system("pip install json")
    import json

#requisições
try:
    import requests
except: #caso não esteja instalado
    os.system("pip install requests")
    import requests

from falar import falar


def noticias():
    url = "https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey=f2ce0afed90948d881c586f6a25090bf"

    news = requests.get(url).text

    news_dict = json.loads(news)
    
    artigos = news_dict["articles"]
    
    falar("Origem: Google News (Brasil)")
    
    falar("Notícias de hoje")
    
    for index, articles in enumerate(artigos):
        falar(articles["title"])
    
        if index == len(artigos) - 1:
            break
        falar("Próxima notícia...")
    
    falar("Acabou as notícias ...")