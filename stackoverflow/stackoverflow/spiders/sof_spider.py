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


    ]

    start_urls = tab_urls

    def get_extracted(value, index=0):
        try:
            return value[index]
        except:
            return ""


    def parse(self, response):
        languages = ['php', 'javascript', 'java', 'android', 'html', 'c%23', 'jquery', 'python', 'android-studio']
        language = str(response).split('/')[-1].strip('>')
        if language in languages:
            tema_extract = response.xpath('//a[@class="question-hyperlink"]/text()').extract()
            votos_extract = response.xpath('//span[@class="vote-count-post "]//strong/text()').extract()
            vistas_extract = response.xpath('//div[@class="views "]/text()').extract()
            respuestas_extract = response.xpath('//div[contains(@class, "status")]//strong/text()').extract()

            i = 0
            while i < len(tema_extract):
                print("Lenguage: " + language)
                print('Tema: ' + tema_extract[i])
                print('Votos: ' + votos_extract[i])
                print('Vistas: ' + vistas_extract[i])
                print('Respuestas: ' + respuestas_extract[i])
                print('\n')
                i += 1

        else:
            tema_extract = response.xpath('//a[@class="question-hyperlink"]/text()').extract()
            i = 0
            while i < len(tema_extract):
                print('Tema: ' + tema_extract[i])
