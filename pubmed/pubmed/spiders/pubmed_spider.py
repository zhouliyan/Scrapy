# -*- coding: utf-8 -*-

import sys
reload(sys)
#python默认环境编码时ascii
sys.setdefaultencoding("utf-8")


from scrapy import signals, Spider
from pydispatch import dispatcher
from pubmed.items import PubmedItem


import cfg
startpoint = cfg.START
interval = cfg.INTERVAL
end = cfg.END
flag = 0


class PubmedSpider(Spider):
    name = "pubmed"
    allowed_domains = ["ncbi.nlm.nih.gov"]
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(PubmedSpider, self).__init__(*args, **kwargs)
        dispatcher.connect(self.queue_more_requests, signals.spider_idle)
        
    def queue_more_requests(self, spider):
        urls = self.get_urls()

        if not urls:
            return

        for url in urls:
            req = self.make_requests_from_url(url)
            self.crawler.engine.crawl(req, spider)


    def get_urls(self):
        global flag,startpoint
        
        if flag == 1:
            return
            
        if startpoint + interval > end:
            urls = ['https://www.ncbi.nlm.nih.gov/pubmed/%d' %(i) for i in range(startpoint,end+1)]
            flag = 1
            for url in urls:
                yield url
            return
            
        urls = ['https://www.ncbi.nlm.nih.gov/pubmed/%d' % (i) for i in range(startpoint,startpoint+interval)]
        startpoint += interval
        for url in urls:
            yield url
    
    
    def parse(self, response):
        item = PubmedItem()
        item['pmid'] = response.xpath('//div[@class="aux"]/div[@class="resc"]/dl[@class="rprtid"]/dd/text()').extract_first().strip()
        item['title'] = response.xpath('//h1/text()').extract_first().strip()
        item['author'] = response.xpath('//div[@class="auths"]/a/text()').extract()
        item['origin'] = response.xpath('//div[@class="cit"]/a/text()').extract_first().strip()
        item['date'] = response.xpath('//div[@class="cit"]/text()').extract_first().strip()
        item['abstract'] = response.xpath('//abstracttext/text()').extract_first()
        yield item
        