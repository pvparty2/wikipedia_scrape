'''Wikipedia scraper context manager.'''

import requests

class UseWikiScraper:
    '''Scrape a wikipedia page given a URL to an article.'''
    
    def __init__(self, wiki_url):
        '''Initialize an instance of a scraper.'''
        self.BASE_URL = '''https://en.wikipedia.org'''
        self.wiki_url = self.BASE_URL + wiki_url


    def __enter__(self):
        try:
            self.response = requests.get(self.wiki_url)
            self.response.raise_for_status()
            return self.response
        except Exception as err:
            raise SystemExit(err.__class__, err.__traceback__, err)
        
    
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.response.close()

    

