import pytrec_eval
import json

from similarity import Similarity

if __name__ == '__main__':
    similarity = Similarity(10000)
    data = similarity.load_data(0, 0)

    qrel = {
        'a': {
            'd1': 1
        }
    }

    run = {
        'a': {
            'd1': 8,
            'd2': 9,
            'd3': 6,
            'd4': 7
        }
    }

    evaluator = pytrec_eval.RelevanceEvaluator(qrel, {'success_2'})

    print(json.dumps(evaluator.evaluate(run), indent=1))