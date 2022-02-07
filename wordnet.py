from nltk.corpus import wordnet


# import nltk
# nltk.download('wordnet')

def get_wordnet_words():
    return list(wordnet.words())


if __name__ == "__main__":
    x = get_wordnet_words()
    print(x[:10])