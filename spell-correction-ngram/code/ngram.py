from nltk.lm import MLE
import re
from nltk.lm.preprocessing import padded_everygram_pipeline


class Ngram:
    n = None
    model = None

    regex_pattern = "[A-Za-z]"
    pattern = re.compile(regex_pattern)

    def __init__(self, n, train_corpus: list):
        self.n = n
        self.model = MLE(self.n)
        train, vocab = padded_everygram_pipeline(n, train_corpus)
        self.model.fit(train, vocab)

    def predict_next_word(self, previous_words: list):
        text_seed = previous_words[-1 * (self.n - 1):]
        context = (
            text_seed[-self.model.order + 1:]
            if len(text_seed) >= self.model.order
            else text_seed
        )
        samples = self.model.context_counts(self.model.vocab.lookup(context))
        while context and not samples:
            context = context[1:] if len(context) > 1 else []
            samples = self.model.context_counts(self.model.vocab.lookup(context))
        samples = sorted(samples)
        return self._weighted_choice(samples, text_seed)

    def _weighted_choice(self, samples, context):
        weights = tuple(self.model.score(w, context) for w in samples)
        s = sorted(zip(weights, samples))[-10:]
        top_10 = [word[1] for word in s]
        return top_10

