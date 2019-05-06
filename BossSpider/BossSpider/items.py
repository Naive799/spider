# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# Item是保存结构数据的地方
# Item提供了类字典的API，并且可以很方便的声明字段
# 很多Scrapy组件可以利用Item的其他信息。
import scrapy


class BOSSItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job = scrapy.Field()            # 工作名称
    company_name = scrapy.Field()   # 公司名
    salary = scrapy.Field()         # 工资
    location = scrapy.Field()       # 地点
    experience = scrapy.Field()     # 经验
    edu = scrapy.Field()            # 学历
    job_content = scrapy.Field()    # 工作描述
    job_requirement = scrapy.Field()# 职位要求
    com_num = scrapy.Field()        # 公司人数
    com_type = scrapy.Field()       # 公司类型
    com_level = scrapy.Field()      # 公司级别
