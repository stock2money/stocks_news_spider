# -*- coding: utf-8 -*-
import scrapy


class A58moneysSpider(scrapy.Spider):
    name = '58moneys'
    allowed_domains = ['58moneys.com']
    start_urls = ['http://58moneys.com/']

    def parse(self, response):
        pass
