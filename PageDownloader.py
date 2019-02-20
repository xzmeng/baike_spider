import requests


class PageDownloader(object):
    def download(self, new_url):
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        r = requests.get(new_url, headers=headers)
        return r.content
