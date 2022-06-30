from gensim.models import Word2Vec

from Corpus import Corpus

if __name__ == '__main__':
    windows_size_list = [1, 2, 5, 10]
    vector_size_list = [10, 50, 100, 300]
    iteration_number = 1000
    corpus = Corpus()
    sentences_list = [('news', corpus.news_words()), ('romance', corpus.romance_words())]

    print("Start training...")
    for windows_size in windows_size_list:
        for vector_size in vector_size_list:
            for sentences in sentences_list:
                model = Word2Vec(sentences=sentences[1],
                                 vector_size=vector_size,
                                 window=windows_size,
                                 epochs=iteration_number,
                                 min_count=1,
                                 workers=4)
                name = f'word2vec_' \
                       f'genre_{sentences[0]}_'\
                       f'vector_size_{vector_size}_'\
                       f'window_size_{windows_size}_'\
                       f'iteration_number_{iteration_number}.model'
                model.save(name)
                print(f"{name} trained successfully.")
