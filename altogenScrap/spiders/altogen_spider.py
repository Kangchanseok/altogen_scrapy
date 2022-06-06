# # import scrapy

# # class BrainSpider(scrapy.Spider):
# #     name = "brain"

# #     def start_requests(self):
# #         urls = [
# #             'https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/ln-229-xenograft-model/',
# #             'https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/sk-n-as-xenograft-model/',
# #             'https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/u87-xenograft-model/'

# #         ]
# #         for url in urls:
# #             yield scrapy.Request(url=url, callback=self.parse)

# #     def parse(self, response):
# #         try:
# #             item = {}
# #             brain_sels = response.css('div.block-content > div.loop > article > div.entry-content')
# #             for brain_sel in brain_sels:
# #                 # 이미지 src
# #                 item['img'] = brain_sel.css('p:nth-child(1) > img::attr(src)').get()
# #                 # # 제목
# #                 item['title'] = brain_sel.css('p:nth-child(2) > strong::text').get()
# #                 # # 내용
# #                 # item['content'] = brain_sel.css('p:nth-child(3)::text').get()
# #                 # print(123456)
# #                 i = 3
# #                 # test = ''
# #                 test = brain_sel.css("p:nth-child(n+3)::text").getall()
# #                 t = ''
# #                 for i in test:
# #                     print("[")
# #                     print(i)
# #                     print("]")
# #                     print('\n')
# #                     j = str(i)

# #                     if j == 'Download Altogen Labs ':
# #                         print('hello')
# #                         break
# #                     else:
# #                         t += j
                        
                
# #                 test = t
# #                 print(t)
# #                 print(len(test))
# #                 print('kang')
# #                 # print(test)
# #                 # while True:
# #                 #     t = brain_sel.css('p:nth-child(n+3)').get()
# #                 #     print(t)
# #                 #     if t == 'Download Altogen Labs ':
# #                 #         print(123)
# #                 #         break
# #                 #     test += t
# #                 #     print(test)
                    
# #                 item['content'] = test

# #                 yield item
# #         except Exception as e:
# #             print('e: ', e)

# from typing import OrderedDict
# import scrapy


# class BrainSpider(scrapy.Spider):
#     name = "brain"

#     def start_requests(self):
        
#         # urls = response.css('div.entry-content > table:nth-child(1) > tbody > tr(n+2) > td > a::attr(href)')
#         # yield scrapy.Request(url='https://altogenlabs.com/xenograft-models/', callback=self.parse2)
#         # urls = url2
#         urls = [
#             'https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/ln-229-xenograft-model/',
#             "https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/sf-268-xenograft-model/",
#             "https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/sf-295-xenograft-model/",
#             "https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/sf-539-xenograft-model/",
#             'https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/sk-n-as-xenograft-model/',
#             'https://altogenlabs.com/xenograft-models/brain-cancer-xenograft/u87-xenograft-model/',
#             'https://altogenlabs.com/xenograft-models/lung-cancer-xenograft/a549-xenograft-model/',
#             'https://altogenlabs.com/xenograft-models/melanoma-xenograft/sk-mel-2-xenograft-model/',
#             'https://altogenlabs.com/xenograft-models/pancreatic-xenograft-models/miapaca-2-xenograft-model/'		
#         ]
        
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     # def parse2(self, response):
#     #     try:
#     #         url2 = []
#     #         url_sels = response.css('div.entry-content')
#     #         for url_sel in url_sels:
#     #             # url
#     #             # item['url'] = url_sel.css('table:nth-child(1) > tbody > tr(n+2) > td > a::attr(href)').get()
#     #             url2 = url_sel.css('table:nth-child(1)').get()

#     #             yield url2
#     #     except Exception as e:
#     #         print('e: ', e)
    
#     async def parse(self, response):
#         try:
#             item = OrderedDict()
#             brain_sels =  response.css('div.block-content > div.loop > article > div.entry-content')
#             for brain_sel in brain_sels:
#                 print('######################################')
#                 # 이미지 src
#                 item['img'] = brain_sel.css('p:nth-child(1) > img::attr(src)').get()
#                 # 제목
#                 test2 = brain_sel.css('p:nth-child(n+2) > strong::text').get()
#                 # t2 = ''
#                 # for k in test2:
#                 #     # print(k)
#                 #     # print('@@@@@@@@@')
#                 #     # if len(k) == 0:
#                 #     #     continue
#                 #     # if (k+1) != 0:
#                 #     #     break
#                 #     # else:
#                 #     t2 += k
#                 # test2 = t2
#                 # print('############')
#                 # print(test2)
#                 item['title'] = test2
                    
#                 # 내용
#                 test = brain_sel.css("p:nth-child(n+3)::text").getall()
#                 print('p size:',len(test))
#                 t = ''
#                 y=0
#                 for i in test:
#                     j = str(i)

# 					# skip terminator string
#                     if j.find('Download Altogen Labs') >=0:
#                         continue

#                     if j.find('PowerPoint Presentation') >=0:
#                         continue

#                     print('j:',j)

#                     idx = j.find('Basic study design')
#                     print('idx :',idx)

#                     if idx >= 0:
#                         print('End of paragraph')
#                         break
#                     else:
#                         t += j
                        
#                     print('Hello ',y)
#                     y+=1
                
#                 test = t
#                 print('=============================================') 
                    
#                 item['content'] = test


#                 yield item
#         except Exception as e:
#             print('e: ', e)



# from altogenScrap.items import AltogenscrapItem
# import scrapy

# class BrainSpider(scrapy.Spider):
#     # spider 이름
#     name = "brain"

#     # 시작 사이트
#     start_urls = ['https://altogenlabs.com/xenograft-models/']
   
#     def parse(self,response):
#         # 전역변수 설정
#         global url

#         # 세부페이지 url
#         for i in range(1,11):
#             url = response.css(f'#post-13 > div > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2) > a:nth-child({i})::attr(href)').get()
#             yield scrapy.Request(url, callback=self.parse2)
        
#         # 삼중포문으로 해야되나?
#         # for i in range(2,16):
#         #     url_sels = response.css(f'#post-13 > div > table:nth-child(3) > tbody > tr:nth-child({i}) > td:nth-child(2)')
#         #     test5 = url_sels.css('a').getall()
#         #     for url_sel in url_sels:
#         #         # print(i)
#         #         n = len(test5)
#         #         # print(n,test5,'^^^')
#         #         for j in range(1,n+1):
#         #             url = url_sel.css(f'a:nth-child({j})::attr(href)').get()
#         #             yield scrapy.Request(url, callback=self.parse2)


#     def parse2(self, response):
#         try:
#             # item = {}
#             item = AltogenscrapItem()
#             brain_sels =  response.css('div.block-content > div.loop > article > div.entry-content')
#             for brain_sel in brain_sels:

#                 # 이미지 src
#                 item['img'] = brain_sel.css('p:nth-child(1) > img::attr(src)').get()

#                 # 제목
#                 item['title'] = brain_sel.css('p:nth-child(n+2) > strong::text').get()
                 
#                 # 내용

#                 if brain_sel.css("p:nth-child(n+3) > span::text").get(): 
#                     test = brain_sel.css("p:nth-child(n+3) > span::text").get()
#                 else:
#                     test = brain_sel.css("p:nth-child(n+3)::text").getall()
#                 t = ''
#                 for i in test:
#                     j = str(i)
                    
#                     # p밑에 span 인거는 어떻게 처리해야할까...?
#                     # print(len(j),'***')
#                     # print(j)
#                     # if len() <= 1:
#                     #     # print('^^^^^^^')
#                     #     j = brain_sel.css("p:nth-child(n+3) > span::text").get()


# 					# skip terminator string
#                     if j.find('Download Altogen Labs') >=0:
#                         continue

#                     if j.find('PowerPoint Presentation') >=0:
#                         continue

#                     idx = j.find('Basic study design')

#                     if idx >= 0:
#                         # print(len(j), '^')
#                         # j = brain_sel.css("p:nth-child(n+3) > span::text").get()
#                         break
#                     else:
#                         t += j

#                     # print(len(j),'###')
#                     # if len(j) == 0:
#                     #     j = brain_sel.css("p:nth-child(n+3) > span::text").get()
#                     #     t+=j
#                 test = t               

#                 item['content'] = test
                
#                 yield item
#         except Exception as e:
#             print('e: ', e)

from altogenScrap.items import AltogenscrapItem
import scrapy
import re
import xml.etree.ElementTree as ET

class BrainSpider(scrapy.Spider):
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
        #     yield scrapy.Request(url, callback=self.parse2)
        
        # 삼중포문으로 해야되나?
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

    def remove_tags(text):
        return ''.join(ET.fromstring(text).itertext())

    def remove_html_tags(text):
        import re
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def parse2(self, response):
        try:
            # item = {}
            item = AltogenscrapItem()
            brain_sels =  response.css('div.block-content > div.loop > article > div.entry-content')
            xy = 0
            for brain_sel in brain_sels:
#            for ii,brain_sel in enumerate(brain_sels):

#                if ii > 2:
#                    break

                # 이미지 src
                item['img'] = brain_sel.css('p:nth-child(1) > img::attr(src)').get()
#                print("$$$Img:",item['img']);
				

                # 제목
                item['title'] = brain_sel.css('p:nth-child(n+2) > strong::text').get()
#                print("$$$Title:",item['title']);
                 
                # 내용

                #span = brain_sel.css("p span:nth-child(n+3) > span::text").getall()
#                span = brain_sel.css("p:nth-child(n+3) > span::text").getall()
#                print("$$$ SPAN len =",len(span))
#                print("$$$ SPAN:",span)


                test = brain_sel.css("p:nth-child(n+3)").getall()
                print("$$$ test len =",len(test))
                print("$$$ test  =",test)

                t = ''
                for i in test:
                    #print(" ith elem:=",i)
                    print("############################ i=[",i)
                    # j = str(i)
                    #j = i.css("p:nth-child(1)::text")
                    #j = remove_tags(i)
                    #j = remove_html_tags(i)
                    j = re.sub(re.compile('<.*?>'),'', i)
                    #j = remove_tage(i)
                    print("############################ j=[",j)
                    
                    
                    # p밑에 span 인거는 어떻게 처리해야할까...?
#                    print("len j=[",len(j))
#                    if len(j) == 0:
#                        print('##############################################')
#                        j = brain_sel.css("p:nth-child(n+3) > span::text").get()

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
