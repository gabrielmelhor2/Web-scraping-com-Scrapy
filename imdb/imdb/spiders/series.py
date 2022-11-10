import scrapy


class FilmesSpider(scrapy.Spider):
    name = 'series'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250']

    def parse(self, response):
        series = response.css(".titleColumn")
        for serie in series:
            yield {
                'title': serie.css(".titleColumn a::text").get(),
                'year': serie.css(".titleColumn span::text").get()
            }
