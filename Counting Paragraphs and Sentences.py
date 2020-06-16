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

def get_token_sentences(sentence_list):
    return [word_tokenize(word) for word in sentence_list]

def clean_text(one_list_sentences):
    new_stopwords = set(stopwords.words('english'))
    all_text, lowered_sentences = [], []

    #for st in one_list_sentences:
    #    st.replace("’", "")
    one_list_sentences = [st.replace("’", "") for st in one_list_sentences]
    one_list_sentences = [st.replace('“', '') for st in one_list_sentences]
    one_list_sentences = [st.replace('”', '') for st in one_list_sentences]
    for sentence in one_list_sentences: # make all letters lowercase
        lowered_sentences.append(sentence.lower())
    token_sentences = get_token_sentences(lowered_sentences) # tokenize sentences
    for sentence in token_sentences:
        for word in sentence:
            if word not in new_stopwords:
                all_text.append(word)
    return all_text

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
        text = get_page_sentences(url)  # gets stripped p tags from each url
        listsOfSentences.append(text)
    one_list_sentences = []
    for elt in listsOfSentences:  # make it just one list of all the strings
        for i in elt:
            one_list_sentences.append(i)
    # all_text = clean_text(one_list_sentences)
    tokenizedList = get_token_sentences(one_list_sentences)
    wordsList = []
    for item in tokenizedList:
        for token in item:
            wordsList.append(token)
    return len(one_list_sentences), len(wordsList)

def plot_freqWords(text, title):
    counter = Counter(text)
    most = counter.most_common()
    print(most[:5])
    x, y = [], []
    for word, count in most[:10]:
        x.append(word)
        y.append(count)
    sns.barplot(x=y, y=x, color='cyan').set_title(title)
    plt.show()


farleft_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Left.csv'
left_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Left.csv'
center_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Center.csv'
right_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Right.csv'
farright_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Right.csv'


farleft_sentences, farleft_words = open_file(farleft_file)
left_sentences, left_words = open_file(left_file)
center_sentences, center_words = open_file(center_file)
right_sentences, right_words = open_file(right_file)
farright_sentences, farright_words = open_file(farright_file)

print('Political leaning', '# of sentences','  # of words')
print('         Far Left', '    ', farleft_sentences,'    ', farleft_words)
print('             Left','    ', left_sentences,'    ', left_words)
print('           Center', '    ',center_sentences,'    ', center_words)
print('            Right','    ',right_sentences,'    ', right_words)
print('        Far Right', '    ',farright_sentences, '    ', farright_words)

#
# sns.barplot(x=y, y=x, color='cyan').set_title(title)
# plt.show()
#
#
# all_info = [words, frequency, leaning]
# df = pd.DataFrame(all_info).transpose()
# df.columns = ['Words', 'Frequency', 'Political Leaning']
#
# plot = sns.catplot(x='Words',y='Frequency',hue='Political Leaning', data=df, kind='bar')
# # plot.set_title('Frequency of Key Words from Newspapers across the Political Spectrum Covering the Black Lives Matter Protests')
# plt.show()