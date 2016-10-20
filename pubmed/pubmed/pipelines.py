# -*- coding: utf-8 -*-


import codecs
import os
import spiders.cfg as cfg

if not os.path.exists(cfg.PATH):
    os.mkdir(cfg.PATH)
    
class PubmedPipeline(object):
    def process_item(self, item, spider):
        file = codecs.open(cfg.PATH + '/%s.txt' % (item['pmid']), mode = 'w',encoding='utf-8')
        
        file.write(item['title']+'\n')
        file.write('/'.join(item['author'])+'\n')      
        file.write(item['origin']+'\n')
        file.write(item['date']+'\n')
        if item['abstract']:
            file.write(item['abstract'])
        file.write('\n')
        return item
