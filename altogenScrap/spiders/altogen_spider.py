from typing import OrderedDict
from altogenScrap.items import AltogenscrapItem
import scrapy
import re
# import xml.etree.ElementTree as ET

class BrainSpider(scrapy.Spider):
    # 명령어: scrapy crawl 이름

    # spider 이름
    name = "brain"

    # 시작 사이트
    start_urls = ['https://altogenlabs.com/xenograft-models/']
   
    def parse(self,response):

        # 전역변수 설정
        global url

        # 세부페이지 url
        # for i in range(1,11):
        #     url = response.css(f'#post-13 > div > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2) > a:nth-child({i})::attr(href)').get()
        #     print("URL:",url)
            
        #     yield scrapy.Request(url, callback=self.parse2,priority=1)
        
        # 삼중 for문 세부페이지 url
        for i in range(2,16):
            url_sels = response.css(f'#post-13 > div > table:nth-child(3) > tbody > tr:nth-child({i}) > td:nth-child(2)')
            test5 = url_sels.css('a').getall()
            for url_sel in url_sels:
                # print(i)
                n = len(test5)
                # print(n,test5,'^^^')
                for j in range(1,n+1):
                    url = url_sel.css(f'a:nth-child({j})::attr(href)').get()
                    yield scrapy.Request(url, callback=self.parse2)

    # 태그 삭제하는 함수 써보려했는데 안됨
    # def remove_tags(text):
    #     return ''.join(ET.fromstring(text).itertext())

    # def remove_html_tags(text):
    #     import re
    #     clean = re.compile('<.*?>')
    #     return re.sub(clean, '', text)

    def parse2(self, response):
        try:
            # item = {}
            item = AltogenscrapItem()

            brain_sels =  response.css('div.block-content > div.loop > article > div.entry-content')
            for brain_sel in brain_sels:

                # 이미지 src
                item['img'] = brain_sel.css('p:nth-child(1) > img::attr(src)').get()				

                # 제목
                item['title'] = brain_sel.css('p:nth-child(n+2) > strong::text').get()
                 
                # 내용
                # p 밑에 text를 가져오려 했는데 span이 포함된 것도 있어서 
                # 우선 태그까지 다 가져온뒤 re.sub로 태그만 지워줌
                test = brain_sel.css("p:nth-child(n+3)").getall()
                t = ''
                for i in test:
                    j = re.sub(re.compile('<.*?>'),'', i)
                
					# skip terminator string
                    if j.find('Download Altogen Labs') >=0:
                        continue

                    if j.find('PowerPoint Presentation') >=0:
                        continue

                    idx = j.find('Basic study design')

                    if idx >= 0:
                        break
                    else:
                        t += j
                        
                test = t

                item['content'] = test

                yield item

        except Exception as e:
            print('e: ', e)
        finally:
            print(item)