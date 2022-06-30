from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class TFiDF:
    vectorizer = None
    vector = None

    def __init__(self, corpus: list):
        print("Start TFiDF...")
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 1), stop_words=["english"])
        self.vector = self.vectorizer.fit_transform(corpus)
        self.words = self.vectorizer.get_feature_names_out()
        self.word_similarity_str = {}
        self.top_10_similar()

    def top_10_similar(self):
        print("Start finding top 10 similar...")
        table = cosine_similarity(self.vector.transpose(), self.vector.transpose())
        # table = cosine_similarity(self.vectorizer.transform(self.words), self.vectorizer.transform(self.words))
        word_similarity_number = {}
        for index, word in enumerate(table):
            top_10_indexes = word.argsort()[-11:-1][::-1]
            word_similarity_number[index] = top_10_indexes

        for word in word_similarity_number:
            self.word_similarity_str[self.words[word]] = list()
            for inner_word in word_similarity_number[word]:
                self.word_similarity_str[self.words[word]].append(self.words[inner_word])

    def get_top_10(self, words: list):
        output = {}
        for word in words:
            if word in self.word_similarity_str:
                output[word] = self.word_similarity_str[word]
        return output
