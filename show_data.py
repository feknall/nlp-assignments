import pytrec_eval
import json

if __name__ == '__main__':
    qrel = {
        'q1': {
            'd1': 0,
            'd2': 1,
            'd3': 0,
        }
    }

    run = {
        'word1': {

        }
    }

    evaluator = pytrec_eval.RelevanceEvaluator(qrel, {'success_30'})

    print(json.dumps(evaluator.evaluate(run), indent=1))