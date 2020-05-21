# -*- coding: utf-8 -*-
import scrapy

class DcinsideSpider(scrapy.Spider):
    name = 'dcinside'
    allowed_domains = ['dcinside.com']

    # Usage: scrapy crawl dcinside -o dcinside.json -a category=animation -a pages=4 -a comments=false
    # GallId could will have to have custom appending due to archive changes
    def __init__(self, category=None, pages=None, minor=None, comments=None, recommend=None, *args, **kwargs):
        super(DcinsideSpider, self).__init__(*args, **kwargs)
        url = 'https://gall.dcinside.com/board/lists?id='
        my_pages = 1
        my_comments = False
        my_recommend = False


        if minor is not None:
            if minor == "true":
                url = 'https://gall.dcinside.com/mgallery/board/lists/?id='


        if category is not None:
            url = url + category
        else:
            url = url + 'hit'

        if pages is not None:
            my_pages = int(pages)


        if recommend is not None:
            if recommend == "true":
                url = url + '&exception_mode=recommend'

        if comments is not None:
            if comments == "true":
                my_comments = True
            else:
                my_comments = False

        my_pages = my_pages

        self.start_urls = [url + '&page=%s' % my_pages for my_pages in range(1, my_pages + 1)]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY':False,
        'DOWNLOAD_DELAY': 4
    }


    def parse(self, response):
        board_links = response.css('.us-post>.gall_tit>a:not([class])')
        yield from response.follow_all(board_links, self.parse_content)

    def parse_content(self, response):
        yield {
            'title': response.css('.title_subject::text').get(),
            'content': list(
                filter(
                    None, [s.strip() for s in response.xpath(
                        '//*[@class="gallview_contents"]//*[@class="writing_view_box"]/div//text()'
                    ).getall()]
                )
            )
        }
