text="""
In 2022 he had decided to plant some apple trees, not crazy for a farmer unless, like Mr Sawant, you live in subtropical southern India, where temperatures can hit 43C.
He bought 100 saplings, of which 80 survived. Last year each tree produced between 30 and 40 kilogrammes of fruit.
"My farm has become something of a local miracle. People travel from far-off places just to see the apple trees growing under the hot Maharashtra sun."
It's not been an unqualified success though. One problem is that the apples are not sweet enough to sell.
Mr Sawant remains enthusiastic. He's had some success selling apple tree saplings and is optimistic about future harvests.
"This is the beginning. The trees are getting acclimatised so according to me in next four to five years these trees will start bearing good, sweet apples."
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

# Download necessary NLTK resources
nltk.download('all')