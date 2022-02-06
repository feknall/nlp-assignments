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
    num_processes = None

    def __init__(self, num_processes: int):
        self.create_result_dir()
        self.birkbeck_words = Birkbeck().get_words()
        self.wordnet_words = wordnet.get_wordnet_words()
        self.num_processes = num_processes

    def calculate_distance_matrix(self, word: str, word_list: list) -> list:
        output = list()
        for inner_word in word_list:
            output.append((inner_word, distance.get_distance(word, inner_word)))
        output = sorted(output, key=lambda tup: tup[1])
        return output

    def find_top_k_most_similar_in_wordnet(self, k: int, word: str, success_at: list) -> dict:
        similar = self.calculate_distance_matrix(word, self.wordnet_words)
        output = dict()
        for i in success_at:
            filtered_similar = filter(lambda tup: tup[1] <= i, similar)
            output[i] = list(filtered_similar)[:k]
        return output

    def find_top_5_most_similar_in_wordnet(self, list_1: list, success_at: list) -> dict:
        output = dict()
        for word in list_1:
            output[word] = self.find_top_k_most_similar_in_wordnet(5, word, success_at)
        return output

    def find_top_5_most_similar_birkbeck_wordnet(self, success_at: list):
        # total misspelled words: 13283
        birkbeck_misspelled_words = self.birkbeck_words
        with concurrent.futures.ProcessPoolExecutor(self.num_processes) as executor:
            futures = []
            for i in range(self.num_processes):
                page_size = int(len(birkbeck_misspelled_words) / self.num_processes)
                sublist = birkbeck_misspelled_words[i * page_size: (i + 1) * page_size]
                print(f"starting process {i}")
                futures.append(executor.submit(self.find_top_5_most_similar_in_wordnet, sublist, success_at))
            for index, future in enumerate(concurrent.futures.as_completed(futures)):
                return_value = future.result()
                with open(f'./{self.result_directory}/result-{index}', 'wb') as handle:
                    pickle.dump(return_value, handle, protocol=pickle.HIGHEST_PROTOCOL)
                    print(f"process {index} is completed")

    def load_data(self):
        output = dict()
        for i in range(self.num_processes):
            with open(f'./{self.result_directory}/result-{i}', 'rb') as handle:
                output = {**output, **pickle.load(handle)}
        return output

    def create_result_dir(self):
        if not os.path.exists(self.result_directory):
            os.makedirs(self.result_directory)