'''
this file is mostly just for running the program. this is where URLs are put in to be scraped
follows SRP due to being able to alter the URLs and it not interfering with the class Scrapper or the scrap.py functions

'''

import os       
import sys


currentDir = os.path.dirname(os.path.abspath(__file__)) # get current directory
parentDir = os.path.dirname(os.path.join(currentDir, os.pardir, os.pardir)) # get parent directory of the current file

from module_2.scrap import main # gets scrap.py
from module_3.openAI import main as openAImain

if __name__ == "__main__":
    # Define list of URLs to scrape
    urls = ["https://www.cnn.com/2022/03/26/business/amazon-coupons-shopping-psychology/index.html"]

    scrapedData = main(urls) # calls scrap.py, used to scrape website articles
    print("Starting OpenAI process")
    aiData = openAImain() # calls openAI.py, used to summarize articles
    print("Complete")
