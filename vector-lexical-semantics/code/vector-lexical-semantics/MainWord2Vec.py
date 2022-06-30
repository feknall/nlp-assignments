import numpy

from SimLex import SimLex
from evaluate import Evaluate
from word2vec.SimpleWord2Vec import SimpleWord2Vec

if __name__ == '__main__':
    news_models = ['word2vec_genre_news_vector_size_10_window_size_1_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_50_window_size_1_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_100_window_size_1_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_300_window_size_1_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_10_window_size_2_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_50_window_size_2_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_100_window_size_2_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_300_window_size_2_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_10_window_size_5_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_50_window_size_5_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_100_window_size_5_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_300_window_size_5_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_10_window_size_10_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_50_window_size_10_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_100_window_size_10_iteration_number_1000.model',
              'word2vec_genre_news_vector_size_300_window_size_10_iteration_number_1000.model']

    romance_models = ['word2vec_genre_romance_vector_size_10_window_size_1_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_50_window_size_1_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_100_window_size_1_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_300_window_size_1_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_10_window_size_2_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_50_window_size_2_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_100_window_size_2_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_300_window_size_2_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_10_window_size_5_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_50_window_size_5_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_100_window_size_5_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_300_window_size_5_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_10_window_size_10_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_50_window_size_10_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_100_window_size_10_iteration_number_1000.model',
              'word2vec_genre_romance_vector_size_300_window_size_10_iteration_number_1000.model']

    simlex = SimLex()
    simlex_words = list(simlex.word_to_similar.keys())

    for models_names in [news_models, romance_models]:
        average_ndcg_list = list()
        average_map_list = list()
        for model_name in models_names:
            model = SimpleWord2Vec(f'/home/hamid/PycharmProjects/vector-lexical-semantics/word2vec/model/{model_name}')
            topKV = model.get_top_10(simlex_words)
            word2vec_words = list(topKV.keys())

            print()
            print(f"Model name: {model_name}")
            topKG = simlex.get_top_10(word2vec_words)

            evaluate = Evaluate(topKV, topKG, 'ndcg')
            average_ndcg_list.append(evaluate.average)

            evaluate = Evaluate(topKV, topKG, 'map')
            average_map_list.append(evaluate.average)

        print()
        print(news_models)
        print(average_ndcg_list)
        print(f"max ndcg: {max(average_ndcg_list)}")
        print(f"argmax ndcg: {numpy.argmax(average_ndcg_list)}")
        print(f"argmax ndcg model: {models_names[numpy.argmax(average_ndcg_list)]}")

        print()
        print(average_map_list)
        print(f"max map: {max(average_map_list)}")
        print(f"argmax map: {numpy.argmax(average_map_list)}")
        print(f"argmax map model: {models_names[numpy.argmax(average_map_list)]}")

        print("--------")