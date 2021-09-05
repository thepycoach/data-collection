import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Getting all the rows of the table
        rows = response.xpath('//tr')

        for row in rows:
            # Extracting title, country names and population
            # title = response.xpath('//h1/text()').get()
            countries = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()

            # Return data extracted
            yield {
                # 'titles': title,
                'countries': countries,
                'population': population,
            }
