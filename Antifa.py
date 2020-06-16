
# Imports
import Protests_Functions as pf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Variables
farleft_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Left.csv'
left_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Left.csv'
center_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Center.csv'
right_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Right.csv'
farright_file = 'C:/Users/khahn/PycharmProjects/NLP Protests/article database/Protests Links - Far Right.csv'

# Action
farleft_text = pf.open_file(farleft_file)
left_text = pf.open_file(left_file)
center_text = pf.open_file(center_file)
right_text = pf.open_file(right_file)
farright_text = pf.open_file(farright_file)
all_text = farleft_text + left_text + farright_text

def count_givenKeyword(text, keyword):
    keywords = []
    for word in text:
        if word == keyword:
            keywords.append(keywords)
    return len(keywords)


antifaCount_FL = count_givenKeyword(farleft_text, 'antifa')
antifaCount_L = count_givenKeyword(left_text, 'antifa')
antifaCount_C = count_givenKeyword(center_text, 'antifa')
antifaCount_R = count_givenKeyword(right_text, 'antifa')
antifaCount_FR = count_givenKeyword(farright_text, 'antifa')

frequency = [antifaCount_FL, antifaCount_L, antifaCount_C, antifaCount_R, antifaCount_FR]
leaning = ['Far left', 'Left', 'Center', 'Right', 'Far Right']

all_info = [leaning, frequency]
df = pd.DataFrame(all_info).transpose()
df.columns = ['Political Leaning', 'Frequency']

plot = sns.catplot(x='Political Leaning',y='Frequency', data=df, kind='bar')
#plot.set_title('Antifa mentions by newspapers from across the political spectrum covering the BLM protests')
plt.show()
