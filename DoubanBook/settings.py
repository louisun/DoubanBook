BOT_NAME = 'DoubanBook'

SPIDER_MODULES = ['DoubanBook.spiders']
NEWSPIDER_MODULE = 'DoubanBook.spiders'

ITEM_PIPELINES = {
    'DoubanBook.pipelines.DoubanBookPipeline': 300,
}

USER_AGENT = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"


ROBOTSTXT_OBEY = False
WEBSERVICE_ENABLED = False
TELNETCONSOLE_ENABLED = False

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 1

DOWNLOADER_MIDDLEWARES = {
    #    'DoubanBook.middlewares.UserAgent': 401,
    #    'DoubanBook.middlewares.CustomHeaders': 351,
    #    'DoubanBook.middlewares.SetCookie': 701,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'DoubanBook.middlewares.RotateUserAgentMiddleware': 400,
    #    'DoubanBook.middlewares.ProxyMiddleware': 100,
}

DUPEFILTER_CLASS = "DoubanBook.bloomfilter.BloomDupeFilter"


LOG_LEVEL = "INFO"

COOKIES_ENABLED = True
COOKIES_DEBUG = True


MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'douban_book'


PROXY_POOL = []

LOG_FILE = "/home/roadsheep/tmp/scrapy_douban_book.log"
#LOG_STDOUT = True

BOOK_CATEGORY = {'J.K.罗琳': '流行',
                 'UCD': '科技',
                 'UE': '科技',
                 'web': '科技',
                 '三毛': '流行',
                 '东野圭吾': '流行',
                 '两性': '生活',
                 '中国历史': '文化',
                 '中国文学': '文学',
                 '二战': '文化',
                 '互联网': '科技',
                 '交互': '科技',
                 '交互设计': '科技',
                 '亦舒': '流行',
                 '人文': '文化',
                 '人物传记': '文化',
                 '人际关系': '生活',
                 '企业史': '经营',
                 '传记': '文化',
                 '余华': '文学',
                 '佛教': '文化',
                 '健康': '生活',
                 '儿童文学': '文学',
                 '养生': '生活',
                 '军事': '文化',
                 '几米': '流行',
                 '创业': '经营',
                 '励志': '生活',
                 '历史': '文化',
                 '古典文学': '文学',
                 '古龙': '流行',
                 '名著': '文学',
                 '哲学': '文化',
                 '商业': '经营',
                 '回忆录': '文化',
                 '国学': '文化',
                 '外国名著': '文学',
                 '外国文学': '文学',
                 '奇幻': '流行',
                 '女性': '生活',
                 '安妮宝贝': '流行',
                 '宗教': '文化',
                 '家居': '生活',
                 '小说': '文学',
                 '幾米': '流行',
                 '广告': '经营',
                 '建筑': '文化',
                 '张小娴': '流行',
                 '张悦然': '流行',
                 '张爱玲': '文学',
                 '当代文学': '文学',
                 '心理': '生活',
                 '心理学': '文化',
                 '思想': '文化',
                 '悬疑': '流行',
                 '情感': '生活',
                 '戏剧': '文化',
                 '成长': '生活',
                 '手工': '生活',
                 '投资': '经营',
                 '推理': '流行',
                 '推理小说': '流行',
                 '摄影': '生活',
                 '政治': '文化',
                 '政治学': '文化',
                 '教育': '生活',
                 '散文': '文学',
                 '数学': '文化',
                 '文化': '文化',
                 '文学': '文学',
                 '旅行': '生活',
                 '日本文学': '文学',
                 '日本漫画': '流行',
                 '杂文': '文学',
                 '村上春树': '文学',
                 '杜拉斯': '文学',
                 '校园': '流行',
                 '武侠': '流行',
                 '沧月': '流行',
                 '港台': '文学',
                 '游记': '生活',
                 '漫画': '流行',
                 '灵修': '生活',
                 '爱情': '生活',
                 '王小波': '文学',
                 '理财': '经营',
                 '生活': '生活',
                 '用户体验': '科技',
                 '电影': '文化',
                 '社会': '文化',
                 '社会学': '文化',
                 '神经网络': '科技',
                 '科学': '科技',
                 '科幻': '流行',
                 '科幻小说': '流行',
                 '科技': '科技',
                 '科普': '科技',
                 '程序': '科技',
                 '穿越': '流行',
                 '童话': '文学',
                 '策划': '经营',
                 '算法': '科技',
                 '管理': '经营',
                 '米兰·昆德拉': '文学',
                 '经典': '文学',
                 '经济': '经营',
                 '经济学': '经营',
                 '绘本': '流行',
                 '绘画': '文化',
                 '编程': '科技',
                 '网络小说': '流行',
                 '美术': '文化',
                 '美食': '生活',
                 '考古': '文化',
                 '耽美': '流行',
                 '职场': '生活',
                 '股票': '经营',
                 '自助游': '生活',
                 '自由主义': '文化',
                 '艺术': '文化',
                 '艺术史': '文化',
                 '茨威格': '文学',
                 '营销': '经营',
                 '落落': '流行',
                 '西方哲学': '文化',
                 '言情': '流行',
                 '设计': '文化',
                 '诗歌': '文学',
                 '诗词': '文学',
                 '轻小说': '流行',
                 '近代史': '文化',
                 '通信': '科技',
                 '郭敬明': '流行',
                 '金庸': '流行',
                 '金融': '经营',
                 '钱钟书': '文学',
                 '阿加莎·克里斯蒂': '流行',
                 '随笔': '文学',
                 '青春': '流行',
                 '青春文学': '流行',
                 '韩寒': '流行',
                 '音乐': '文化',
                 '高木直子': '流行',
                 '魔幻': '流行',
                 '鲁迅': '文学'}
