import re
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from stop_list import closed_class_stop_words
import itertools

s = SnowballStemmer("english")

# Stripping cran.qry for the (ID, query) tuple
query_file = open('cran.qry').read()
queries = query_file.split('I')
queries.pop(0)
queries = [tuple(q.split('W')) for q in queries]
queries = [(re.findall(r'\d{3}', i), word_tokenize(s.stem(q))) for (i,q) in queries]
queries = [(i, [w for w in q if w not in closed_class_stop_words]) for (i, q) in queries]
# Strip punctuation later

# Set of all unique words in queries to make dictionary for IDF score
all_queries = [q for (i,q) in queries]
all_queries = set(itertools.chain.from_iterable(all_queries))

# Stripping cran.all.1400 for abstracts