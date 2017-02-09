"""View states for asp.net"""

import scrapy

class MiddSpider(scrapy.Spider):
    name = 'midd_spider'
    start_urls = ['http://bookstore.middlebury.edu/SelectTermDept.aspx']
    download_delay = 1.5

    def parse(self, response):
        """for author in response.css('select#author > option ::attr(value)').extract():
            yield scrapy.FormRequest(
                'http://quotes.toscrape.com/filter.aspx',
                formdata={
                    'author': author,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_tags
            )"""

#Reverse engineer the above code to work for the middlebury book store.

        for term in response.css('select#ctl00_ctl00_Content_Content_courseSelect_select_term" > option ::attr(text)').extract():
            yield scrapy.FormRequest(
                'http://bookstore.middlebury.edu/SelectTermDept.aspx',
                formdata={
                    'term': term,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_depts
            )




    def parse_depts(self, response):
        """for tag in response.css('select#tag > option ::attr(value)').extract():
            yield scrapy.FormRequest(
                'http://quotes.toscrape.com/filter.aspx',
                formdata={
                    'author': response.css(
                        'select#author > option[selected] ::attr(value)'
                    ).extract_first(),
                    'tag': tag,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_results,
            )"""

        for department in response.css('select#ctl00_ctl00_Content_Content_courseSelect_select_dept > option ::attr(text)').extract():
            yield scrapy.FormRequest(
                'http://bookstore.middlebury.edu/SelectTermDept.aspx',
                formdata={
                    'term': response.css(
                        'ctl00_ctl00_Content_Content_courseSelect_select_term > option[selected]  ::attr(text)'
                    ).extract_first(),
                    'department': department,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_section
            )
#ctl00_ctl00_Content_Content_courseSelect_select_dept > option:nth-child(1)

    def parse_section(self, response):
        """for section in response.css("//*[@id='ctl00_ctl00_Content_Content_courseSelect_select_section'] > option ::attr(text)").extract():
            yield scrapy.FormRequest(
                'http://bookstore.middlebury.edu/SelectTermDept.aspx',
                formdata={
                    'term': response.css(
                        'ctl00_ctl00_Content_Content_courseSelect_select_term > option[selected]  ::attr(text)'
                    ).extract_first(),
                    'department': css.response(
                        'select#ctl00_ctl00_Content_Content_courseSelect_select_dept > option[selected] ::attr(text)'
                    ).extract_first(),
                    'section': section,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_add"""

            for section in response.css("//*[@id='ctl00_ctl00_Content_Content_courseSelect_select_section'] > option ::attr(text)").extract():
                yield {
                    'section': section
                }

            )

    """def parse_add(self, response):
        FormRequest.from_response(
            response,
            formdata={
               'ctl00$ctl00$Content$Content$courseSelect$btnAddCourseToList'
            },
            dont_click=True,
            dont_filter=True,
            callback=self.parse
        )"""

































"""import scrapy

class SpidyQuotesViewStateSpider(scrapy.Spider):
    name = 'lol'
    start_urls = ['http://quotes.toscrape.com/search.aspx']
    download_delay = 1.5

    def parse(self, response):
        for author in response.css('select#author > option ::attr(value)').extract():
            yield scrapy.FormRequest(
                'http://quotes.toscrape.com/filter.aspx',
                formdata={
                    'author': author,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_tags
            )

    def parse_tags(self, response):
        for tag in response.css('select#tag > option ::attr(value)').extract():
            yield scrapy.FormRequest(
                'http://quotes.toscrape.com/filter.aspx',
                formdata={
                    'author': response.css(
                        'select#author > option[selected] ::attr(value)'
                    ).extract_first(),
                    'tag': tag,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_results,
            )

    def parse_results(self, response):
        for quote in response.css("div.quote"):
            yield {
                'quote': response.css('span.content ::text').extract_first(),
                'author': response.css('span.author ::text').extract_first(),
                'tag': response.css('span.tag ::text').extract_first(),
            }"""


















"""import scrapy


class MiddSpider(scrapy.Spider):
    name = "midd"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }"""