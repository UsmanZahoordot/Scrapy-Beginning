import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.brightbazaarblog.com/']

    def parse(self, response):
        file = open("file.html",'wb')
        file.write(response.body)