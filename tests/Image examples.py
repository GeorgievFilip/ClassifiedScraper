import sys
sys.path.append('../ClassifiedScraper/')

from Articles import Articles
from Images import Images
from utils import *

# The following 3 examples show extracting images from a certain section from different websites.
# XKCD (first 10 pages)
B = Images(
    input_urls = ['https://xkcd.com/{}/'],
    pages = 10,
    articles = ['#comic']
)
B.img_folder = '../Data/Images/xkcd.com/'
B.get_images()


# wow.gamepedia.com
B = Images(
    input_urls =  ['https://wow.gamepedia.com/Kel%27Thuzad'],
    articles = ['li.gallerybox']
)
B.img_folder = '../Data/Images/wow.gamepedia.com/'
B.get_images()


# Wikipedia
B = Images(
    input_urls = ['https://en.wikipedia.org/wiki/Skopje'],
    articles = ['ul.gallery:nth-child(65) li.gallerybox']
)
B.img_folder = '../Data/Images/wiki/'
B.get_images()

# For scraping every image on the website, don't specify articles
# wow.gamepedia.com
B = Images(
    input_urls = ['https://wow.gamepedia.com/Kel%27Thuzad']
)
B.img_folder = '../Data/Images/wow.gamepedia.com (all images)/'
B.get_images()