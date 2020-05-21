# -*- coding: utf-8 -*-
import scrapy

class OPGGSpider(scrapy.Spider):
    name = 'opgg'
    allowed_domains = ['talk.op.gg']

    # Usage: scrapy crawl opgg -o opgg.json -a category=animation -a pages=4 -a comments=false
    def __init__(self, category=None, pages=None, minor=None, comments=None, recommend=None, *args, **kwargs):
        super(OPGGSpider, self).__init__(*args, **kwargs)
        url = 'https://talk.op.gg/s/lol/all?sort=popular'
        my_pages = 1
        my_comments = False
        my_recommend = False

        if category is not None:
            url = url + category
        else:
            url = url + 'hit'

        if pages is not None:
            my_pages = int(pages)

        my_pages = my_pages

        self.start_urls = [url + '&page=%s' % my_pages for my_pages in range(1, my_pages + 1)]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY':False,
        'DOWNLOAD_DELAY': 4
    }

    def parse(self, response):
        board_links = response.css('.article-list-item__info')
        yield from response.follow_all(board_links, self.parse_content)

    def parse_content(self, response):
        yield {
            'title': response.css('.article__title::text').get(),
            'content': list(
                filter(
                    None, [s.strip() for s in response.xpath(
                        '//*[@class="article-content"]//text()'
                    ).getall()]
                )
            )
        }
