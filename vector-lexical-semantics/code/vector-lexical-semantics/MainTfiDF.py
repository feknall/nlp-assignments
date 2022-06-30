from Corpus import Corpus
from SimLex import SimLex
from TFiDF.TFiDF import TFiDF
from evaluate import Evaluate

if __name__ == '__main__':
    simlex = SimLex()
    corpus = Corpus()

    simlex_words = list(simlex.word_to_similar.keys())

    for sentences in [(corpus.news(), 'news'), (corpus.romance(), 'romance')]:
        tfidf = TFiDF(sentences[0])
        topKV = tfidf.get_top_10(simlex_words)
        tfidf_words = list(topKV.keys())

        topKG = simlex.get_top_10(tfidf_words)

        evaluate = Evaluate(topKV, topKG, 'map')
        print(f"Average map for {sentences[1]}: {evaluate.average}")

        evaluate = Evaluate(topKV, topKG, 'ndcg')
        print(f"Average ndcg for {sentences[1]}: {evaluate.average}")
