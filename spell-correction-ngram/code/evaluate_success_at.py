import pytrec_eval
from misspelled import Misspelled
from ngram import Ngram
from nltk.corpus import brown

if __name__ == '__main__':

    n_list = [1, 2, 3, 5, 10]
    train_corpus = brown.sents(categories=['news'])
    misspelled_words = Misspelled()
    for n in n_list:
        print(f"Start training {n}-gram")
        ngram = Ngram(n, train_corpus)
        print(f"Finish training {n}-gram")
        brown_dict = dict()
        predicted_dict = dict()
        for i in range(misspelled_words.get_size()):
            correct_word = misspelled_words.get_correct_words()[i]
            sentence = misspelled_words.get_sentences()[i]
            sentence_str = ' '.join(sentence) + correct_word
            inner_dict = dict()
            inner_dict[correct_word] = 1
            brown_dict[sentence_str] = inner_dict

            top_ten_prediction = ngram.predict_next_word(sentence)

            predicted_dict[sentence_str] = dict()
            for index, predicted in enumerate(top_ten_prediction):
                if predicted == correct_word:
                    print(f"sentence: {sentence}, {predicted}")
                predicted_dict[sentence_str][predicted] = 10 - index

        success_1_key = 'success_1'
        success_5_key = 'success_5'
        success_10_key = 'success_10'
        metrics = {success_1_key, success_5_key, success_10_key}
        evaluator = pytrec_eval.RelevanceEvaluator(brown_dict, metrics)
        evaluation = evaluator.evaluate(predicted_dict)
        total_success_1 = 0
        total_success_5 = 0
        total_success_10 = 0
        for word in evaluation:
            total_success_1 += evaluation[word][success_1_key]
            total_success_5 += evaluation[word][success_5_key]
            total_success_10 += evaluation[word][success_10_key]

        print(f"N is: {n}")
        print(f"success_1 average: {total_success_1 / len(evaluation)}, total: {total_success_1} "
              f"success_5 average: {total_success_5 / len(evaluation)}, total: {total_success_5} "
              f"success_10 average: {total_success_10 / len(evaluation)}, total: {total_success_10}")
