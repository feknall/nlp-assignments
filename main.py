import similarity
from similarity import Similarity

if __name__ == '__main__':
    similarity = Similarity(10)
    similarity.find_top_5_most_similar_birkbeck_wordnet([1, 5, 10])
    # similarity.load_data()
    # misspelled_word_list = read_list_of_misspelled_words()
    # for misspelled_word in misspelled_word_list:
