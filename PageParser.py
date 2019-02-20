import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class PageParser(object):
    def parse(self, new_url, content):
        soup = BeautifulSoup(content, 'html.parser')
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        dd = soup.select('dd.lemmaWgt-lemmaTitle-title')[0]
        title = dd.h1.get_text()
        # <div class="para" label-module="para">
        intro = soup.select('div.para[label-module=para]')[0].get_text()
        # <a target="_blank" href="/item/%E9%98%BF%E5%A7%86%
        new_full_urls = set()
        new_urls = soup.find_all(href=re.compile(r'/item/*'))
        for a in new_urls:
            rel_url = a['href']
            full_url = urljoin(new_url, rel_url)
            new_full_urls.add(full_url)

        data = {
            'title': title,
            'intro': intro
        }
        return new_full_urls, data
