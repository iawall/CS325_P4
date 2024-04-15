
# Project 3: Simplifying LLM API Account Creation with OpenAI

## Creating an OpenAI account
Creating an LLM API account is quite simple. For this, I used OpenAI.

 ### https://platform.openai.com/apps

You can sign up using an email account. If you create an account, you have 3 months to use free tokens, however if you go past this then you have to purchase tokens. After account creation, you can create a key.

## How to create a key
- After logging in, Choose the "API" option. This will take you to the documentation page. 
- On the right side of the dashboard click "API keys" then "Create new secret key" name the key and set the permissions to "All". This will then give you a one-time look at the key, so you will want to store the key somewhere safe. You will use this key in your program to make prompts. 
 - You can navigate to the "Usage" section on the dashboard to see how much money you are using when making these prompt calls with the tokens. Different models have different limits to how many tokens you can use a minute.


A key gives you access to prompt AI using tokens (not enough tokens will result in error code 429). This key should only be used where it's necessary and should not be exposed to the browser or client-side code for security of the account. Open AI may automatically disable the key if they detect a leak.

Using the key to make a call to the API is explained in the code, but explained here: 
- In Summary, in the code you write:
    - What AI model you want to use
    - The prompt that the model will get
    - The temperature (or variation) of how the model response to the prompt

To make calls to the model, you need to import openai and some of its features, this requires the yaml file to be updated with the openai package.

Right now it is set up to where the URLs are hardcoded in the run file, I could not update it in this time but hope to update it by next project.

## For the user:
- How to test this code
    - go to openAI.py
    - Where it says "YOUR API KEY" remove and paste with your API key
    - make sure to run "run.py" when testing new sites being scraped

#### Note:
- Some articles do not give the exact specifications asked for
- Articles that are not scrapable will go unnoticed in the summary files
- Scraping and prompting OpenAI takes some time (approximately 40 seconds) due to the list format used
- Summaries generate new line by ".", so the use of "Mr.", "Mrs.", etc. may cause a newline to happen