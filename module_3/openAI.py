import os
import requests
from openai import OpenAIError, OpenAI # used to contact openAI

currentDir = os.path.dirname(os.path.abspath(__file__)) # get current directory
parentDir = os.path.dirname(os.path.join(currentDir, os.pardir, os.pardir)) # get parent directory of the current file
dataDir = os.path.dirname(os.path.join(parentDir, "Data", "processed")) # get data folder
processedDir = os.path.join(dataDir, 'processed') # gets the processed folder
summaryDir = os.path.join(dataDir, 'summary') # gets the summary folder

if not os.path.exists(summaryDir): # if the summary folder does not exist, create one
    os.makedirs(summaryDir)

### CHANGE TO YOUR CREATED API KEY ###
api_key = 'YOUR API KEY'

client = OpenAI(api_key=api_key)

def query_openai(prompt): # function to return the openAI models response with the given prompt
    chat_completion = client.chat.completions.create( # create chat with openAI
        messages=[
            {
                "role": "user",
                "content": prompt, # grabs the prompt
            }
        ],
        model="gpt-3.5-turbo", # the model being used
        temperature=0.3
    )
    return chat_completion.choices[0].message.content.strip() # gets and returns the AI send back, specifically the content

def summarize_article(article, outputFile,i):
    prompt = f"Include a Spicy title followed by a colon. Then create a space between the title and summarize the article only using 50 words: \n{article}." # the prompt used
    summary = query_openai(prompt) # uses prompt to get summary

    summaryFile = os.path.join(outputFile, f"summary{i}.txt") # path to summary file
    with open(summaryFile, 'w', encoding='utf-8') as file:
        summaryPart = summary.split(". ") # used for readability
        for part in summaryPart:
           # file.write(summary)
           file.write(part.strip() + ".\n") # adds newline after each . or sentence
    return summaryFile

def process_articles_from_folder(folder_path):
    summaries = [] # list that will store the location of summaries of each website scraped
    
    # filenames sorts the folder path. Without this, article10 would be before article2 due to the number in that specific spot
    filenames = sorted(os.listdir(folder_path), key=lambda x: int(x.split('.')[0].split('e')[-1]))

    for i, filename in enumerate(filenames,1): # iterates over each file in the path
        file_path = os.path.join(folder_path, filename)

       # if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            article = file.read().strip() # reads the scraped article
        summary_file = summarize_article(article, summaryDir,i) # generates the summary of the article
    
        summaries.append(summary_file) # add it to the list
    return summaries

def main():
    articles_folder = processedDir # gets the articles in the folder
    summaries = process_articles_from_folder(articles_folder) # starts the process

    for i, summary in enumerate(summaries, 1):
        print(f"Summary {i} written to {summary}") # says where the summaries were written to

if __name__ == "__main__":
    main()
