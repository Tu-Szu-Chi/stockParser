# -*- coding: utf-8 -*-
import scrapy
from twse.items import TwseItem

class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ["www.twse.com.tw"]
    start_urls = (
        'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=html&date=20171018&type=13',
    )

    def parse(self, response):
        print('----------')
        items = []
        for tr in response.css('table > tbody > tr'):
            print('!!!tr!!!')
            yield self.parse_stock(tr)
        print('----------')

    def parse_stock(self, trSelector):
        item = TwseItem()
        item['id'] = trSelector.css('td:nth-child(1)::text').extract_first()
        item['name'] = trSelector.css('td:nth-child(2)::text').extract_first()
        item['tradeTotalShare'] = trSelector.css('td:nth-child(3)::text').extract_first()
        item['tradeTotalCount'] = trSelector.css('td:nth-child(4)::text').extract_first()
        item['tradeTotalPrice'] = trSelector.css('td:nth-child(5)::text').extract_first()
        item['openPrice'] = trSelector.css('td:nth-child(6)::text').extract_first()
        item['heightPrice'] = trSelector.css('td:nth-child(7)::text').extract_first()
        item['lowPrice'] = trSelector.css('td:nth-child(8)::text').extract_first()
        item['closePrice'] = trSelector.css('td:nth-child(9)::text').extract_first()
        item['benefitRatio'] = trSelector.css('td:nth-child(16)::text').extract_first()
        return item