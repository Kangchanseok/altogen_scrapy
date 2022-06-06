# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter, XmlItemExporter, JsonItemExporter
import json

class CsvPipeline(object):
    def __init__(self):
        self.file = open("assets/altogen.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class JsonPipeline(object):
    def __init__(self):
        # self.list_items = []
        self.file = open("assets/altogen.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        # ordered_list = [None for i in range(len(self.list_items))]
        # for i in self.list_items:
        #     ordered_list[int(i['id']-1)] = json.dumps(dict(i))

        # for i in ordered_list:
        #     self.file.write(str(i)+",\n")
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        # self.list_items.append(item)
        self.exporter.export_item(item)
        return item

class XmlPipeline(object):
    def __init__(self):
        self.file = open("assets/altogen.xml", 'wb')
        self.exporter = XmlItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item