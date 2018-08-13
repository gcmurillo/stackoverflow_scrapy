import re
import json

from scrapy import Spider, Item, Field

class StackoverflowItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tema = Field()
    votos = Field()
    vistas = Field()
    respuestas = Field()


class StackOverFlow(Spider):

    def __init__(self):
        file = open('results.csv', 'w')
        cadena = 'tab/language,question,votes,views,answers\n'
        file.write(cadena)
        file.close()

    name = "StackOverFlow"
    languages_urls = [
        "https://es.stackoverflow.com/questions/tagged/php",
        "https://es.stackoverflow.com/questions/tagged/javascript",
        "https://es.stackoverflow.com/questions/tagged/java",
        "https://es.stackoverflow.com/questions/tagged/android",
        "https://es.stackoverflow.com/questions/tagged/html",
        "https://es.stackoverflow.com/questions/tagged/c%23",
        "https://es.stackoverflow.com/questions/tagged/jquery",
        "https://es.stackoverflow.com/questions/tagged/python",
        "https://es.stackoverflow.com/questions/tagged/android-studio"
    ]

    tab_urls = [
        "https://es.stackoverflow.com/?tab=active",
        "https://es.stackoverflow.com/?tab=featured",
        "https://es.stackoverflow.com/?tab=hot",
        "https://es.stackoverflow.com/?tab=week",
        "https://es.stackoverflow.com/?tab=month"
    ]

    start_urls = tab_urls + languages_urls

    def get_extracted(value, index=0):
        try:
            return value[index]
        except:
            return ""


    def parse(self, response):
        file = open('results.csv', 'a+')
        languages = ['php', 'javascript', 'java', 'android', 'html', 'c%23', 'jquery', 'python', 'android-studio']
        language = str(response).split('/')[-1].strip('>')
        if language in languages:
            tema_extract = response.xpath('//a[@class="question-hyperlink"]/text()').extract()
            votos_extract = response.xpath('//span[@class="vote-count-post "]//strong/text()').extract()
            vistas_extract = response.xpath('//div[@class="views "]/text()').extract()
            respuestas_extract = response.xpath('//div[contains(@class, "status")]//strong/text()').extract()
            i = 0
            while i < len(tema_extract):
                '''print("Lenguage: " + language)
                print('Tema: ' + tema_extract[i])
                print('Votos: ' + votos_extract[i])
                print('Vistas: ' + vistas_extract[i])
                print('Respuestas: ' + respuestas_extract[i])
                print('\n')'''
                vistas = [s for s in vistas_extract[i].strip() if s.isdigit()][0]
                cadena = language + ",\"" + tema_extract[i] + "\"," + votos_extract[i] + "," + vistas + "," + respuestas_extract[i] + '\n'
                print(cadena)
                file.write(cadena)
                i += 1
        else:
            tab = str(response).split('=')[-1].strip('>')
            tema_extract = response.xpath('//a[@class="question-hyperlink"]/text()').extract()
            votos_extract = response.xpath('//div[@class="votes"]//span/text()').extract()
            vistas_extract = response.xpath('//div[@class="views"]//span/text()').extract()
            respuestas_extract = response.xpath('//div[contains(@class, "status")]//span/text()').extract()
            i = 0
            while i < len(tema_extract):
                '''
                print(tab)
                print('Tema: ' + tema_extract[i])
                print('Votos: ' + votos_extract[i])
                print('Vistas: ' + vistas_extract[i])
                print('Respuestas: ' + respuestas_extract[i])
                print('\n')'''
                cadena = tab + ",\"" + tema_extract[i] + "\"," + votos_extract[i] + "," + vistas_extract[i] + "," + respuestas_extract[i] + '\n'
                print(cadena)
                file.write(cadena)
                i+=1
        file.close()
