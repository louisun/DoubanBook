import random
from scrapy.spiders import Spider, Request
from ..settings import BOOK_CATEGORY
from scrapy.conf import settings
from ..items import DoubanbookItem
from ..helper import gen_bids


class BookSpider(Spider):

    name = 'book'

    allowed_domains = ['book.douban.com', ]

    # custom_settings = {'CONCURRENT_REQUESTS': 30,
    #                    'CONCURRENT_REQUESTS_PER_DOMAIN': 30,
    #                    'COOKIES_DEBUG': True}

    def __init__(self):
        super(BookSpider, self).__init__()
        self.bids = gen_bids()

    # 自动从 start_url 开始请求，解析提取 restrict_xpaths 中链接（必须匹配 allow），回调 parse，继续跟进提取的链接
    # rules =  (Rule(LinkExtractor(allow='/tag/小说', restrict_xpaths=(
    #     '//span[@class="next"]/a')), callback='parse', follow=False),)

    def start_requests(self):
        tags = BOOK_CATEGORY.keys()
        for tag in tags:
            url = 'https://book.douban.com/tag/' +  tag
            request = Request(url=url, callback=self.parse, cookies={
                              'bid': random.choice(self.bids)})
            request.meta['real_tag'] = tag
            yield request

    def parse(self, response):
        links = response.xpath('//div[@class="info"]/h2/a/@href').extract()
        for link in links:
            request = Request(url=link, callback=self.parse_detail, cookies={'bid': random.choice(self.bids)})
            request.meta['real_tag'] = response.meta['real_tag']
            yield request

        next_page = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_page:
            next_page = response.urljoin(next_page[0])
            request = Request(url=next_page, callback=self.parse, cookies={'bid': random.choice(self.bids)})
            request.meta['real_tag'] = response.meta['real_tag']
            yield request

    # scrapy parse --spider=book(指定spider) -c parse_detail(指定解析函数) -v url
    # scrapy shell --spider=douban url
    def parse_detail(self, response):
        item = DoubanbookItem()
        subject_id = response.url.split('/')[-2]

        item['subject_id'] = subject_id
        item['name'] = response.xpath(
            '//div[@id="wrapper"]/h1/span/text()').extract_first().strip()
        item['img_link'] = response.xpath(
            '//div[@id="mainpic"]/a/img/@src').extract_first().strip()

        info_list = []
        info_dict = {}
        for i in response.xpath('//div[@id="info"]//text()').extract():
            strip_i = i.replace('\n', '').replace(' ', '').replace('\xa0', '')
            if strip_i:
                info_list.append(strip_i)
        tmp_list = []
        before = None
        for i in info_list:
            if i == ':':
                continue
            if i == '作者':
                i = '作者:'
            if i == '译者':
                i = '译者:'
            if i == '出版社':
                i = '出版社:'
            if i == '原作名':
                i = '原作名:'
            if i.endswith(':'):
                if before:
                    info_dict[before] = ''.join(tmp_list)
                before = i
                tmp_list = []
            else:
                tmp_list.append(i)
                if before == 'ISBN:':
                    info_dict[before] = ''.join(tmp_list)

        item['author'] = info_dict.get('作者:')
        item['publisher'] = info_dict.get('出版社:')
        item['original'] = info_dict.get('原作名:')
        item['translator'] = info_dict.get('译者:')
        item['publish_date'] = info_dict.get('出版年:')
        item['page_num'] = info_dict.get('页数:')
        item['price'] = info_dict.get('定价:')
        item['isbn'] = info_dict.get('ISBN:')

        score_l = response.xpath(
            '//div[@class="rating_self clearfix"]/strong/text()').extract()
        rating_sum_l = response.xpath(
            '//div[@class="rating_sum"]/span/a/span/text()').extract()
        item['score'] = score_l[0].strip() if score_l else None
        item['rating_num'] = rating_sum_l[0].strip() if rating_sum_l else None

        item['tags'] = response.xpath(
            '//div[@id="db-tags-section"]/div/span/a/text()').extract()

        item['real_tag'] = response.meta['real_tag']
        yield item
