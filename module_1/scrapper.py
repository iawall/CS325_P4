'''
The code follows similarly to the code in part 1, it takes in a list of the URLs
and scrapes the data from each one using requests for HTTPS requests and bs4 for extracting data.

The time.sleep() function is there as a precautionary measure to not make requests in very short periods
after it iterates through the websites, it returns the data.

This follows Single Responsibility Principle due to this class having a single responsibility 
which is to scrape data from the sites given. This can be modified without changing other files
'''
import requests
from bs4 import BeautifulSoup
import time

class Scrapper:

    @staticmethod
    def scrape(urls): 
        scrapeData = []
        for i, url in enumerate(urls, start = 1): # through each url
            response = requests.get(url) # get request
            if response.status_code == 200: # successful request
                soup = BeautifulSoup(response.text, 'html.parser')
                headline_text = [headline.text for headline in soup.find_all('h1')] # get headlines
                paragraph_text = [paragraph.text for paragraph in soup.find_all('p')] # get paragraphs
                scrapeData.append({'headlines': headline_text, 'paragraphs': paragraph_text}) # appends to scrapeData
                time.sleep(1)
            else:
                print(f"Failed to retrieve the page {url}. Status code: {response.status_code}") # return url and status code problem
        return scrapeData
