# Imports
import Protests_Functions as pf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


#Variables
farleft_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Left.csv'
left_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Left.csv'
center_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Center.csv'
right_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Right.csv'
farright_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Right.csv'
dictionaryNames = ['black_indicators', 'white_indicators', 'other', 'protest_words', 'riot_words']
print(dictionaryNames)


# Frequency of the words in the categories of article
# Get the text from all the articles per political ideology
farleft_text = pf.open_file(farleft_file)
left_text = pf.open_file(left_file)
center_text = pf.open_file(center_file)
right_text = pf.open_file(right_file)
farright_text = pf.open_file(farright_file)
all_text = farleft_text + left_text + farright_text

# Plot the most frequent words per leaning
# a = pf.plot_freqWords(farleft_text, 'Most frequent far left words')
# b = pf.plot_freqWords(left_text, 'Most frequent left words')
# c = pf.plot_freqWords(center_text, 'Most frequent center words')
# d = pf.plot_freqWords(right_text, 'Most frequent right words')
# e = pf.plot_freqWords(farright_text, 'Most frequent far right words')
# f = pf.plot_freqWords(all_text, 'Most frequent words from all text')


# Find the frequency of the keywords given
all_indicators = pf.count_keywordfreq(all_text, dictionaryNames)
farleft_indicators = pf.count_keywordfreq(farleft_text, dictionaryNames)
left_indicators = pf.count_keywordfreq(left_text, dictionaryNames)
center_indicators = pf.count_keywordfreq(center_text, dictionaryNames)
right_indicators = pf.count_keywordfreq(right_text, dictionaryNames)
farright_indicators = pf.count_keywordfreq(farright_text, dictionaryNames)

# Plot the frequency of the keywords given
# g = pf.plot_freqWords(all_indicators, 'All Indicators')
# h = pf.plot_freqWords(farleft_indicators, 'Far Left Indicators')

words, frequency, leaning = [],[],[]
for word, count in farleft_indicators:
    words.append(word)
    frequency.append(count)
    leaning.append('Far Left')
for word, count in left_indicators:
    words.append(word)
    frequency.append(count)
    leaning.append('Left')
for word, count in center_indicators:
    words.append(word)
    frequency.append(count)
    leaning.append('Center')
for word, count in right_indicators:
    words.append(word)
    frequency.append(count)
    leaning.append('Right')
for word, count in farright_indicators:
    words.append(word)
    frequency.append(count)
    leaning.append('Far Right')

all_info = [words, frequency, leaning]
df = pd.DataFrame(all_info).transpose()
df.columns = ['Words', 'Frequency', 'Leaning']

sns.catplot(x='Words',y='Frequency',hue='Leaning', data=df, kind='bar')
plt.show()