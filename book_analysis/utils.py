
import numpy as np
import matplotlib.pyplot as plt
import PyPDF2
import regex as re
import unicodedata
import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk import WordNetLemmatizer
# Other imports
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from matplotlib import pyplot as plt
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
snowball_stemmer = SnowballStemmer('spanish')


# functions
def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        num_pages = len(pdf_reader.pages)

        # Loop through all pages and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


def save_text_to_file(text, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)


def word_count(text):
  if type(text) == list:
        text = ' '.join(text)
  words = text.split()
  # Create an empty dictionary
  d = dict()

  # Iterate over each word in line
  for word in words:
      word = word.lower()
        # Check if the word is already in dictionary
      if word in d:
            # Increment count of word by 1
          d[word] = d[word] + 1
      else:
            # Add the word to dictionary with count 1
          d[word] = 1
  # Print the contents of dictionary
  sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)
  #return(sorted_d)

  # Using zip function and Unpacking the values
  word_used, occurrence = zip(*sorted_d)

# printing the scatter values
#print(word_used)
#print(occurrence)

  plt.scatter(word_used[0:50], occurrence[0:50])
  plt.xticks(rotation = 90)
  plt.title('Top 50 Used Words and Occurence')
  plt.show()


def word_count_clean(text):
# Tokenize the text into words
  words = word_tokenize(text.lower())
# Remove stopwords
  stop_words = nltk.corpus.stopwords.words('spanish')
  filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

# Create an empty dictionary
  d = dict()
# Iterate over each word in line
  for word in filtered_words:
      word = word.lower()
        # Check if the word is already in dictionary
      if word in d:
            # Increment count of word by 1
          d[word] = d[word] + 1
      else:
            # Add the word to dictionary with count 1
          d[word] = 1
  # Print the contents of dictionary
  sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)
  #return(sorted_d)

  # Using zip function and Unpacking the values
  word_used, occurrence = zip(*sorted_d)

# printing the scatter values
#print(word_used)
#print(occurrence)

  plt.scatter(word_used[0:50], occurrence[0:50])
  plt.xticks(rotation = 90)
  plt.title('Top 50 Used Words and Occurence (No Stopwords)')
  plt.show()