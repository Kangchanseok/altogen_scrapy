from typing import OrderedDict
from urllib import response
import scrapy

class BrainSpider(scrapy.Spider):
    # spider 이름
    name = "brain23"
    # 크롤링하는 처음 사이트
    start_urls = ['https://altogenlabs.com/xenograft-models/']
   
    def start_requests(self):

        # 전역변수 설정
        global url

        # 세부페이지 url
        for i in range(1,11):
            url = response.css(f'#post-13 > div > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2) > a:nth-child({i})::attr(href)').get()
            yield scrapy.Request(url, callback=self.parse)

   
    
    def parse(self, response):
        try:
            item = OrderedDict()
            brain_sels =  response.css('div.block-content > div.loop > article > div.entry-content')
            for brain_sel in brain_sels:
                print('######################################')
                # 이미지 src
                item['img'] = brain_sel.css('p:nth-child(1) > img::attr(src)').get()
                # 제목
                test2 = brain_sel.css('p:nth-child(n+2) > strong::text').get()
                
                item['title'] = test2
                    
                # 내용
                test = brain_sel.css("p:nth-child(n+3)::text").getall()
                print('p size:',len(test))
                t = ''
                y=0
                for i in test:
                    j = str(i)

					# skip terminator string
                    if j.find('Download Altogen Labs') >=0:
                        continue

                    if j.find('PowerPoint Presentation') >=0:
                        continue

                    print('j:',j)

                    idx = j.find('Basic study design')
                    print('idx :',idx)

                    if idx >= 0:
                        print('End of paragraph')
                        break
                    else:
                        t += j
                        
                    print('Hello ',y)
                    y+=1
                
                test = t
                print('=============================================') 
                    
                item['content'] = test

                yield item
        except Exception as e:
            print('e: ', e)