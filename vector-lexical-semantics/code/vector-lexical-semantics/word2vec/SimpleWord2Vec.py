from gensim.models import Word2Vec


class SimpleWord2Vec:
    model = None

    def __init__(self, path: str):
        self.model = Word2Vec.load(path)

    def get_top_10(self, words: list):
        output = {}
        for word in words:
            if word in self.model.wv.key_to_index:
                 output[word] = list()
                 similar_tuple_list = self.model.wv.most_similar(word, topn=10)
                 for similar_tuple in similar_tuple_list:
                     output[word].append(similar_tuple[0])
        return output