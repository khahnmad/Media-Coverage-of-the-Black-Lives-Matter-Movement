# To do


# Imports
import Protests_Functions as pf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def count_genderfreq(text, dictionaryIndicators):
    indicators = []
    for word in text:
        if word in dictionaryIndicators:
            indicators.append(word)
    return len(indicators)

# Variables
farleft_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Left.csv'
left_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Left.csv'
center_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Center.csv'
right_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Right.csv'
farright_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Right.csv'

genderDict = {'male indicators': ['male', 'man', 'men', 'he', 'his', 'him', 'boy', 'boys'], 'female indicators':
    ['female', 'woman', 'women', 'she', 'her', 'hers', 'girl', 'girls']}
dictionaryNames = ['male indicators', 'female indicators']

# Frequency of the words in the categories of article
# Get the text from all the articles per political ideology
farleft_text = pf.open_file(farleft_file)
left_text = pf.open_file(left_file)
center_text = pf.open_file(center_file)
right_text = pf.open_file(right_file)
farright_text = pf.open_file(farright_file)
all_text = farleft_text + left_text + farright_text
print('got all the text')



all_indicatorsm = count_genderfreq(all_text, genderDict['male indicators'])
farleft_indicatorsm = count_genderfreq(farleft_text, genderDict['male indicators'])
left_indicatorsm = count_genderfreq(left_text, genderDict['male indicators'])
center_indicatorsm = count_genderfreq(center_text, genderDict['male indicators'])
right_indicatorsm = count_genderfreq(right_text, genderDict['male indicators'])
farright_indicatorsm = count_genderfreq(farright_text, genderDict['male indicators'])

all_indicatorsf = count_genderfreq(all_text, genderDict['female indicators'])
farleft_indicatorsf = count_genderfreq(farleft_text, genderDict['female indicators'])
left_indicatorsf = count_genderfreq(left_text, genderDict['female indicators'])
center_indicatorsf = count_genderfreq(center_text, genderDict['female indicators'])
right_indicatorsf = count_genderfreq(right_text, genderDict['female indicators'])
farright_indicatorsf = count_genderfreq(farright_text, genderDict['female indicators'])
print('got all the indicators')

maleFreq = [farleft_indicatorsm, left_indicatorsm, center_indicatorsm, right_indicatorsm, farright_indicatorsm]
femaleFreq = [farleft_indicatorsf, left_indicatorsf, center_indicatorsf, right_indicatorsf, farright_indicatorsf]
frequency = [farleft_indicatorsm, left_indicatorsm, center_indicatorsm, right_indicatorsm, farright_indicatorsm, farleft_indicatorsf, left_indicatorsf, center_indicatorsf, right_indicatorsf, farright_indicatorsf]
words = ['Male gender', 'Male gender', 'Male gender', 'Male gender', 'Male gender', 'Female gender', 'Female gender',
         'Female gender', 'Female gender', 'Female gender']
leaning = ['Far left', 'Left', 'Center', 'Right', 'Far Right', 'Far left', 'Left', 'Center', 'Right', 'Far Right']


# words, frequency, leaning = [],[],[]
# for word, count in farleft_indicators:
#     words.append(word)
#     frequency.append(count)
#     leaning.append('Far Left')
# for word, count in left_indicators:
#     words.append(word)
#     frequency.append(count)
#     leaning.append('Left')
# for word, count in center_indicators:
#     words.append(word)
#     frequency.append(count)
#     leaning.append('Center')
# for word, count in right_indicators:
#     words.append(word)
#     frequency.append(count)
#     leaning.append('Right')
# for word, count in farright_indicators:
#     words.append(word)
#     frequency.append(count)
#     leaning.append('Far Right')
# print('sorted all the words')


all_info = [words, frequency, leaning]
df = pd.DataFrame(all_info).transpose()
df.columns = ['Words', 'Frequency', 'Political Leaning']
print('made the dataframe')

plot = sns.catplot(x='Words',y='Frequency',hue='Political Leaning', data=df, kind='bar')
#plot.set_title('Frequency of Gender Words from Newspapers across the Political Spectrum Covering the Black Lives Matter Protests')
plt.show()
