import pytrec_eval

from birkbeck import Birkbeck
from similarity import Similarity

if __name__ == '__main__':
    similarity = Similarity(10000)
    top_ten_similar = similarity.load_data(0, 200)

    birkbeck_words = Birkbeck().get_words()
    birkbeck_dict = dict()
    similar_dict = dict()
    for word in birkbeck_words:
        inner_dict = dict()
        inner_dict[word[1]] = 1
        birkbeck_dict[word[0]] = inner_dict

        similar_dict[word[0]] = dict()
        for index, similar in enumerate(top_ten_similar[word[0]]):
            similar_dict[word[0]][similar[0]] = 10 - index

    success_1_key = 'success_1'
    success_5_key = 'success_5'
    success_10_key = 'success_10'
    metrics = {success_1_key, success_5_key, success_10_key}
    evaluator = pytrec_eval.RelevanceEvaluator(birkbeck_dict, metrics)
    evaluation = evaluator.evaluate(similar_dict)
    total_success_1 = 0
    total_success_5 = 0
    total_success_10 = 0
    for word in evaluation:
        total_success_1 += evaluation[word][success_1_key]
        total_success_5 += evaluation[word][success_5_key]
        total_success_10 += evaluation[word][success_10_key]

    print(f"success_1 average: {total_success_1 / len(evaluation)}, "
          f"success_5 average: {total_success_5 / len(evaluation)}, "
          f"success_10 average: {total_success_10 / len(evaluation)}")