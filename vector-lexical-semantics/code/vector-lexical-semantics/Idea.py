from word2vec.SimpleWord2Vec import SimpleWord2Vec

if __name__ == '__main__':
    model_name = 'word2vec_genre_news_vector_size_50_window_size_10_iteration_number_1000.model'
    model = SimpleWord2Vec(f'/home/hamid/PycharmProjects/vector-lexical-semantics/word2vec/model/{model_name}')
    print()