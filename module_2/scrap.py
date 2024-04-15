'''
scrap.py focuses on getting the right paths for the data to be written to:
If Data folder is not created, it will create it and then write data to its respective place
scrapper.py is imported here to make use of it's scraping, while os and sys deals with the system
This module also follows SRP due to dealing with the location of Urls, changing this module would not interfere with
class Scrapper or vice versa
'''
import os       
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) # grabs the parent directory path of the file
sys.path.append(parent_dir) # add to the system path

from module_1.scrapper import Scrapper # imports scrapper class

def main(urls):

    currentDir = os.path.dirname(os.path.abspath(__file__)) # get current directory
    parentDir = os.path.dirname(os.path.join(currentDir, os.pardir, os.pardir)) # get parent directory of the current file
    dataDir = os.path.join(parentDir, 'Data') # creates data directory

    if not os.path.exists(dataDir): # create Data folder if not exist
        os.makedirs(dataDir)
    rawDir = os.path.join(dataDir, 'raw') # creates raw folder
    if not os.path.exists(rawDir): # create raw directory if not exist
        os.makedirs(rawDir)
    processedDir = os.path.join(dataDir, 'processed') # create processed folder
    if not os.path.exists(processedDir):  # create process if not exist
        os.makedirs(processedDir)

    scrapData = Scrapper.scrape(urls) # scrapes data in the URL list using the class

    for i, data in enumerate(scrapData, start=1): # loops through the scraped data
        #print("in scrap.py for loop")
        filename = os.path.join(processedDir, f"article{i}.txt") # make filename
        with open(filename, 'w', encoding="utf-8") as file: # to write
            file.write("Headlines:\n") # writes the headlines
            file.write("\n".join(data['headlines']) + "\n")
            file.write("Paragraphs:\n") # writes the paragraphs
            file.write("\n".join(data['paragraphs']) + "\n")
        print("Raw data stored in Data/raw directory.") # prints where the data is stored

if __name__ == "__main__":
    main()