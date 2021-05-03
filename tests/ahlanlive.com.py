import sys
sys.path.append('../ClassifiedScraper/')

from Data import Data

# cloudscraper example
A = Data(
    input_urls = [
        'https://www.ahlanlive.com/star-stories/celebrities/a-z'
    ],
    articles = ['li.views-row.views-row'],
    cloudscraper=True,
    Name = ['span.field-content a']
)
A.data_file = '../Data/ahlanlive.com/ahlanlive.com.csv'
A.get_data()
