import sys
sys.path.append('../ClassifiedScraper/')

from Data import Data
import random
from time import sleep

A = Data(
    input_urls = ['https://www.imdb.com/search/title/?genres=adventure&start={}&ref_=adv_nxt'],
    pages = 10,
    articles = ['div.lister-item.mode-advanced'],
    Title = ['h3.lister-item-header a'],
    Year = ['h3.lister-item-header span.lister-item-year.text-muted.unbold'],
    Certificate = ['p.text-muted span.certificate'],
    Runtime = ['span.runtime'],
    Genre = ['span.genre'],
    Description = ['div:nth-child(3) > p:nth-child(4)'],
    Rating = ['div.inline-block.ratings-imdb-rating strong']
    )
A.page_jump = 50
A.first_page = 1
A.time_sleep = sleep(random.uniform(0.1, 1.9))
A.data_file = '../Data/imdb.com/imdb.com.csv'
A.get_data()
