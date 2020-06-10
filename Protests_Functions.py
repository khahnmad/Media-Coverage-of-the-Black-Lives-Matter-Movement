# Imports
import glob
import os
import csv
from bs4 import BeautifulSoup
import requests
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from cucco import Cucco
import collections
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt


# Variables
variablesDict = {'black_indicators': ['black', 'african american'], 'white_indicators': ['white', 'caucasian'],
                 'other' : ['police', 'brutality', 'antifa'], 'protest_words': ['peaceful', 'protestors', 'protests', 'protestor',
                'protest'], 'riot_words': ['violent', 'violence', 'riot', 'riots', 'rioters','looting','rioting']}


# Functions
def get_allArticles(directory):
    csvfiles = glob.glob(os.path.join(directory, '*.csv'))  # get the files in that folder
    csvcontent, csvColumns, columnsList, urlsList = [], [], [], []
    for elt in csvfiles:
        with open(elt, 'r', encoding='utf-8') as f:
            csv_f = csv.reader(f)
            csvcontent.append([x for x in csv_f])
    # clean the articles and put them into one list
    for csvfile in csvcontent:  # reads the columns for each of the csv files
        for column in csvfile:
            csvColumns.append(column)
    for elt in csvColumns:  # makes each column a string in one list
        for i in elt:
            columnsList.append(i)
    while '' in columnsList:  # remove empty strings
        columnsList.remove('')
    totalElements = len(columnsList)
    for elt in columnsList:  # remove content that is not a url and remove repeated urls
        if elt.startswith('http') and elt not in urlsList:
            urlsList.append(elt)
    totalUnrepeatedElements = len(urlsList)
    return urlsList

# Get website text
# input: single url
# output: list of lists which are tokenized sentences
# problems: with the test, has a bunch of empty lists at the end; not clean
def get_page_sentences(url):
    paragraphs_normalized = []
    normEsp = Cucco()
    norms = ['replace_punctuation', 'remove_extra_whitespaces']
    soup = BeautifulSoup(requests.get(url).text, "lxml")
    paragraphs = soup.find_all('p')
    stripped_paragraph = [tag.get_text().strip() for tag in paragraphs]
    for sentence in stripped_paragraph:
        paragraphs_normalized.append(normEsp.normalize(sentence, norms))
    return paragraphs_normalized


# Tokenize
# inputs: list of sentences as strings
# return: list of list of sentences which are tokenized
def get_token_sentences(sentence_list):
    return [word_tokenize(word) for word in sentence_list]

def clean_text(one_list_sentences):
    new_stopwords = set(stopwords.words('english'))
    all_text, lowered_sentences = [], []
    for sentence in one_list_sentences: # make all letters lowercase
        lowered_sentences.append(sentence.lower())
    token_sentences = get_token_sentences(lowered_sentences) # tokenize sentences
    for sentence in token_sentences:
        for word in sentence:
            if word not in new_stopwords:
                all_text.append(word)
    return all_text

# Plot the frequent related words
# input: list of sentences, title of the plot
# output: plot of the most frequent related words
def plot_freqWords(text, title):
    counter = Counter(text)
    most = counter.most_common()
    x, y = [], []
    for word, count in most[:30]:
        x.append(word)
        y.append(count)
    sns.barplot(x=y, y=x, color='cyan').set_title(title)
    plt.show()


def open_file(filename):
    # open the file
    csvfile, csvColumns, columnsList, urlsList = [], [], [], []
    with open(filename, 'r', encoding='utf-8') as f:
        csv_f = csv.reader(f)
        csvfile.append([x for x in csv_f])
    for column in csvfile:
            csvColumns.append(column)
    for elt in csvColumns:  # makes each column a string in one list
        for i in elt:
            columnsList.append(i)
    while '' in columnsList:  # remove empty strings
        columnsList.remove('')
    totalElements = len(columnsList)
    for elt in columnsList:  # remove content that is not a url and remove repeated urls
        for i in elt:
            if i.startswith('http') and i not in urlsList:
                urlsList.append(i)
    totalUnrepeatedElements = len(urlsList)
    listsOfSentences = []
    for url in urlsList:
        text = get_page_sentences(url)  # gets stripped p tags from each url
        listsOfSentences.append(text)
    one_list_sentences = []
    for elt in listsOfSentences:  # make it just one list of all the strings
        for i in elt:
            one_list_sentences.append(i)
    all_text = clean_text(one_list_sentences)
    return all_text

def count_keywordfreq(text, dictionaryNames):
    indicators = []
    for word in text:
        for indicator in dictionaryNames:
            if word in variablesDict[indicator]:
                indicators.append(word)
    counter = Counter(indicators)
    most = counter.most_common()
    return most[:8]
