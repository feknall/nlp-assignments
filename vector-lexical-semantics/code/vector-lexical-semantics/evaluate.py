import pytrec_eval

class Evaluate:

    def __init__(self, topKV, topKG, metric: str):
        topKV_dict = {}
        for key in topKV:
            topKV_dict[key] = {}
            for index, word in enumerate(topKV[key]):
                topKV_dict[key][word] = 10 - index

        topKG_dict = {}
        for key in topKV:
            topKG_dict[key] = {}
            for index, word in enumerate(topKG[key]):
                topKG_dict[key][word] = 10 - index

        metrics = {metric}
        evaluator = pytrec_eval.RelevanceEvaluator(topKV_dict, metrics)
        evaluation = evaluator.evaluate(topKG_dict)

        self.sum = 0.0
        self.counter = 0
        self.size = len(evaluation)
        for word in evaluation:
            value = evaluation[word][metric]
            if value > 0:
                print(f"{word}: {value}")
                print(f"G: {topKG[word]}")
                print(f"V: {topKV[word]}")
                self.sum += value
                self.counter += 1
        self.average = self.sum / self.size
        print(f"Sum: {self.sum}")
        print(f"Size: {self.size}")
        print(f"Count: {self.counter}")
        print(f"Average: {self.average}")
