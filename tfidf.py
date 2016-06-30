from math import log

def tf(term, document):
    count = 0
    for word in document:
        if word == term:
            count += 1
    return count

def idf(term, document_set):
    num_docs_containing_term = 0
    for document in document_set:
        if term in document:
            num_docs_containing_term += 1
    return log(len(document_set)/num_docs_containing_term)
