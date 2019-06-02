# -*- coding: utf-8 -*-
import scrapy
from stocks_news_spider.items import NewsItem

class A58moneysSpider(scrapy.Spider):
    name = '58moneys'
    allowed_domains = ['58moneys.com']
    start_urls = ['https://www.58moneys.com/finance.html',
                  'https://www.58moneys.com/finance2.html',
                  'https://www.58moneys.com/finance3.html',
                  'https://www.58moneys.com/finance4.html',
                  'https://www.58moneys.com/finance5.html',
                  'https://www.58moneys.com/finance6.html',
                  'https://www.58moneys.com/finance7.html',
                  'https://www.58moneys.com/finance8.html',
                  'https://www.58moneys.com/finance9.html']
                  
    base_url = 'https://www.58moneys.com'

    def parse(self, response):
        print("---", response)
        news = response.xpath('//*[@id="ajaxGetNewsList"]/ul/li')
        for each in news:
            item = NewsItem()
            item["title"] = each.xpath('./div[1]/a/text()').extract()[0]
            item["time"] = each.xpath('./div[2]/text()').extract()[0]
            item["href"] = self.base_url + each.xpath('./div[1]/a/@href').extract()[0]
            request = scrapy.Request(url=item["href"], callback=self.parseHref)
            request.meta['item'] = item
            yield request
            # print(item)

    def parseHref(self, response):
        item = response.meta['item']
        article = response.xpath('//div[@class="nr"]/p')
        detail = ''
        for p in article:
            if len(p.xpath('./text()').extract()) > 0:
                detail += p.xpath('./text()').extract()[0]
        item['detail'] = detail
        yield item
