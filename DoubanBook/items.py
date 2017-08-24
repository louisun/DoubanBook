import scrapy


class DoubanbookItem(scrapy.Item):
    subject_id = scrapy.Field()
    name = scrapy.Field()

    img_link = scrapy.Field()

    author = scrapy.Field()
    publisher = scrapy.Field()
    original = scrapy.Field()
    translator = scrapy.Field()
    publish_date = scrapy.Field()
    page_num = scrapy.Field()
    price = scrapy.Field()
    isbn = scrapy.Field()

    score = scrapy.Field()
    rating_num = scrapy.Field()
 
    tags = scrapy.Field()
    real_tag = scrapy.Field()