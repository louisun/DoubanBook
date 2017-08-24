import pymongo
import xpinyin
from scrapy.conf import settings
from .settings import BOOK_CATEGORY

class DoubanBookPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient(
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']
        )
        self.db = client[settings['MONGODB_DBNAME']]
        self.p = xpinyin.Pinyin()

    def process_item(self, item, spider):
        if spider.name != "book":
            return item

        if not item.get("subject_id"):
            return item

        if item.get('real_tag'):
            collection_name = self.p.get_pinyin(BOOK_CATEGORY[item.get('real_tag')],'')
        else:
            collection_name = 'no_tag'
        del item['real_tag']

        spec = {"subject_id": item["subject_id"]}

        self.db[collection_name].update(
            spec, {'$set': dict(item)}, upsert=True)
        return item
