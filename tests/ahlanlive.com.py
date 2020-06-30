import sys
sys.path.append('../ClassifiedScraper/')

from Articles import Articles
from Data import Data
from utils import txt_read


A = Data(
    input_urls = [
        'https://www.ahlanlive.com/star-stories/celebrities/a-z'
    ],
    articles = ['li[class*="views-row views-row-"]'],
    Name = ['span.field-content a']
)
A.data_file = '../Data/ahlanlive.com/ahlanlive.com.csv'
A.get_data()