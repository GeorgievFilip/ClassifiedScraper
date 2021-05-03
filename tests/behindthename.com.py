import sys
sys.path.append('../ClassifiedScraper/')

from Data import Data

A = Data(input_urls = [
    'https://www.behindthename.com/names/gender/masculine/{}',
    'https://www.behindthename.com/names/gender/feminine/{}',
    'https://www.behindthename.com/names/gender/unisex/{}'],
    results = ['div.pgblurb'],
    split_results = ['result', 0],
    articles = ['div.browsename'],
    Name = ['span.listname'],
    Gender = ['span.listgender'],
    Origin = ['span.listusage'])
A.data_file = '../Data/behindthename.com/behindthename.com.csv'
A.get_data()
