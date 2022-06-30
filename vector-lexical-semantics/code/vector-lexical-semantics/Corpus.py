import nltk
from nltk.corpus import brown
import re

class Corpus:
    regex_pattern = "[A-Za-z]"
    pattern = re.compile(regex_pattern)

    def news(self):
        sentences = list()
        for sentence in brown.sents(categories=['news']):
            sentences.append(nltk.Text(sentence).name)
        return sentences

    def news_words(self):
        return brown.sents(categories=['news'])

    def news_stat(self):
        print(len(self.news()))

    def romance(self):
        sentences = list()
        for sentence in brown.sents(categories=['romance']):
            sentences.append(nltk.Text(sentence).name)
        return sentences

    def romance_words(self):
        return brown.sents(categories=['romance'])

    def romance_stat(self):
        print(len(self.romance()))


if __name__ == '__main__':
    corpus = Corpus()
    corpus.news_stat()
    corpus.romance_stat()