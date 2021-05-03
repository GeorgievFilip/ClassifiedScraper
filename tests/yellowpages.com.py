import sys
sys.path.append('../ClassifiedScraper/')

from Articles import Articles
from Data import Data
from utils import txt_read

# Retrieve url links so scrape
A = Articles(
    input_urls = ['https://www.yellowpages.com/new-york-ny/restaurants?page={}'],
    articles = ['div.result'],
    pages = 5,
    headers = txt_read('user agents.txt')
)
A.txt_file = '../Data/yellowpages.com/articles.com.txt'
A.get_articles()

# Scrape the urls
B = Data(
    input_urls = txt_read(A.txt_file),
    headers = txt_read('user agents.txt'),
    company_name = ['.sales-info > h1:nth-child(1)'],
    city = ['.breadcrumb > li:nth-child(3) > a:nth-child(1) > span:nth-child(1)'],
    company_address = ['.address'],
    company_category = ['.breadcrumb > li:nth-child(5) > a:nth-child(1) > span:nth-child(1)']
)
B.data_file = '../Data/yellowpages.com/yellowpages.com.csv'
B.get_data()
