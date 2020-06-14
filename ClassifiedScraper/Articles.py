from Prepare import *

class Articles(Prepare):
    txt_file = 'articles.txt'
    write_mode = 'w'
    time_sleep = None

    def __init__(self, input_urls, articles, pages = None, results = None, proxies = None, headers = None,
    split_results = None, split_pages = None):
        super().__init__(input_urls, articles)

        pages = None if pages is None else pages
        results = None if results is None else results
        headers = None if headers is None else headers
        proxies = None if proxies is None else proxies
        split_results = None if split_results is None else split_results
        split_pages = None if split_pages is None else split_pages

        self.pages = pages
        self.results = results
        self.headers = headers
        self.proxies = proxies
        self.split_results = split_results
        self.split_pages = split_pages

    def get_articles(self):
        print("Collecting articles")
        with open(self.txt_file, self.write_mode, encoding="utf-8") as f:
            for input_url in self.input_urls:
                url = input_url.split('/')[2]
                source = self.get_url(input_url)
                soup = self.get_soup(source)
                arts = self.soup_attributes(soup, *self.articles)
                results = self.get_results(soup)
                try:
                    pages = self.get_pages_from_results(results, len(arts)) if self.pages is None else self.get_pages(soup)
                except:
                    pages = 1
                newlines = self.get_pages_urls(pages, input_url)
                for newline in newlines:
                    source = self.get_url(newline)
                    soup = self.get_soup(source)
                    arts = self.soup_attributes(soup, *self.articles)
                    for article in arts:
                        href = article.find('a')['href']
                        if url not in href:
                            f.write('http://' + url + href+'\n')
                        else:
                            f.write(href+'\n')
                    self.time_sleep
        f.close()
        print("Number of unique articles collected: " + str(len(txt_read(self.txt_file))))
        print("")
