import scrapy

class ApartmentPriceSpider(scrapy.Spider):
    name = 'apartment_price'
    start_urls = [
        'https://www.caasa.it/treviso/treviso/appartamento/in-vendita.html',
    ]

    def parse(self, response):
        for post in response.css('div.price-results'):
            yield {
                'price': post.xpath("ul/li/b[@title='prezzo']/text()").get(),
                'surface': post.xpath("ul/li/b[@title='superficie']/text()").get(),
            }

        next_page = response.css('li.arrow-next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
