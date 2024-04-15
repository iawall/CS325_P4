
** FROM P1 DESCRIPTION**

First, I created my repository in git, linked it to VScode, installed packages request (used to retrieve the website) and BeautifulSoup4 (used for the web scraping) to my environment

After doing this, I then pathed my VScode to the miniconda environment so that the code i run in VScode uses the packages within my conda environment.

I then created my scraping python program (step by step):
  1. program imports request and BeautifulSoup
  2. It then loops the following through 5 URLs:
    a. opens the specified file that will be written over with the scraped website
    b. The code then sends a get request to the website being scraped. If the response status code = 200, then the request was successfully retrieved. Else, it prints out the response status code of why it failed
    c. If successful, i use beautifulsoup to find all html specified under 'h1' or header 1 described html. i then write these headlines to the out file
    d. after getting all h1 headers, i then retrieve all text with the 'p' or paragraph html and write it to the out file
    e. after getting texts from a website, it then uses time.sleep() to delay the scraping for 1 second. This is     precautionary in case websited pick up bot activity.
  The program outputs after each website has been scraped.

