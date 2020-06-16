from Prepare import *

class Data(Prepare):
    format_num = 1
    csv_separator = ','
    data_file = 'data.csv'
    write_mode = 'w'
    time_sleep = None
    
    def __init__(self, input_urls, articles = None, pages = None, results = None, proxies = None, headers = None,
    split_results = None, split_pages = None, **kwargs):
        super().__init__(input_urls, articles)

        articles = None if articles is None else articles
        pages = None if pages is None else pages
        results = None if results is None else results
        proxies = None if proxies is None else proxies
        headers = None if headers is None else headers
        split_results = None if split_results is None else split_results
        split_pages = None if split_pages is None else split_pages

        self.input_urls = input_urls
        self.articles = articles
        self.pages = pages
        self.results = results
        self.proxies = proxies
        self.headers = headers
        self.split_results = split_results
        self.split_pages = split_pages
        self.kwargs = kwargs

    def keywords(self, soup, url):
        dic = {}
        #* ili **
        for x in self.kwargs:
            if len(self.kwargs[x]) == 1:
                try:
                    dic[x] = self.soup_attribute(soup, self.kwargs[x][0]).text.strip()
                except:
                    dic[x] = None
            elif len(self.kwargs[x]) == 2:
                try:
                    dic[x] = self.soup_attribute(soup, self.kwargs[x][0], self.kwargs[x][1])
                except:
                    dic[x] = None
        dic['Search Link'] = url
        dic['Date collected'] = datetime.today().strftime('%Y-%m-%d')
        return dic
    
    def column_names(self):
        return ['Search Link', 'Date collected'] + [x for x in self.kwargs]
    
    def get_data(self):
        print("Scraping data")
        if self.articles is None:
            with open(self.data_file, self.write_mode, encoding='utf-8') as f:
                w = csv.DictWriter(f, self.column_names(), delimiter =self.csv_separator, lineterminator='\n')
                w.writeheader()
                for input_url in tqdm(self.input_urls):
                    try:
                        source = self.get_url(base_url = input_url)
                        soup = self.get_soup(source)
                        w.writerow(self.keywords(soup, input_url))
                    except:
                        pass
                    self.time_sleep = None

        else:
            with open(self.data_file, self.write_mode, encoding='utf-8') as f:
                w = csv.DictWriter(f, self.column_names(), delimiter =self.csv_separator, lineterminator='\n')
                w.writeheader()
                for input_url in tqdm(self.input_urls):
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
                        source = self.get_url(base_url = newline)
                        soup = self.get_soup(source)
                        arts = self.soup_attributes(soup, *self.articles)
                        for article in arts:
                            try:
                                w.writerow(self.keywords(article, newline))
                            except:
                                pass
                        self.time_sleep = None
        f.close()
 
