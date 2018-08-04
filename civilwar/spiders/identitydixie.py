# -*- coding: utf-8 -*-
import scrapy


class IdentitydixieSpider(scrapy.Spider):
    name = 'identitydixie'
    allowed_domains = ['identitydixie.com']
    start_urls = ['http://identitydixie.com/']

    def parse(self, response):
        for link in response.css('a::attr(href)').extract():
            print link.css('a::attr(href)').extract(),

        next_page = response.css('a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        page = response.url.split("/")[-2]
        filename = 'identity-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
