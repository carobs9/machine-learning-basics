from utils import extract_text_from_pdf, save_text_to_file, word_count_clean, word_count, save_plot
from utils import unicodedata, nltk, snowball_stemmer, re

pdf_file_path = "el-amante-japones-isabel-allende.pdf"
extracted_text = extract_text_from_pdf(pdf_file_path)

output_file_path = "extracted_text.txt" 
save_text_to_file(extracted_text, output_file_path)

text_lower = extracted_text.lower()
text_normalized = unicodedata.normalize('NFKD', text_lower).encode('ascii', 'ignore').decode('utf-8')
filtered_text = re.sub('[^A-Za-z0-9\s]', ' ', text_normalized)
#filtered_text = re.sub('[^A-Za-z0-9áéíóúÁÉÍÓÚñÑüÜ\s]', ' ',text_lower)
tokens = nltk.word_tokenize(filtered_text)
tokens_no_stopwords = [word for word in tokens if word not in nltk.corpus.stopwords.words('spanish')]
stemmed_words = [snowball_stemmer.stem(word) for word in tokens_no_stopwords]


freq = nltk.FreqDist(stemmed_words) # Getting Most Common Stemmed Tokens
print('Most frequent 200 stemmed words: ', freq.most_common(200))

word_count(extracted_text)
word_count_clean(extracted_text)
word_count(stemmed_words)


# More Analysis (Lexical Dispersion, Collocations)

ntext = nltk.Text(tokens)
dispersion_plot = ntext.dispersion_plot(['tiempo', 'guerra', 'amor', 'vida', 'vejez', 'muerte'])
save_plot(dispersion_plot)
ntext.collocations(window_size=2, num=30)


# Initial Characters Analysis

for name in ('Alma', 'Ichimei', 'Nathaniel', 'Seth', 'Irina', 'Isaac', 'Lenny', 'Lillian'):
    print('{}:'.format(name), freq.get(name.lower()))

print('Done')