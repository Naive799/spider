# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from BossSpider.items import BOSSItem

import re


class BossSpider(CrawlSpider):
    name = 'boss'  # 命名
    allowed_domains = ['zhipin.com']  # 过滤爬取的域名，不在此允许范围内的域名就会被过滤，而不会进行爬取
    start_urls = ['https://www.zhipin.com/c101020100/?query=%E4%B8%8A%E6%B5%B7&page=1&ka=page-1']  # 启动时爬取的url列表

    rules = (
        Rule(LinkExtractor(allow=r'c101020100/?query=上海.*&?page=.*'), follow=True),  # 爬虫爬取规则
        Rule(LinkExtractor(allow=r'job_detail/\w.*'), callback='parse_item', follow=True),
        # allow是允许爬取的规则，后面的内容是正则表达式，匹配页面中所有符合匹配规则的标签
        # callback是回调函数，用于解析抓取到的符合匹配的链接
        # follow：是否跟进，是否继续请求抓取到的链接
    )
    custom_settings = {
        "COOKIES_ENABLED": False
        #
    }

    def parse_item(self, response):
        article_items = BOSSItem() # 实例化BOSSItem()
        job = response.css('.info-primary h1:nth-child(1)::text').extract()[0] #抽取网页内容
        company_name = response.css('.job-sec.prop-item+div h3+div::text').extract()[0]
        salary = response.css('.info-primary span.salary::text').extract()[0]
        salary = str(re.search(".*?(\d+.*\d)", salary).group(1)).strip().replace('-', ',')#正则匹配
        location = response.css('.info-primary>p::text').extract()[0]
        experience = response.css('.info-primary>p::text').extract()[1]
        edu = response.css('.info-primary>p::text').extract()[2]
        job_content = response.css('.detail-content div:nth-child(2)::text').extract()[1]
        job_requirement = response.css('.detail-content div:nth-child(2)::text').extract()[2]
        com_num = response.css('.sider-company p:nth-child(4)::text').extract_first()
        com_type = response.css('a[ka="job-detail-brandindustry"]::text').extract()[0]
        com_level = response.css('.sider-company p:nth-child(3)::text').extract()[0]

        article_items['job'] = job
        article_items['company_name'] = company_name
        article_items['salary'] = salary
        article_items['location'] = location
        article_items['experience'] = experience
        article_items['edu'] = edu
        article_items['job_content'] = job_content
        article_items['job_requirement'] = job_requirement
        article_items['com_num'] = com_num
        article_items['com_type'] = com_type
        article_items['com_level'] = com_level
        yield article_items#生成器函数
