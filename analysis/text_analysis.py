from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

def process_text(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.isalpha() and not token in stop_words]
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word, pos='v') for word in tokens]

def create_wordcloud(text):
    word_cloud = WordCloud(max_words=100, background_color='white').generate(text)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
