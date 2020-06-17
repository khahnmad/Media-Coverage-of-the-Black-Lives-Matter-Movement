# Media Coverage of the Black Lives Matter Movement

In the wake of the Black Lives Matter (BLM) protests emerging internationally following the murder of George Floyd, I was interested to see how political leaning influenced different newspapers’ coverage of the topic.

Based on [AllSides’ Media Bias Ratings](https://www.allsides.com/media-bias/media-bias-chart), I sorted 200 articles from 36 newspapers into five categories: far left, left, center, right, and far right. I retrieved the articles based on recent results from the search word “protests” in early- to mid-June. To see the full write-up, check out my [article](https://medium.com/@khahn.madole/police-antifa-and-gender-word-frequency-analysis-of-the-coverage-of-blacklivesmatter-protests-1dbe20a03700) on Medium. 


## Protests Functions 

This file has contains functions that are referenced in other codes. It uses the following packages: glob, os, csv, BeautifulSoup, requests, time, nltk, cucco, collections, seaborn, and matplotlib.


## Counting Paragraphs and Sentences 

In this code, I access the text from each of the urls and count how many sentences and words there are in each category. 


## Counting Keywords

In Counting Keywords, I scrape the text from the 200 urls and then 1) plot the frequency of words for each of the five political leaning cateogries and 2) plot the top eight most frequent words from each political category in one chart. 



## Antifa

This file counts the frequency of the word "antifa" in each political leaning category and then plots the results. 



## Counting Gender

Given the urls for each political leaning cateogry and a dictionary of male and female gender nouns and pronouns, this code counts the presecence of male and female gender words per political leaning category. Then, it plots the results. 

