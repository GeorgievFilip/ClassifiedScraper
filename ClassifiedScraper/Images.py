from Prepare import *
import re

'''Used to scrape images from a webpage (either all of them or from a selection).
   NOTE: By default the images will be scraped in a 'Images' folder.
   To change this change the "image_folder" at the instance you are crating.
   See "Image examples.py" in the 'tests' folder.'''
class Images(Prepare):
    format_num = 1
    img_folder = os.getcwd() + '\\Images\\'
    time_sleep = None
    
    def __init__(self, input_urls, articles = None, pages = None, results = None, proxies = None, headers = None,
    split_results = None, split_pages = None, sess = None, cloudscraper = False):
        super().__init__(input_urls, articles)

        articles = None if articles is None else articles
        pages = None if pages is None else pages
        results = None if results is None else results
        proxies = None if proxies is None else proxies
        headers = None if headers is None else headers
        split_results = None if split_results is None else split_results
        split_pages = None if split_pages is None else split_pages
        sess = None if sess is None else sess
        cloudscraper = False if cloudscraper is None else cloudscraper

        self.input_urls = input_urls
        self.articles = articles
        self.pages = pages
        self.results = results
        self.proxies = proxies
        self.headers = headers
        self.split_results = split_results
        self.split_pages = split_pages
        self.sess = sess
        self.cloudscraper = cloudscraper

    # Used to detect the format of an image in an image url
    def image_format(self, img_url):
        img_formats = re.compile('.jpg|.jpeg|.png|.svg|.gif|.webm', re.IGNORECASE)
        format_search = re.search(img_formats, img_url)
        if format_search:
            return format_search.group(0)
        else:
            return
    
    def find_img_tag(self, soup_element):
        if not soup_element.select_one('img'):
            soup_element = soup_element
        else:
            soup_element = soup_element.select_one('img')
        return soup_element

    ''' Once selecting a soup element/ article, extract the image url and properly format it,
        meaning adding "http://" when it's missing and/ or the webpage url, removing unnecessary characters,
        as well as getting the url of the highest resolution version of the image. '''
    def get_image_url(self, soup_element):
        soup_element = self.find_img_tag(soup_element)
        try:
            img_url = soup_element['srcset'].split(',')[0].replace('/thumb', '')
        except:
            img_url = soup_element['src']

        img_url = self.get_parent_url(img_url)
        format_search = self.image_format(img_url)
        #?
        if format_search:
            img_url = img_url.split(format_search)[0] + format_search
        return img_url

    # Extract the name of the image file
    def get_image_name(self, img_url):
        format_search = self.image_format(img_url)
        if format_search:
            img = os.path.basename(img_url).split(format_search)[0] + format_search
        else:
            img = None
        return img

    def get_images(self):
        print("Collecting images")
        sess = self.get_sess()
        make_directory(self.img_folder)
        count = 0
        #Download every image on website
        if not self.results and not self.pages:
            for input_url in self.input_urls:
                if self.image_format(input_url) is not None:
                    try:
                        with open(self.img_folder + self.get_image_name(input_url), 'wb') as f:
                            f.write(self.get_url(input_url, sess).content)
                        count += 1
                    except:
                        pass
                else:
                    source = self.get_url(input_url, sess)
                    soup = self.get_soup(source)
                    if self.articles is not None:
                        arts = self.soup_attributes(soup, *self.articles)
                    else:
                        arts = self.soup_attributes(soup, 'img')
                    for article in arts:
                        img_url = self.get_image_url(article)
                        try:
                            with open(self.img_folder + self.get_image_name(img_url), 'wb') as f:
                                f.write(self.get_url(img_url, sess).content)
                            count += 1
                        except:
                            pass

                self.time_sleep
        else:
            for input_url in self.input_urls:
                source = self.get_url(input_url, sess)
                soup = self.get_soup(source)
                arts = self.soup_attributes(soup, *self.articles)
                results = self.get_results(soup)
                try:
                    pages = self.get_pages_from_results(results, len(arts)) if self.pages is None else self.get_pages(soup)
                except:
                    pages = 1
                newlines = self.get_pages_urls(pages, input_url)
                for newline in newlines:
                    source = self.get_url(newline, sess)
                    soup = self.get_soup(source)
                    arts = self.soup_attributes(soup, *self.articles)
                    for article in arts:
                        try:
                            img_url = self.get_image_url(article)
                            with open(self.img_folder + self.get_image_name(img_url), 'wb') as f:
                                f.write(self.get_url(img_url, sess).content)
                            count += 1
                        except:
                            pass
                    self.time_sleep
        print("Number of images collected: " + str(count))
        print("")
        try:
            f.close()
        except:
            pass
