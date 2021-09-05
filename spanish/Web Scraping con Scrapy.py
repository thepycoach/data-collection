import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Obtener todas las filas (rows) de la tabla
        rows = response.xpath('//tr')

        for row in rows:
            # Extraer el titulo (title), pais (country) y poblacion (population)
            # title = response.xpath('//h1/text()').get()
            countries = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()

            # Devolver data extraida
            yield {
                # 'titles': title,
                'countries': countries,
                'population': population,
            }
