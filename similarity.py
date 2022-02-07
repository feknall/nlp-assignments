import wordnet
import distance
import concurrent.futures
import os
from birkbeck import Birkbeck
import pickle


class Similarity:
    result_directory = 'result'
    birkbeck_words = None
    wordnet_words = None
    birkbeck_total_parts = None

    def __init__(self, birkbeck_total_parts: int):
        self.create_result_dir()
        self.birkbeck_words = Birkbeck().get_misspelled_words()
        self.wordnet_words = wordnet.get_wordnet_words()
        self.birkbeck_total_parts = birkbeck_total_parts

    def calculate_distance_matrix(self, word: str, word_list: list) -> list:
        output = list()
        for inner_word in word_list:
            output.append((inner_word, distance.get_distance(word, inner_word)))
        output = sorted(output, key=lambda tup: tup[1])
        return output

    # def find_top_k_most_similar_in_wordnet(self, k: int, word: str, success_at: list) -> dict:
    #     similar = self.calculate_distance_matrix(word, self.wordnet_words)
    #     output = dict()
    #     for i in success_at:
    #         filtered_similar = filter(lambda tup: tup[1] <= i, similar)
    #         output[i] = list(filtered_similar)[:k]
    #     return output

    def find_top_10_most_similar_in_wordnet(self, list_1: list) -> dict:
        output = dict()
        for word in list_1:
            output[word] = self.calculate_distance_matrix(word, self.wordnet_words)[:10]
        return output

    def find_top_5_most_similar_birkbeck_wordnet_multiprocessing(self):
        # total misspelled words: 13283
        birkbeck_misspelled_words = self.birkbeck_words
        with concurrent.futures.ProcessPoolExecutor(self.birkbeck_total_parts) as executor:
            futures = []
            for i in range(self.birkbeck_total_parts):
                page_size = int(len(birkbeck_misspelled_words) / self.birkbeck_total_parts)
                sublist = birkbeck_misspelled_words[i * page_size: (i + 1) * page_size]
                print(f"starting process {i}")
                futures.append(executor.submit(self.find_top_10_most_similar_in_wordnet, sublist))
            for index, future in enumerate(concurrent.futures.as_completed(futures)):
                return_value = future.result()
                with open(f'./{self.result_directory}/result-{index}', 'wb') as handle:
                    pickle.dump(return_value, handle, protocol=pickle.HIGHEST_PROTOCOL)
                    print(f"process {index} is completed")

    def find_top_10_most_similar_birkbeck_wordnet_single_process(self, birkbeck_page: int):
        # total misspelled words: 13283
        page_size = int(len(self.birkbeck_words) / self.birkbeck_total_parts)
        sublist = self.birkbeck_words[birkbeck_page * page_size: (birkbeck_page + 1) * page_size]
        return_value = self.find_top_10_most_similar_in_wordnet(sublist)
        with open(f'./{self.result_directory}/result-{birkbeck_page}', 'wb') as handle:
            pickle.dump(return_value, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"page {birkbeck_page} is completed")

    def load_data(self, begin: int, end: int):
        output = dict()
        for i in range(begin, end + 1):
            with open(f'./{self.result_directory}/result-{i}', 'rb') as handle:
                output = {**output, **pickle.load(handle)}
        return output

    def create_result_dir(self):
        if not os.path.exists(self.result_directory):
            os.makedirs(self.result_directory)
