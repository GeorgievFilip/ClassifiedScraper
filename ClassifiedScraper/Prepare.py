import requests
from bs4 import BeautifulSoup
from utils import *
import csv
import backoff
from tqdm import tqdm
from datetime import datetime

class Prepare:
    format_num = 1
    page_jump = 1
    first_page = 1
    def __init__(self, input_urls, articles, pages = None, results = None,
                proxies = None, headers = None, split_results = None, split_pages = None):

        pages = None if pages is None else pages
        results = None if results is None else results
        headers = None if headers is None else headers
        proxies = None if proxies is None else proxies
        split_results = None if split_results is None else split_results
        split_pages = None if split_pages is None else split_pages

        self.input_urls = input_urls
        self.articles = articles
        self.pages = pages
        self.results = results
        self.headers = headers
        self.proxies = proxies
        self.split_results = split_results
        self.split_pages = split_pages

    # Get a requests for a given url
    @backoff.on_exception(
        backoff.expo,
        IOError,
        max_tries=3
    )
    def get_url(self, base_url):
        if self.proxies is None:
            prox = None
        else:
            prox = random_choice(self.proxies)
        if self.headers is None:
            header = None
        else:
            header = random_choice(self.headers)

        if self.format_num is None:
            return requests.get(base_url,
                    proxies ={ 
                        "http": prox,
                        "https": prox 
                        },
                        headers = { 'user_agent': header })
        else:
            return requests.get(base_url.format(self.format_num),
                    proxies = {
                        "http": prox,
                        "https": prox
                        },
                    headers = { 'user_agent': header })
    
    # Get a soup from a given source(made request)
    def get_soup(self, source):
        return BeautifulSoup(source.text, 'lxml')

    def soup_attributes(self, soup, search):
        return soup.select(search)

    def soup_attribute(self, soup, list1, tag = None):
        tag = None if tag is None else tag
        soup1 = soup.select_one(list1)
        if tag is None:
            return soup1
        elif tag is not None:
            return soup1[tag]
    
    def get_pages(self, soup = None):
        soup = None if soup is None else soup
        if isinstance(self.pages, int):
            pages = self.pages
        elif isinstance(self.pages, list):
            pages = extract_number(self.soup_attribute(soup, *self.pages).text)
        else:
            pages = 1
        return pages
    
    def get_pages_from_results(self, rez, rez_per_page):
        pages = get_round(extract_number(rez), rez_per_page)
        return pages
    
    def get_pages_urls(self, pages, base_url):
        newlines = [base_url.format(page) for page in [self.first_page] + [i*self.page_jump for i in range(self.first_page, pages+1)]]
        return newlines
        
    def get_results(self, soup):
        if self.results is None:
            results = None

        elif self.results is not None:
            if self.split_results is None:
                results = extract_number(self.soup_attribute(soup, *self.results).text)
            elif self.split_results is not None:
                string = self.soup_attribute(soup, *self.results).text
                split = self.split_results[0]
                num = self.split_results[1]
                results = extract_number(split_string_at(
                    string,
                    split,
                    num))
        return results
