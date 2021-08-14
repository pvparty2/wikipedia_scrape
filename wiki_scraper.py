'''
    This project was obtained from: 
    https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/
'''

import requests
from bs4 import BeautifulSoup
import random

from scraper_cm import UseWikiScraper


def wiki_scraper(wiki_url='/wiki/') -> None:
    '''Endlessly scrape wikipedia articles.'''

    # Use wiki scraper context manager.
    with UseWikiScraper(wiki_url) as response:
        article_content = response.content

    # Parse the HTML content with soup
    soup = BeautifulSoup(article_content, 'html.parser')
    
    # Get the name of the current article
    title = soup.find(id='firstHeading')
    print(title.string)

    # Find all the URLs in the body of the current article
    all_urls = soup.find(id='bodyContent').find_all('a', href=True)
    
    # Find all wiki urls
    wiki_urls = [a['href'] for a in all_urls if a['href'].startswith('/wiki/')]
    assert wiki_urls, 'There are no URLs.'
    
    # Randomly choose new wiki article
    new_wiki_url = random.choice(wiki_urls)

    # Confirm user wants to proceed.
    if input('Type "Y" to continue. Any key to exit.').lower() == 'y':
        wiki_scraper(new_wiki_url)


if __name__ == '__main__':
    wiki_scraper('dodo')
    
    