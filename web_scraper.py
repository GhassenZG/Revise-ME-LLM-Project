import requests
from bs4 import BeautifulSoup

def scrape_website_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title = soup.title.string if soup.title else 'No title found'

        # Extract text content from paragraphs
        paragraphs = soup.find_all('p')
        content = ' '.join([para.get_text() for para in paragraphs])

        return {
            'title': title,
            'content': content
        }
    except Exception as e:
        return {
            'title': 'Error',
            'content': f"Error scraping the website: {str(e)}"
        }
