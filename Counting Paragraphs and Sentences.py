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
import Protests_Functions as pf


# Functions
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
    print('Number of URls:',totalUnrepeatedElements)
    listsOfSentences = []
    numberOfParagraphs = []
    for url in urlsList:
        text = pf.get_page_sentences(url)  # gets stripped p tags from each url
        listsOfSentences.append(text)
    one_list_sentences = []
    for elt in listsOfSentences:  # make it just one list of all the strings of sentences
        for i in elt:
            one_list_sentences.append(i)
    tokenizedList = pf.get_token_sentences(one_list_sentences) # make each word a token
    wordsList = []
    for item in tokenizedList: 
        for token in item:
            wordsList.append(token) # list of all the words from the articles in this category
    return len(one_list_sentences), len(wordsList)


# Variables
# each of these references a csv file with 40 urls from different newspapers 
farleft_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Left.csv'
left_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Left.csv'
center_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Center.csv'
right_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Right.csv'
farright_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Right.csv'


# Action 
farleft_sentences, farleft_words = open_file(farleft_file) #get the number of sentences, words in all the articles in this category
left_sentences, left_words = open_file(left_file)
center_sentences, center_words = open_file(center_file)
right_sentences, right_words = open_file(right_file)
farright_sentences, farright_words = open_file(farright_file)

print('Political leaning', '# of sentences','  # of words') # print  chart of the number of sentences, words per category
print('         Far Left', '    ', farleft_sentences,'    ', farleft_words)
print('             Left','    ', left_sentences,'    ', left_words)
print('           Center', '    ',center_sentences,'    ', center_words)
print('            Right','    ',right_sentences,'    ', right_words)
print('        Far Right', '    ',farright_sentences, '    ', farright_words)

