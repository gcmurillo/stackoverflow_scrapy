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
    start_urls = ["http://es.stackoverflow.com"]

    def get_extracted(value, index=0):
        try:
            return value[index]
        except:
            return ""


    def parse(self, response):
        tema_extract = response.xpath('//a[@class="question-hyperlink"]/text()').extract()
        votos_extract = response.xpath('//div[@class="votes"]//span/text()').extract()
        vistas_extract = response.xpath('//div[@class="views"]//span/text()').extract()
        respuestas_extract = response.xpath('//div[contains(@class, "status")]//span/text()').extract()

        i = 0
        while i < len(tema_extract):
            print('Tema: ' + tema_extract[i])
            print('Votos: ' + votos_extract[i])
            print('Vistas: ' + vistas_extract[i])
            print('Respuestas: ' + respuestas_extract[i])
            print('\n')
            i += 1
