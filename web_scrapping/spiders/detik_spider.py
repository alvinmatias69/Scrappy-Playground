import scrapy

class DetikSpider(scrapy.Spider):
    name = "detik"
    base_date = ''
    base_url = 'https://news.detik.com/indeks/all/'
    page = 1

    def start_requests(self):
        date = getattr(self, 'date', '02/26/2018')
        self.set_date(date)
        yield scrapy.Request(
            self.base_url + str(self.page) + '?date=' + date,
            callback=self.parse
        )

    def increment_page(self):
        self.page += 1

    def set_date(self, date):
        self.base_date = date

    def parse(self, response):
        titles = response.css('h2::text').extract()

        for title in titles:
            yield {
                'title': title
            }

        if len(titles) > 0:
            self.increment_page()
            yield scrapy.Request(
                self.base_url + str(self.page) + '?date=' + self.base_date,
                callback=self.parse
            )
