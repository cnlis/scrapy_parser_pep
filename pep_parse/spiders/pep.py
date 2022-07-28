import re

import scrapy

from pep_parse.items import PepParseItem

PEP_NUMBER_PATTERN = r'^PEP (?P<number>\d+) .+$'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response, **kwargs):
        numerical_index = response.xpath('//*[@id="numerical-index"]')
        all_docs = numerical_index.css('a::attr(href)')
        for doc_link in all_docs:
            yield response.follow(doc_link, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get().strip()
        number = re.search(PEP_NUMBER_PATTERN, name).group(1)
        data = {
            'number': number,
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd::text'
            ).get().strip(),
        }
        yield PepParseItem(data)
