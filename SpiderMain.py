import PageDownloader
import PageParser
import ResultOutputer
import UrlManager


class SpiderMain(object):
    def __init__(self, root_url):
        self.root_url = root_url
        self.urls = UrlManager.UrlManager()
        self.urls.add_new_url(root_url)
        self.downloader = PageDownloader.PageDownloader()
        self.parser = PageParser.PageParser()
        self.outputer = ResultOutputer.ResultOutputer()

    def crawl(self):
        all_data = []
        count = 0
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print('crawling {}: {}'.format(count, new_url))
            content = self.downloader.download(new_url)
            new_urls, data = self.parser.parse(new_url, content)
            self.urls.add_new_urls(new_urls)
            all_data.append(data)
            if count == 100:
                break
            count += 1

        self.outputer.add_data(all_data)


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider = SpiderMain(root_url)
    spider.crawl()
