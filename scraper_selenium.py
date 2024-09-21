from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

def scrape_website_info(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        
        # Wait for the main content to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        
        title = soup.title.get_text() if soup.title else 'No title found'
        paragraphs = soup.find_all(['p', 'div'], text=True)
        content = " ".join([para.get_text() for para in paragraphs if para.get_text()])
        
        return {
            'title': title,
            'content': content
        }
    
    except Exception as e:
        driver.quit()
        return {
            'title': 'Error',
            'content': str(e)
        }

def save_to_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    url = input("Enter the URL of a website to scrape information from: ")
    scraped_data = scrape_website_info(url)
    save_to_json(scraped_data)
    print(f"Data scraped and saved successfully from {url}!")

if __name__ == "__main__":
    main()
